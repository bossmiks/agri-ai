# 🌾 Agri-AI: Agriculture Assistant for Philippines

An AI-powered agriculture assistant designed specifically for Filipino farmers to provide personalized farming advice based on local conditions, crops, and challenges.

## Features

- **Crop-Specific Advice**: Tailored recommendations for rice, corn, banana, coconut, and other Philippine crops
- **Climate-Aware**: Considers wet season, dry season, and monsoon patterns
- **Soil-Specific**: Provides advice based on different soil types (sandy, clay, loamy)
- **Multiple Concerns**: Covers water management, pest control, soil health, yield improvement, and weather planning
- **Web Interface**: Easy-to-use web application
- **Command Line**: Terminal-based interface for quick consultations

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Command Line Version
```bash
python main.py
```

### 3. Run Web Interface
```bash
python web_interface.py
```
Then open http://localhost:5000 in your browser.

## Usage Examples

### Water Management for Rice
- **Input**: Rice, Central Luzon, Wet season, Clay soil, Water Management
- **Output**: Specific irrigation techniques, drainage recommendations, and water scheduling

### Pest Control for Corn
- **Input**: Corn, Mindanao, Dry season, Sandy loam, Pest Control
- **Output**: Common pests identification, IPM strategies, and organic control methods

### Soil Health for Banana
- **Input**: Banana, Southern Luzon, Monsoon, Sandy soil, Soil Health
- **Output**: Soil improvement techniques, nutrient management, and testing recommendations

## Supported Crops

- Rice (Palay)
- Corn (Mais)
- Banana (Saging)
- Coconut (Niyog)
- Sugarcane (Tubo)
- Vegetables
- Fruits
- Other crops

## Farming Concerns Covered

1. **Water Management**: Irrigation, drainage, water conservation
2. **Pest Control**: Identification, prevention, organic/chemical control
3. **Disease Control**: Common diseases, prevention, treatment
4. **Soil Health**: Testing, improvement, nutrient management
5. **Yield Improvement**: Optimization strategies, best practices
6. **Weather Planning**: Seasonal planning, climate adaptation

## File Structure

```
agri-ai/
├── main.py                 # Command line interface
├── web_interface.py        # Flask web application
├── agriculture_assistant.py # Core AI logic
├── data_models.py          # Data structures
├── prompt_templates.py     # AI prompt templates
├── templates/
│   └── index.html         # Web interface template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Contributing

This system is designed to be easily extensible:

1. **Add New Crops**: Update `PhilippinesAgriData` in `data_models.py`
2. **Add New Advice Types**: Extend methods in `AgricultureAssistant`
3. **Improve Prompts**: Modify templates in `prompt_templates.py`
4. **Enhance UI**: Update HTML/CSS in `templates/index.html`

## Local Context

This system is specifically designed for Philippine agriculture, considering:

- Local climate patterns (wet/dry seasons, monsoons)
- Common Philippine crops and varieties
- Regional farming practices
- Local pest and disease challenges
- Philippine soil types and conditions
- PAGASA weather integration recommendations

## License

Open source - feel free to modify and distribute for agricultural education and support.

---

**Made with ❤️ for Filipino farmers**