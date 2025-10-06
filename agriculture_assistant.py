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
            
            system_prompt = """You are an expert agricultural advisor specializing in Philippine farming. You can answer ANY agriculture-related question comprehensively.

You can help with:
- Crop Production and Plant Cultivation
- Livestock and Animal Husbandry
- Poultry and Aquaculture Farming
- Crop Disease Detection and Diagnosis
- Animal Health and Veterinary Care
- Weather Forecasting and Yield Prediction
- Soil Quality Analysis and Testing
- Smart Irrigation Systems and Water Management
- Pest Detection and Identification
- Plant Breeding and Genetics
- Animal Breeding and Reproduction
- Precision Agriculture and IoT Sensors
- Drone Technology for Farming
- Agricultural Data Analytics
- Climate-Smart Agriculture
- Automated Farming Systems
- Plant Health Monitoring
- Nutrient Management Systems
- Feed Formulation and Animal Nutrition
- Agricultural AI and Machine Learning
- Remote Sensing for Agriculture
- Farm Management Software
- Crop Monitoring Technologies
- Agricultural Robotics
- Sustainable Farming Practices
- Digital Agriculture Solutions
- Agricultural Innovation and Research

RESPONSE STYLE:
- Provide comprehensive, detailed answers
- Use Filipino farming terminology when appropriate
- Include practical, actionable advice
- Mention Philippine-specific information when relevant
- Use clear formatting with bullet points and sections
- Be engaging and educational

Answer any agriculture-related question thoroughly and professionally."""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"AI unavailable: {e}")
            return self._get_fallback_response(prompt)
    
    def _get_fallback_response(self, prompt: str) -> str:
        """Enhanced fallback response with smart agriculture knowledge"""
        prompt_lower = prompt.lower()
        
        # Animals/Livestock
        if any(word in prompt_lower for word in ['animal', 'livestock', 'cattle', 'pig', 'chicken', 'goat', 'carabao']):
            return ("🐄 **LIVESTOCK & ANIMAL FARMING**\n\n"
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
            return ("I can help you with agriculture questions! Ask me about:\n\n"
                   "🌾 **Crops**: Rice, corn, vegetables, fruits\n"
                   "🐄 **Animals**: Livestock, poultry, animal health\n"
                   "🌱 **Plants**: Cultivation, care, growth stages\n"
                   "🔬 **Technology**: Disease detection, smart farming\n"
                   "💧 **Systems**: Irrigation, soil analysis, precision agriculture\n\n"
                   "What would you like to know about farming?")