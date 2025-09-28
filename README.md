# 🌱 KrishiMitra - Smart Crop Recommendation System

**"Your Friend in Smart Agriculture"**

KrishiMitra is an advanced AI-powered crop recommendation system with sustainability scoring, intelligent filtering, and comprehensive fertilizer recommendations. Built to empower farmers with data-driven agricultural decisions while promoting sustainable farming practices.

## ✨ Features

### 🤖 **AI-Powered Recommendations**
- Machine Learning model trained on crop suitability data
- Intelligent probability scoring based on soil and environmental conditions
- Season-specific crop filtering and recommendations

### 🌍 **Sustainability & Environmental Focus**
- **Carbon Footprint Assessment**: 0-10 scale scoring for environmental impact
- **Water Efficiency Ratings**: Resource usage optimization metrics
- **Soil Health Impact**: Long-term agricultural sustainability analysis
- **Biodiversity Considerations**: Ecosystem impact evaluation

### 💧 **Smart Water Management**
- **Automatic Rainfall Calculation**: District + Season + Water Source integration
- **Real-time Updates**: Dynamic calculations as user changes selections
- **Water Source Integration**: Groundwater, Canal, River, Pond/Lake contributions

### 🧪 **Advanced Filtering System**
- **Fertilizer Requirements**: Filter by Low/Medium/High fertilizer needs
- **Sustainability Levels**: Filter by environmental impact scores
- **Smart Sorting**: Sort by suitability, sustainability, or fertilizer requirements

### 📋 **Detailed Fertilizer Recommendations**
- **Basal Application Schedules**: Precise timing and quantities
- **Top-dressing Plans**: Follow-up fertilization strategies
- **Organic Matter Guidance**: Compost and farmyard manure recommendations
- **Micronutrient Specifications**: Zinc, Boron, Molybdenum requirements
- **Complete Timing Calendar**: Full seasonal application schedules

### 🎨 **Modern User Interface**
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Interactive Elements**: Smooth animations and hover effects
- **Professional Styling**: Modern gradient design with intuitive navigation
- **Visual Feedback**: Progress indicators and real-time updates

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download the project**
   ```bash
   cd "G:\sih project\crop recoomadation\new daa"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the system**
   Open your web browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
KrishiMitra/
├── app.py                    # Main Flask application
├── crop_data.py             # Crop data, sustainability scores, and functions
├── crop_model.pkl           # Trained machine learning model
├── requirements.txt         # Python dependencies
├── setup_and_run.py         # Easy setup and launch script
├── templates/
│   └── index.html          # Web interface template
├── Crop_recommendation.csv  # Training dataset (reference)
└── README.md               # This documentation
```

## 🔧 System Components

### **Backend (app.py)**
- Flask web framework
- Machine learning model integration
- API endpoints for data and calculations
- Advanced filtering and sorting logic
- Sustainability scoring integration

### **Data Layer (crop_data.py)**
- Crop information and characteristics
- Sustainability scoring metrics
- Fertilizer requirement categories
- Detailed fertilizer recommendations
- Regional rainfall data
- Water source contribution factors

### **Frontend (templates/index.html)**
- Responsive web interface
- Advanced filter controls
- Real-time rainfall calculations
- Interactive recommendation displays
- Detailed fertilizer plan expansion

### **ML Model (crop_model.pkl)**
- Random Forest Classifier
- Trained on comprehensive crop dataset
- Features: N, P, K, temperature, humidity, pH, rainfall
- Supports 22 different crop types

## 🌾 Supported Crops

### **Cereals**
- Rice, Maize

### **Legumes (High Sustainability)**
- Chickpea, Kidneybeans, Pigeonpeas, Mothbeans, Mungbean, Blackgram, Lentil

### **Fruits**
- Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut

### **Cash Crops**
- Cotton, Jute, Coffee

## 📊 Sustainability Scoring

### **Scoring Criteria (0-10 scale)**
- **Carbon Score**: Greenhouse gas emissions and carbon sequestration
- **Water Efficiency**: Water usage optimization and conservation
- **Soil Health**: Impact on soil fertility and structure
- **Biodiversity**: Effect on local ecosystem diversity

### **Categories**
- **High Sustainability (8.0+)**: Legumes, environmentally friendly crops
- **Medium Sustainability (5.5-7.9)**: Balanced environmental impact
- **Low Sustainability (<5.5)**: High input, resource-intensive crops

## 🧪 Fertilizer Categories

### **Low Fertilizer Crops**
- Legumes (nitrogen-fixing): Chickpea, Lentil, Pigeonpeas, etc.
- Benefit: Reduced input costs, environmental sustainability

### **Medium Fertilizer Crops**
- Moderate input requirements: Maize, Pomegranate, Coffee, etc.
- Benefit: Balanced productivity and sustainability

### **High Fertilizer Crops**
- Intensive input needs: Rice, Cotton, Banana, etc.
- Benefit: High productivity potential with proper management

## 🔍 Usage Guide

1. **Enter Soil Parameters**: N, P, K levels, temperature, humidity, pH
2. **Select Location**: Choose season, district, and water source
3. **Apply Filters** (Optional): Set fertilizer and sustainability preferences
4. **Get Recommendations**: View ranked crop suggestions with detailed information
5. **Explore Details**: Click "Detailed Fertilizer Plan" for comprehensive guidance

## 🌐 API Endpoints

- `GET /get_rainfall_data` - Retrieve rainfall calculation data
- `GET /calculate_rainfall` - Calculate water availability for specific conditions
- `GET /get_filter_data` - Get filtering options and categories
- `GET /get_fertilizer_recommendation/<crop_name>` - Get detailed fertilizer plan

## 🤝 Contributing

This system is designed for agricultural decision support and sustainable farming practices. 

## 📝 License

Educational and research use.

## 🎯 Impact

This system promotes:
- **Sustainable Agriculture**: Environmentally conscious crop selection
- **Data-Driven Farming**: Evidence-based agricultural decisions
- **Resource Optimization**: Efficient use of water and fertilizers
- **Climate-Smart Agriculture**: Carbon footprint consideration
- **Farmer Empowerment**: Easy-to-use decision support tools

---

**Built with ❤️ for sustainable agriculture and environmental conservation**