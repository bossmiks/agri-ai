"""
Simple web interface for Agri-AI using Flask
"""

from flask import Flask, render_template, request, jsonify
from agriculture_assistant import AgricultureAssistant
from data_models import FarmingContext
import os

app = Flask(__name__)
assistant = AgricultureAssistant()

@app.route('/')
def landing():
    """Landing page"""
    return render_template('landing.html')

@app.route('/app')
def index():
    """Main app with farming context form"""
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    """API endpoint to get agriculture advice"""
    try:
        data = request.json
        
        context = FarmingContext(
            crop=data.get('crop', ''),
            location=data.get('location', ''),
            climate=data.get('climate', ''),
            soil_type=data.get('soil_type', ''),
            main_concern=data.get('main_concern', '')
        )
        
        advice = assistant.get_advice(context)
        
        return jsonify({
            'success': True,
            'advice': advice
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/crops')
def get_crops():
    """Get list of available crops"""
    crops = ["Rice", "Corn", "Banana", "Coconut", "Sugarcane", "Vegetables", "Fruits", "Other"]
    return jsonify(crops)

@app.route('/api/concerns')
def get_concerns():
    """Get list of farming concerns"""
    concerns = [
        "Water Management",
        "Pest Control", 
        "Disease Control",
        "Soil Health",
        "Yield Improvement",
        "Weather Planning",
        "General Advice"
    ]
    return jsonify(concerns)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)