from flask import Flask, render_template, request, jsonify
from joblib import load
from crop_data import (crop_info, growth_stages, crop_seasons, seasonal_rainfall, 
                      calculate_total_water_availability, get_rainfall_data_for_frontend, 
                      crop_rainfall_req, crop_sustainability_scores, fertilizer_categories,
                      get_sustainability_category, get_fertilizer_category, 
                      get_detailed_fertilizer_recommendation, get_filter_data_for_frontend)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'krishimitra-crop-recommendation-2024'

# Load trained Random Forest model for KrishiMitra
model = load("crop_model.pkl")  # Make sure this path is correct

# Features expected by the model
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

def dynamic_recommendation(crop, input_data, water_source, district, season):
    # Convert crop name to title case for data lookup
    crop_name = crop.strip().replace(" ","").title()
    
    # Fertilizer
    info = crop_info.get(crop_name, {"fertilizer": (0,0,0)})
    rec_N, rec_P, rec_K = info['fertilizer']
    N, P, K = input_data[0], input_data[1], input_data[2]
    added_N = max(0, rec_N-N)
    added_P = max(0, rec_P-P)
    added_K = max(0, rec_K-K)
    fert_msg = []
    if added_N>0: fert_msg.append(f"N: {added_N} kg/ha")
    if added_P>0: fert_msg.append(f"P: {added_P} kg/ha")
    if added_K>0: fert_msg.append(f"K: {added_K} kg/ha")
    fertilizer_msg = ", ".join(fert_msg) if fert_msg else "No additional fertilizer needed"
    
    # Rainfall check based on season and district
    min_r, max_r = seasonal_rainfall.get(season, {}).get(district, (0,1000))
    rainfall_val = input_data[6]
    rainfall_msg = "Sufficient" if min_r <= rainfall_val <= max_r else "Not Sufficient"
    
    # Growth stages - with defaults
    stages = growth_stages.get(crop_name, {
        "Sowing": "N/A",
        "Vegetative": "N/A", 
        "Flowering": "N/A",
        "Harvest": "N/A"
    })
    
    return rainfall_msg, fertilizer_msg, stages, rainfall_val

def calculate_crop_suitability_score(crop, input_data, season, district, water_source):
    """Calculate a comprehensive suitability score for a crop based on multiple factors"""
    crop_name = crop.strip().replace(" ","").title()
    
    # Base score from model probability (already filtered for season)
    score = 0.4  # Base score for being in correct season
    
    # Rainfall suitability (30% weight)
    available_water = calculate_total_water_availability(season, district, water_source)
    if crop_name in crop_rainfall_req:
        min_rain, max_rain = crop_rainfall_req[crop_name]
        if min_rain <= available_water <= max_rain:
            rainfall_score = 1.0
        elif available_water < min_rain:
            rainfall_score = max(0, available_water / min_rain)
        else:  # available_water > max_rain
            rainfall_score = max(0, 1 - ((available_water - max_rain) / max_rain))
    else:
        rainfall_score = 0.5  # Default if no data
    
    score += 0.3 * rainfall_score
    
    # Nutrient suitability (20% weight)
    if crop_name in crop_info:
        required_n, required_p, required_k = crop_info[crop_name]['fertilizer']
        actual_n, actual_p, actual_k = input_data[0], input_data[1], input_data[2]
        
        # Calculate nutrient adequacy (closer to required = better score)
        n_score = min(1.0, actual_n / max(required_n, 1))
        p_score = min(1.0, actual_p / max(required_p, 1))
        k_score = min(1.0, actual_k / max(required_k, 1))
        
        nutrient_score = (n_score + p_score + k_score) / 3
    else:
        nutrient_score = 0.5
    
    score += 0.2 * nutrient_score
    
    # Environmental suitability (10% weight) - temperature and humidity
    temp = input_data[3]
    humidity = input_data[4]
    
    # Simple environmental scoring (this could be enhanced with crop-specific data)
    temp_score = 1.0 if 15 <= temp <= 35 else max(0, 1 - abs(temp - 25) / 25)
    humidity_score = 1.0 if 40 <= humidity <= 90 else max(0, 1 - abs(humidity - 65) / 65)
    env_score = (temp_score + humidity_score) / 2
    
    score += 0.1 * env_score
    
    return min(1.0, score)  # Cap at 1.0

@app.route("/get_rainfall_data")
def get_rainfall_data():
    """API endpoint to get rainfall data for frontend calculations"""
    return jsonify(get_rainfall_data_for_frontend())

@app.route("/calculate_rainfall")
def calculate_rainfall():
    """API endpoint to calculate total water availability"""
    season = request.args.get('season', 'Kharif')
    district = request.args.get('district', 'Ranchi')
    water_source = request.args.get('water_source', 'Groundwater')
    
    total_water = calculate_total_water_availability(season, district, water_source)
    
    return jsonify({
        'total_water': total_water,
        'season': season,
        'district': district,
        'water_source': water_source
    })

@app.route("/get_filter_data")
def get_filter_data():
    """API endpoint to get filter data for frontend"""
    return jsonify(get_filter_data_for_frontend())

@app.route("/get_fertilizer_recommendation/<crop_name>")
def get_fertilizer_recommendation(crop_name):
    """API endpoint to get detailed fertilizer recommendation for a specific crop"""
    crop_title = crop_name.strip().replace(" ", "").title()
    recommendation = get_detailed_fertilizer_recommendation(crop_title)
    
    return jsonify({
        'crop': crop_title,
        'fertilizer_recommendation': recommendation,
        'fertilizer_category': get_fertilizer_category(crop_title),
        'sustainability_category': get_sustainability_category(crop_title)
    })

@app.route("/", methods=["GET","POST"])
def home():
    recommendations = []
    water_source = "Groundwater"
    district = "Ranchi"
    season = "Kharif"
    
    if request.method == "POST":
        # Read inputs (except rainfall which will be calculated)
        water_source = request.form.get("water_source", "Groundwater")
        district = request.form.get("district", "Ranchi")
        season = request.form.get("season", "Kharif")
        
        # Read filter preferences
        fertilizer_filter = request.form.get("fertilizer_filter", "All")
        sustainability_filter = request.form.get("sustainability_filter", "All")
        sort_by = request.form.get("sort_by", "suitability")  # suitability, sustainability, fertilizer
        
        # Calculate total water availability automatically
        calculated_rainfall = calculate_total_water_availability(season, district, water_source)
        
        # Build input data with calculated rainfall
        input_data = [
            float(request.form.get('N', 0)),
            float(request.form.get('P', 0)),
            float(request.form.get('K', 0)),
            float(request.form.get('temperature', 0)),
            float(request.form.get('humidity', 0)),
            float(request.form.get('ph', 0)),
            calculated_rainfall  # Use calculated rainfall instead of user input
        ]
        
        # Predict probabilities
        try:
            probs = model.predict_proba([input_data])[0]
            crops = model.classes_
            print(f"Debug - Input data: {input_data}")
            print(f"Debug - Season: {season}, District: {district}")
            print(f"Debug - Top predictions: {sorted(zip(crops, probs), key=lambda x: x[1], reverse=True)[:3]}")
        except Exception as e:
            print(f"Model error: {e}")
            return render_template("index.html", features=features, error=f"Model prediction error: {e}",
                                 water_source=water_source, district=district, season=season)
        
        # Filter crops by season (convert model output to title case for comparison)
        season_crops = crop_seasons.get(season, [])
        seasonal_crop_probs = [(c, p) for c, p in zip(crops, probs) if c.title() in season_crops]
        
        if seasonal_crop_probs:
            # Calculate combined scores (model probability + suitability)
            combined_scores = []
            
            for crop, model_prob in seasonal_crop_probs:
                suitability_score = calculate_crop_suitability_score(crop, input_data, season, district, water_source)
                # Combine model probability (40%) and suitability score (60%)
                combined_score = (0.4 * model_prob) + (0.6 * suitability_score)
                
                if combined_score > 0.2:  # Only include crops with reasonable scores
                    combined_scores.append((crop, combined_score))
            
            # Apply filters before normalization
            if combined_scores:
                filtered_scores = []
                
                for crop, score in combined_scores:
                    crop_title = crop.title()
                    
                    # Apply fertilizer filter
                    if fertilizer_filter != "All":
                        crop_fert_cat = get_fertilizer_category(crop_title)
                        if crop_fert_cat != fertilizer_filter:
                            continue
                    
                    # Apply sustainability filter
                    if sustainability_filter != "All":
                        crop_sust_cat = get_sustainability_category(crop_title)
                        if crop_sust_cat != sustainability_filter:
                            continue
                    
                    filtered_scores.append((crop, score))
                
                # Sort based on preference
                if sort_by == "sustainability" and filtered_scores:
                    # Sort by sustainability score
                    filtered_scores.sort(key=lambda x: crop_sustainability_scores.get(x[0].title(), {}).get('overall', 0), reverse=True)
                elif sort_by == "fertilizer" and filtered_scores:
                    # Sort by fertilizer requirement (Low first)
                    fert_order = {'Low': 3, 'Medium': 2, 'High': 1}
                    filtered_scores.sort(key=lambda x: fert_order.get(get_fertilizer_category(x[0].title()), 0), reverse=True)
                else:
                    # Default: sort by suitability score
                    filtered_scores.sort(key=lambda x: x[1], reverse=True)
                
                # Normalize filtered scores to sum to 100%
                if filtered_scores:
                    total_score = sum(score for _, score in filtered_scores)
                    normalized_scores = [(crop, score/total_score) for crop, score in filtered_scores]
                    crop_probs = normalized_scores[:5]  # Top 5 recommendations
                    
                    print(f"Debug - Season crops available: {len(seasonal_crop_probs)}")
                    print(f"Debug - After filters applied: {len(filtered_scores)}")
                    print(f"Debug - Fertilizer filter: {fertilizer_filter}, Sustainability filter: {sustainability_filter}")
                    print(f"Debug - Final normalized recommendations: {[(c, f'{p*100:.1f}%') for c, p in crop_probs[:3]]}")
                else:
                    crop_probs = []
            else:
                crop_probs = []
        else:
            crop_probs = []
        
        for crop, prob in crop_probs:
            crop_title = crop.title()
            rainfall_msg, fert_msg, stages, rainfall_val = dynamic_recommendation(crop, input_data, water_source, district, season)
            
            # Get sustainability and fertilizer data
            sustainability_data = crop_sustainability_scores.get(crop_title, {})
            fertilizer_category = get_fertilizer_category(crop_title)
            sustainability_category = get_sustainability_category(crop_title)
            detailed_fertilizer = get_detailed_fertilizer_recommendation(crop_title)
            
            recommendations.append({
                "crop": crop_title,
                "probability": f"{prob*100:.2f}",
                "rainfall": rainfall_msg,
                "rainfall_value": rainfall_val,
                "fertilizer": fert_msg,
                "fertilizer_category": fertilizer_category,
                "detailed_fertilizer": detailed_fertilizer,
                "sustainability_category": sustainability_category,
                "sustainability_score": sustainability_data.get('overall', 0),
                "carbon_score": sustainability_data.get('carbon_score', 0),
                "water_efficiency": sustainability_data.get('water_efficiency', 0),
                "soil_health": sustainability_data.get('soil_health', 0),
                "biodiversity": sustainability_data.get('biodiversity', 0),
                "stages": stages,
                "water_source": water_source,
                "district": district,
                "season": season
            })
    
    # Calculate initial rainfall for display
    initial_rainfall = calculate_total_water_availability(season, district, water_source)
    
    return render_template("index.html", features=features, recommendations=recommendations,
                           water_source=water_source, district=district, season=season,
                           calculated_rainfall=initial_rainfall, 
                           fertilizer_categories=fertilizer_categories,
                           fertilizer_filter=fertilizer_filter if request.method == "POST" else "All",
                           sustainability_filter=sustainability_filter if request.method == "POST" else "All",
                           sort_by=sort_by if request.method == "POST" else "suitability")

if __name__ == "__main__":
    app.run(debug=True)
