"""
Philippine Agriculture AI Assistant
"""

import os

class AgricultureAssistant:
    """AI-powered agriculture assistant for Philippine farming"""
    
    def __init__(self):
        self.use_ai = os.getenv('USE_AI_MODEL', 'false').lower() == 'true'
    
    def get_chat_response(self, prompt: str) -> str:
        """Get AI response for farming questions"""
        if self.use_ai:
            return self._get_ai_response(prompt)
        else:
            return self._get_fallback_response(prompt)
    
    def _get_ai_response(self, prompt: str) -> str:
        """Get response from OpenAI API"""
        try:
            from openai import OpenAI
            client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            
            system_prompt = """You are Agri-AI, an expert agricultural advisor and conversational AI assistant specializing in Philippine farming. You have deep knowledge of agriculture and can engage in natural, helpful conversations about farming topics.

Your personality:
- Friendly, knowledgeable, and approachable like ChatGPT
- Patient and understanding with farmers of all experience levels
- Enthusiastic about helping improve Philippine agriculture
- Use conversational tone while maintaining expertise
- Acknowledge when you don't know something and suggest alternatives

Your expertise covers:
- All aspects of crop production (rice, corn, vegetables, fruits, etc.)
- Livestock and poultry farming (cattle, pigs, chickens, goats, carabao)
- Modern agricultural technology (IoT, precision farming, drones)
- Traditional Filipino farming methods and local knowledge
- Plant diseases, pests, and integrated management
- Soil health, fertilization, and sustainable practices
- Weather patterns, climate adaptation, and yield optimization
- Agricultural business, marketing, and economics
- Government programs (DA, ATI, LGU support)
- Post-harvest processing and value-adding

Conversation guidelines:
- Always stay focused on agriculture-related topics
- If asked about non-agricultural topics, politely redirect to farming
- Use Filipino terms when appropriate (palay, mais, saging, etc.)
- Provide practical, actionable advice tailored to Philippine conditions
- Ask clarifying questions when needed to give better advice
- Use emojis and formatting to make responses engaging
- Reference specific Philippine locations, varieties, and practices
- Suggest local resources and contacts when helpful

Example responses:
- Be conversational: "That's a great question about rice farming!"
- Show understanding: "I understand you're dealing with pest issues..."
- Provide context: "In the Philippines, this is especially important because..."
- Offer alternatives: "If that doesn't work, you could also try..."

Remember: You're here to help Filipino farmers succeed through friendly, expert agricultural guidance."""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI unavailable: {e}")
            return self._get_fallback_response(prompt)
    
    def _get_fallback_response(self, prompt: str) -> str:
        """Enhanced conversational fallback response"""
        prompt_lower = prompt.lower()
        
        # Check for non-agricultural topics and redirect
        non_agri_keywords = ['weather today', 'news', 'politics', 'sports', 'entertainment', 'cooking', 'recipe']
        if any(keyword in prompt_lower for keyword in non_agri_keywords):
            return ("I appreciate your question, but I'm specifically designed to help with agricultural topics! \n\n"
                   "I'd love to help you with farming questions instead. For example:\n"
                   "- How to improve crop yields\n"
                   "- Livestock care and management\n"
                   "- Pest and disease control\n"
                   "- Modern farming techniques\n\n"
                   "What farming challenge can I help you with today? 🌾")
        
        prompt_lower = prompt.lower()
        
        # Animals/Livestock
        if any(word in prompt_lower for word in ['animal', 'livestock', 'cattle', 'pig', 'chicken', 'goat', 'carabao']):
            return ("Great question about livestock farming! 🐄 Let me help you with animal agriculture in the Philippines.\n\n"
                   "**LIVESTOCK & ANIMAL FARMING**\n\n"
                   "**Common Philippine Livestock:**\n"
                   "- **Cattle**: Dairy and beef production\n"
                   "- **Pigs**: Backyard and commercial swine\n"
                   "- **Chickens**: Layers and broilers\n"
                   "- **Goats**: Meat and milk production\n"
                   "- **Carabao**: Draft animals and dairy\n\n"
                   "**Animal Health Management:**\n"
                   "- Regular vaccination schedules\n"
                   "- Proper nutrition and feeding\n"
                   "- Clean housing and sanitation\n"
                   "- Disease prevention and monitoring\n"
                   "- Veterinary care and check-ups\n\n"
                   "**Breeding Programs:**\n"
                   "- Select quality breeding stock\n"
                   "- Maintain breeding records\n"
                   "- Artificial insemination services\n"
                   "- Genetic improvement programs\n\n"
                   "**Feed and Nutrition:**\n"
                   "- Balanced commercial feeds\n"
                   "- Local feed ingredients (rice bran, copra meal)\n"
                   "- Forage crops and pasture management\n"
                   "- Mineral and vitamin supplements\n\n"
                   "Contact your local veterinarian or livestock technician for specific advice.")
        
        # Plants/Crops
        elif any(word in prompt_lower for word in ['plant', 'crop', 'vegetable', 'fruit', 'tree', 'flower']):
            return ("🌱 **PLANT & CROP CULTIVATION**\n\n"
                   "**Popular Philippine Crops:**\n"
                   "- **Vegetables**: Tomato, eggplant, okra, kangkong\n"
                   "- **Fruits**: Mango, banana, papaya, citrus\n"
                   "- **Root Crops**: Sweet potato, cassava, taro\n"
                   "- **Spices**: Ginger, turmeric, chili, onion\n"
                   "- **Ornamentals**: Orchids, roses, bougainvillea\n\n"
                   "**Plant Care Essentials:**\n"
                   "- **Soil Preparation**: Proper tillage and organic matter\n"
                   "- **Seed Selection**: Use certified, disease-free seeds\n"
                   "- **Watering**: Consistent moisture without waterlogging\n"
                   "- **Fertilization**: Balanced NPK and micronutrients\n"
                   "- **Pest Control**: Regular monitoring and IPM\n\n"
                   "**Growth Stages:**\n"
                   "- **Germination**: Proper temperature and moisture\n"
                   "- **Vegetative**: Nitrogen-rich fertilizers\n"
                   "- **Flowering**: Phosphorus and potassium boost\n"
                   "- **Fruiting**: Adequate water and nutrients\n"
                   "- **Harvest**: Proper timing for quality\n\n"
                   "**Plant Health Indicators:**\n"
                   "- Green, vigorous foliage\n"
                   "- Strong root development\n"
                   "- Normal growth patterns\n"
                   "- Absence of disease symptoms\n\n"
                   "Choose varieties suited to your local climate and soil conditions.")
        
        # Disease detection
        elif any(word in prompt_lower for word in ['disease', 'detect', 'symptom', 'diagnosis']):
            return ("🔬 **CROP DISEASE DETECTION**\n\n"
                   "**Common Philippine Crop Diseases:**\n"
                   "- **Rice**: Blast, Bacterial Leaf Blight, Tungro\n"
                   "- **Corn**: Downy Mildew, Rust, Ear Rot\n"
                   "- **Vegetables**: Bacterial Wilt, Mosaic Virus\n\n"
                   "**Detection Methods:**\n"
                   "- Visual inspection of leaves, stems, roots\n"
                   "- Use plant disease identification apps\n"
                   "- Laboratory testing for confirmation\n"
                   "- Monitor weather conditions (humidity, temperature)\n\n"
                   "**Early Detection Tips:**\n"
                   "- Check plants weekly for unusual spots or discoloration\n"
                   "- Look for wilting, stunted growth, or abnormal leaf patterns\n"
                   "- Document symptoms with photos for expert consultation\n\n"
                   "Contact your local DA plant pathologist for accurate diagnosis.")
        
        # Smart irrigation
        elif any(word in prompt_lower for word in ['irrigation', 'water', 'smart', 'automated']):
            return ("💧 **SMART IRRIGATION SYSTEMS**\n\n"
                   "**Smart Irrigation Technologies:**\n"
                   "- **Drip Irrigation**: Water-efficient, precise application\n"
                   "- **Sprinkler Systems**: Good for larger areas\n"
                   "- **Soil Moisture Sensors**: Monitor water needs\n"
                   "- **Weather-based Controllers**: Adjust based on conditions\n\n"
                   "**Benefits:**\n"
                   "- 30-50% water savings compared to traditional methods\n"
                   "- Reduced labor costs and time\n"
                   "- Better crop yields and quality\n"
                   "- Precise nutrient delivery through fertigation\n\n"
                   "**Implementation Tips:**\n"
                   "- Start with soil moisture monitoring\n"
                   "- Choose system based on crop type and field size\n"
                   "- Consider solar-powered options for remote areas\n"
                   "- Train on proper maintenance and operation\n\n"
                   "Consult with irrigation specialists for system design and installation.")
        
        # Weather and yield prediction
        elif any(word in prompt_lower for word in ['weather', 'yield', 'prediction', 'forecast']):
            return ("🌦️ **WEATHER & YIELD PREDICTION**\n\n"
                   "**Key Weather Factors:**\n"
                   "- **Rainfall**: Critical for crop growth timing\n"
                   "- **Temperature**: Affects flowering and fruiting\n"
                   "- **Humidity**: Influences disease pressure\n"
                   "- **Wind**: Impacts pollination and pest movement\n\n"
                   "**Yield Prediction Methods:**\n"
                   "- Monitor crop growth stages and development\n"
                   "- Track weather patterns during critical periods\n"
                   "- Use historical yield data for comparison\n"
                   "- Assess plant health and stress indicators\n\n"
                   "**Philippine Weather Resources:**\n"
                   "- PAGASA weather forecasts and warnings\n"
                   "- Local weather monitoring stations\n"
                   "- Agricultural weather apps and services\n"
                   "- Farmer weather networks and cooperatives\n\n"
                   "Plan your farming activities based on seasonal weather patterns.")
        
        # Precision agriculture
        elif any(word in prompt_lower for word in ['precision', 'iot', 'sensor', 'gps', 'technology']):
            return ("📡 **PRECISION AGRICULTURE & IoT**\n\n"
                   "**IoT Sensors for Farming:**\n"
                   "- **Soil Sensors**: Monitor moisture, temperature, pH\n"
                   "- **Weather Stations**: Track local climate conditions\n"
                   "- **Crop Monitoring**: Growth stages and health status\n"
                   "- **Livestock Tracking**: Animal health and location\n\n"
                   "**GPS Technology Applications:**\n"
                   "- **Field Mapping**: Accurate land measurement\n"
                   "- **Variable Rate Application**: Precise fertilizer/pesticide use\n"
                   "- **Yield Mapping**: Track productivity across fields\n"
                   "- **Equipment Guidance**: Automated tractor steering\n\n"
                   "**Data Analytics Benefits:**\n"
                   "- Optimize input usage and reduce costs\n"
                   "- Improve crop yields and quality\n"
                   "- Make data-driven farming decisions\n"
                   "- Monitor farm operations remotely\n\n"
                   "Start small and gradually expand your precision agriculture toolkit.")
        
        # Basic crops
        elif any(word in prompt_lower for word in ['rice', 'palay']):
            return ("🌾 **RICE FARMING ADVICE**\n\n"
                   "For rice farming in the Philippines:\n"
                   "- **Varieties**: Use certified seeds like PSB Rc82, NSIC Rc222\n"
                   "- **Planting**: Best during wet season (June-October)\n"
                   "- **Water**: Maintain 2-5cm water depth, use AWD method\n"
                   "- **Fertilizer**: Apply 14-14-14 at planting, urea at tillering\n"
                   "- **Pests**: Watch for stem borer, brown planthopper\n\n"
                   "Contact your local DA office for specific variety recommendations.")
        
        elif any(word in prompt_lower for word in ['corn', 'mais']):
            return ("🌽 **CORN FARMING ADVICE**\n\n"
                   "For corn farming in the Philippines:\n"
                   "- **Varieties**: Use hybrid varieties suited for your region\n"
                   "- **Planting**: Plant at start of rainy season or with irrigation\n"
                   "- **Spacing**: 75cm between rows, 25cm between plants\n"
                   "- **Fertilizer**: Apply complete fertilizer at planting\n"
                   "- **Pests**: Monitor for fall armyworm, corn borer\n\n"
                   "Visit your nearest ATI center for training programs.")
        
        else:
            return ("Hello! I'm your agriculture assistant, and I'm here to help with any farming questions you have! \n\n"
                   "I can assist you with:\n\n"
                   "🌾 **Crop Farming**: Rice, corn, vegetables, fruits, and more\n"
                   "🐄 **Livestock**: Cattle, pigs, chickens, goats, carabao care\n"
                   "🌱 **Plant Care**: From seed to harvest guidance\n"
                   "🔬 **Smart Farming**: Modern technology and techniques\n"
                   "💧 **Farm Systems**: Irrigation, soil health, pest management\n"
                   "💼 **Agri-Business**: Marketing, economics, and planning\n\n"
                   "Feel free to ask me anything about farming - I'm here to help you succeed! What's on your mind today?")