# crop_data.py

# Fertilizer info for all 22 crops
crop_info = {
    'Rice': {'fertilizer': (100,50,50)}, 'Maize': {'fertilizer': (120,60,60)},
    'Chickpea': {'fertilizer': (20,40,20)}, 'Kidneybeans': {'fertilizer': (25,30,20)},
    'Pigeonpeas': {'fertilizer': (30,30,20)}, 'Mothbeans': {'fertilizer': (25,25,20)},
    'Mungbean': {'fertilizer': (20,25,20)}, 'Blackgram': {'fertilizer': (20,25,20)},
    'Lentil': {'fertilizer': (20,30,20)}, 'Pomegranate': {'fertilizer': (50,30,40)},
    'Banana': {'fertilizer': (120,60,60)}, 'Mango': {'fertilizer': (80,40,40)},
    'Grapes': {'fertilizer': (70,50,50)}, 'Watermelon': {'fertilizer': (50,30,40)},
    'Muskmelon': {'fertilizer': (50,30,40)}, 'Apple': {'fertilizer': (80,50,50)},
    'Orange': {'fertilizer': (70,40,40)}, 'Papaya': {'fertilizer': (60,30,40)},
    'Coconut': {'fertilizer': (100,50,50)}, 'Cotton': {'fertilizer': (90,40,60)},
    'Jute': {'fertilizer': (70,30,30)}, 'Coffee': {'fertilizer': (80,40,50)}
}

# Growth stages for crops
growth_stages = {
    "Rice": {"Sowing":"Jun-Jul","Vegetative":"Jul-Sep","Flowering":"Sep-Oct","Harvest":"Oct-Nov"},
    "Maize": {"Sowing":"Jun-Jul","Vegetative":"Jul-Sep","Flowering":"Sep-Oct","Harvest":"Oct-Nov"},
    "Chickpea": {"Sowing":"Oct-Nov","Vegetative":"Nov-Dec","Flowering":"Dec-Jan","Harvest":"Jan-Feb"},
    "Kidneybeans": {"Sowing":"Oct","Vegetative":"Nov-Dec","Flowering":"Dec-Jan","Harvest":"Feb"},
    "Pigeonpeas": {"Sowing":"Jun-Jul","Vegetative":"Jul-Sep","Flowering":"Sep-Oct","Harvest":"Oct-Nov"},
    "Mothbeans": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Sep-Oct"},
    "Mungbean": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Sep-Oct"},
    "Blackgram": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Sep-Oct"},
    "Lentil": {"Sowing":"Oct-Nov","Vegetative":"Nov-Dec","Flowering":"Dec-Jan","Harvest":"Feb-Mar"},
    "Pomegranate": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Jan-Feb"},
    "Banana": {"Sowing":"Jan-Feb","Vegetative":"Feb-Apr","Flowering":"Apr-Jun","Harvest":"Jun-Aug"},
    "Mango": {"Sowing":"Mar-Apr","Vegetative":"Apr-Jun","Flowering":"Jun-Jul","Harvest":"Jul-Sep"},
    "Grapes": {"Sowing":"Feb-Mar","Vegetative":"Mar-Apr","Flowering":"Apr-May","Harvest":"Jul-Aug"},
    "Watermelon": {"Sowing":"Feb-Mar","Vegetative":"Mar-Apr","Flowering":"Apr-May","Harvest":"Jun-Jul"},
    "Muskmelon": {"Sowing":"Feb-Mar","Vegetative":"Mar-Apr","Flowering":"Apr-May","Harvest":"Jun-Jul"},
    "Apple": {"Sowing":"Apr-May","Vegetative":"May-Jun","Flowering":"Jun-Jul","Harvest":"Sep-Oct"},
    "Orange": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Dec-Jan"},
    "Papaya": {"Sowing":"Jan-Feb","Vegetative":"Feb-Apr","Flowering":"Apr-Jun","Harvest":"Jun-Aug"},
    "Coconut": {"Sowing":"Jan-Feb","Vegetative":"Feb-Apr","Flowering":"Apr-Jun","Harvest":"Jun-Aug"},
    "Cotton": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Aug-Sep","Harvest":"Oct-Nov"},
    "Jute": {"Sowing":"Apr-May","Vegetative":"May-Jun","Flowering":"Jun-Jul","Harvest":"Sep-Oct"},
    "Coffee": {"Sowing":"Jun-Jul","Vegetative":"Jul-Aug","Flowering":"Sep-Oct","Harvest":"Nov-Dec"}
}

# Seasons mapping
crop_seasons = {
    "Kharif": ["Rice", "Maize", "Pigeonpeas", "Mothbeans", "Mungbean", "Blackgram", "Cotton"],
    "Rabi": ["Chickpea", "Kidneybeans", "Lentil"],
    "Zaid": ["Watermelon", "Muskmelon", "Papaya", "Banana", "Coconut", "Grapes", "Mango"]
}

# District-wise seasonal rainfall (mm)
district_rainfall = {
    "Ranchi": {"Kharif": 120, "Rabi": 45, "Zaid": 80},
    "Jamshedpur": {"Kharif": 110, "Rabi": 40, "Zaid": 75},
    "Dhanbad": {"Kharif": 105, "Rabi": 35, "Zaid": 70},
    "Giridih": {"Kharif": 115, "Rabi": 50, "Zaid": 85},
    "Hazaribagh": {"Kharif": 125, "Rabi": 55, "Zaid": 90}
}

# Water source contribution (mm per season)
water_source_contribution = {
    "Groundwater": 20,
    "River": 25,
    "Canal": 30,
    "Pond/Lake": 15,
    "Borewell": 20
}

# Crop-specific rainfall requirements (mm)
crop_rainfall_req = {
    "Rice": (100, 200), "Maize": (80, 120), "Chickpea": (40, 60),
    "Kidneybeans": (45, 70), "Pigeonpeas": (60, 100), "Mothbeans": (30, 50),
    "Mungbean": (50, 75), "Blackgram": (50, 75), "Lentil": (40, 60),
    "Pomegranate": (50, 80), "Banana": (100, 150), "Mango": (60, 100),
    "Grapes": (60, 100), "Watermelon": (50, 80), "Muskmelon": (50, 80),
    "Apple": (70, 100), "Orange": (70, 100), "Papaya": (80, 120),
    "Coconut": (100, 150), "Cotton": (60, 90), "Jute": (100, 140),
    "Coffee": (120, 180)
}

seasonal_rainfall = {
    "Kharif": {
        "Ranchi": (75,170), "Jamshedpur": (70,160), "Dhanbad": (65,150), "Giridih": (70,160), "Hazaribagh": (60,150)
    },
    "Rabi": {
        "Ranchi": (40,90), "Jamshedpur": (35,85), "Dhanbad": (30,80), "Giridih": (35,85), "Hazaribagh": (30,80)
    },
    "Zaid": {
        "Ranchi": (50,120), "Jamshedpur": (45,110), "Dhanbad": (40,100), "Giridih": (45,110), "Hazaribagh": (40,100)
    }
}

def calculate_total_water_availability(season, district, water_source):
    """Calculate total water availability from natural rainfall + water source"""
    # Get base district rainfall for the season
    base_rainfall = district_rainfall.get(district, {}).get(season, 0)
    
    # Get water source contribution
    water_contribution = water_source_contribution.get(water_source, 0)
    
    # Calculate total available water
    total_water = base_rainfall + water_contribution
    
    return total_water

# Crop sustainability scores (0-10, higher is more sustainable)
# Based on: carbon footprint, water efficiency, soil health impact, biodiversity
crop_sustainability_scores = {
    # Cereals - generally moderate sustainability
    'Rice': {'carbon_score': 4, 'water_efficiency': 3, 'soil_health': 6, 'biodiversity': 5, 'overall': 4.5},
    'Maize': {'carbon_score': 6, 'water_efficiency': 7, 'soil_health': 7, 'biodiversity': 6, 'overall': 6.5},
    
    # Legumes - high sustainability (nitrogen fixation)
    'Chickpea': {'carbon_score': 8, 'water_efficiency': 8, 'soil_health': 9, 'biodiversity': 7, 'overall': 8.0},
    'Kidneybeans': {'carbon_score': 8, 'water_efficiency': 7, 'soil_health': 9, 'biodiversity': 7, 'overall': 7.8},
    'Pigeonpeas': {'carbon_score': 9, 'water_efficiency': 8, 'soil_health': 9, 'biodiversity': 8, 'overall': 8.5},
    'Mothbeans': {'carbon_score': 8, 'water_efficiency': 9, 'soil_health': 8, 'biodiversity': 7, 'overall': 8.0},
    'Mungbean': {'carbon_score': 8, 'water_efficiency': 8, 'soil_health': 9, 'biodiversity': 7, 'overall': 8.0},
    'Blackgram': {'carbon_score': 8, 'water_efficiency': 7, 'soil_health': 9, 'biodiversity': 7, 'overall': 7.8},
    'Lentil': {'carbon_score': 8, 'water_efficiency': 8, 'soil_health': 9, 'biodiversity': 7, 'overall': 8.0},
    
    # Fruits - moderate to low sustainability (high water/carbon needs)
    'Pomegranate': {'carbon_score': 5, 'water_efficiency': 4, 'soil_health': 6, 'biodiversity': 6, 'overall': 5.3},
    'Banana': {'carbon_score': 4, 'water_efficiency': 3, 'soil_health': 5, 'biodiversity': 5, 'overall': 4.3},
    'Mango': {'carbon_score': 5, 'water_efficiency': 4, 'soil_health': 6, 'biodiversity': 7, 'overall': 5.5},
    'Grapes': {'carbon_score': 4, 'water_efficiency': 4, 'soil_health': 5, 'biodiversity': 5, 'overall': 4.5},
    'Watermelon': {'carbon_score': 5, 'water_efficiency': 5, 'soil_health': 6, 'biodiversity': 5, 'overall': 5.3},
    'Muskmelon': {'carbon_score': 5, 'water_efficiency': 5, 'soil_health': 6, 'biodiversity': 5, 'overall': 5.3},
    'Apple': {'carbon_score': 4, 'water_efficiency': 5, 'soil_health': 6, 'biodiversity': 6, 'overall': 5.3},
    'Orange': {'carbon_score': 4, 'water_efficiency': 4, 'soil_health': 6, 'biodiversity': 6, 'overall': 5.0},
    'Papaya': {'carbon_score': 5, 'water_efficiency': 5, 'soil_health': 6, 'biodiversity': 6, 'overall': 5.5},
    'Coconut': {'carbon_score': 6, 'water_efficiency': 6, 'soil_health': 7, 'biodiversity': 7, 'overall': 6.5},
    
    # Cash crops - variable sustainability
    'Cotton': {'carbon_score': 3, 'water_efficiency': 2, 'soil_health': 4, 'biodiversity': 4, 'overall': 3.3},
    'Jute': {'carbon_score': 7, 'water_efficiency': 6, 'soil_health': 7, 'biodiversity': 6, 'overall': 6.5},
    'Coffee': {'carbon_score': 5, 'water_efficiency': 4, 'soil_health': 6, 'biodiversity': 7, 'overall': 5.5}
}

# Fertilizer requirement categories
fertilizer_categories = {
    'Low': ['Chickpea', 'Kidneybeans', 'Pigeonpeas', 'Mothbeans', 'Mungbean', 'Blackgram', 'Lentil'],
    'Medium': ['Maize', 'Pomegranate', 'Watermelon', 'Muskmelon', 'Apple', 'Orange', 'Papaya', 'Jute', 'Coffee'],
    'High': ['Rice', 'Banana', 'Mango', 'Grapes', 'Coconut', 'Cotton']
}

# Detailed fertilizer recommendations with specific products
detailed_fertilizer_recommendations = {
    'Rice': {
        'basal': 'Apply 50% of Nitrogen (Urea), full Phosphorus (DAP) and Potassium (MOP) at planting',
        'top_dressing': 'Apply remaining 50% Nitrogen in 2 splits: 25% at tillering, 25% at panicle initiation',
        'organic': 'Apply 10-15 tons/hectare well-decomposed farmyard manure 2 weeks before transplanting',
        'micronutrients': 'Zinc sulfate 25 kg/ha if deficient, Iron sulfate for iron-deficient soils',
        'timing': 'Basal: At transplanting, Top dress: 3-4 weeks and 6-7 weeks after transplanting'
    },
    'Maize': {
        'basal': 'Apply 50% Nitrogen, full Phosphorus (DAP) and Potassium (MOP) at sowing',
        'top_dressing': 'Apply 25% Nitrogen at knee-high stage, 25% at tasseling stage',
        'organic': 'Apply 8-10 tons/hectare well-decomposed farmyard manure before sowing',
        'micronutrients': 'Zinc sulfate 25 kg/ha, Boron 1-2 kg/ha if deficient',
        'timing': 'Basal: At sowing, Top dress: 30-35 days and 55-60 days after sowing'
    },
    'Chickpea': {
        'basal': 'Apply full Phosphorus (DAP) and Potassium at sowing, minimal Nitrogen (20 kg/ha)',
        'top_dressing': 'Generally not required due to nitrogen fixation',
        'organic': 'Apply 5-7 tons/hectare compost or farmyard manure',
        'micronutrients': 'Molybdenum seed treatment, Sulfur 40 kg/ha',
        'timing': 'All fertilizers at sowing, rhizobium inoculation of seeds'
    },
    'Kidneybeans': {
        'basal': 'Apply full Phosphorus, Potassium and 25% Nitrogen at planting',
        'top_dressing': 'Light nitrogen top-dressing at flowering if needed',
        'organic': 'Apply 6-8 tons/hectare well-decomposed manure',
        'micronutrients': 'Rhizobium inoculation, Molybdenum seed treatment',
        'timing': 'Basal at planting, light top-dress at 40-45 days if required'
    },
    'Pigeonpeas': {
        'basal': 'Apply full Phosphorus and Potassium, minimal Nitrogen at sowing',
        'top_dressing': 'Generally not required, excellent nitrogen fixer',
        'organic': 'Apply 8-10 tons/hectare farmyard manure',
        'micronutrients': 'Rhizobium inoculation essential, Sulfur supplementation',
        'timing': 'All at sowing with proper rhizobium inoculation'
    },
    'Cotton': {
        'basal': 'Apply 25% Nitrogen, full Phosphorus and Potassium at sowing',
        'top_dressing': 'Apply 50% N at squaring, 25% N at flowering stage',
        'organic': 'Apply 12-15 tons/hectare farmyard manure',
        'micronutrients': 'Zinc sulfate, Boron, Magnesium sulfate as per soil test',
        'timing': 'Basal: At sowing, Top dress: 45-50 days and 80-85 days after sowing'
    }
    # Add more crops as needed...
}

def get_sustainability_category(crop_name):
    """Return sustainability category based on overall score"""
    if crop_name in crop_sustainability_scores:
        score = crop_sustainability_scores[crop_name]['overall']
        if score >= 7.5:
            return 'High'
        elif score >= 5.5:
            return 'Medium'
        else:
            return 'Low'
    return 'Unknown'

def get_fertilizer_category(crop_name):
    """Return fertilizer requirement category"""
    for category, crops in fertilizer_categories.items():
        if crop_name in crops:
            return category
    return 'Medium'  # Default

def get_detailed_fertilizer_recommendation(crop_name):
    """Get detailed fertilizer recommendation for a crop"""
    if crop_name in detailed_fertilizer_recommendations:
        return detailed_fertilizer_recommendations[crop_name]
    else:
        # Default recommendation based on fertilizer requirements
        n, p, k = crop_info.get(crop_name, {"fertilizer": (50, 30, 30)})['fertilizer']
        return {
            'basal': f'Apply {n//2} kg N, {p} kg P2O5, {k} kg K2O per hectare at sowing',
            'top_dressing': f'Apply remaining {n//2} kg N at active growth stage',
            'organic': 'Apply 8-10 tons well-decomposed farmyard manure per hectare',
            'micronutrients': 'Apply micronutrients based on soil test results',
            'timing': 'Basal at sowing, top-dress at 30-45 days after sowing'
        }

def get_rainfall_data_for_frontend():
    """Return rainfall data structure for frontend JavaScript"""
    return {
        'district_rainfall': district_rainfall,
        'water_source_contribution': water_source_contribution
    }

def get_filter_data_for_frontend():
    """Return filter data for frontend"""
    return {
        'fertilizer_categories': fertilizer_categories,
        'sustainability_scores': crop_sustainability_scores
    }
