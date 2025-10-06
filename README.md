# 🌾 Agri-AI: Agriculture Assistant for Philippines

AI-powered agriculture assistant designed for Filipino farmers with ChatGPT-style interface.

## Features

- **Chat Interface**: Ask farming questions naturally like ChatGPT
- **OpenAI Integration**: Powered by GPT for intelligent responses
- **Philippine Focus**: Specialized for local crops, climate, and conditions
- **Web Interface**: Easy-to-use browser-based chat

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key
```bash
set OPENAI_API_KEY=your_api_key_here
set USE_AI_MODEL=true
```

### 3. Run Web Interface
```bash
python web_interface.py
```
Then open http://localhost:5000

## Usage

Simply type your farming questions:
- "How do I grow rice in wet season?"
- "What pests affect corn in Mindanao?"
- "Best soil for banana farming?"
- "Water management for coconut trees"

## File Structure

```
agri-ai/
├── web_interface.py        # Flask web application
├── agriculture_assistant.py # Core AI logic
├── data_models.py          # Data structures
├── templates/
│   ├── landing.html       # Landing page
│   └── index.html         # Chat interface
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Requirements

- Python 3.7+
- OpenAI API key
- Flask
- Internet connection

---

**Made with ❤️ for Filipino farmers**