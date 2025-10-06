"""
Web interface for Philippine Agriculture AI Assistant
"""

from flask import Flask, render_template, request, jsonify
from agriculture_assistant import AgricultureAssistant
import os

app = Flask(__name__)
assistant = AgricultureAssistant()

@app.route('/')
def landing():
    """Landing page"""
    return render_template('landing.html')

@app.route('/app')
def index():
    """Main chat interface"""
    return render_template('index.html')

@app.route('/get_advice', methods=['POST'])
def get_advice():
    """API endpoint for chat responses"""
    try:
        data = request.json
        prompt = data.get('prompt', '').strip()
        
        if not prompt:
            return jsonify({
                'success': False, 
                'error': 'Please enter your farming question'
            })
        
        # Get AI response
        advice = assistant.get_chat_response(prompt)
        
        return jsonify({
            'success': True,
            'advice': advice
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Sorry, something went wrong. Please try again.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)