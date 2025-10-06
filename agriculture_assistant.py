"""
Core agriculture assistant with prompt-based AI responses
"""

from data_models import FarmingContext, AgricultureAdvice, PhilippinesAgriData
from prompt_templates import PromptTemplates
import json

class AgricultureAssistant:
    """Main agriculture assistant class"""
    
    def __init__(self):
        self.agri_data = PhilippinesAgriData()
        self.templates = PromptTemplates()
    
    def get_advice(self, context: FarmingContext) -> str:
        """Generate agriculture advice based on farming context"""
        
        # Normalize inputs
        crop = context.crop.lower()
        concern = context.main_concern.lower()
        
        # Route to specific advice based on concern
        if "water" in concern:
            return self._get_water_management_advice(context)
        elif "pest" in concern or "disease" in concern:
            return self._get_pest_disease_advice(context)
        elif "soil" in concern:
            return self._get_soil_health_advice(context)
        elif "yield" in concern:
            return self._get_yield_improvement_advice(context)
        elif "weather" in concern:
            return self._get_weather_advice(context)
        else:
            return self._get_general_advice(context)
    
    def _get_water_management_advice(self, context: FarmingContext) -> str:
        """Water management specific advice"""
        crop = context.crop.lower()
        climate = context.climate.lower()
        
        advice = f"💧 WATER MANAGEMENT for {context.crop.upper()}\n"
        advice += f"Location: {context.location} | Climate: {context.climate}\n\n"
        
        if "rice" in crop:
            if "wet" in climate:
                advice += "🌧️ WET SEASON RICE MANAGEMENT:\n"
                advice += "• Monitor field water levels (5-10cm depth)\n"
                advice += "• Install proper drainage to prevent flooding\n"
                advice += "• Use alternate wetting and drying (AWD) technique\n"
                advice += "• Check for water stagnation daily\n"
            else:
                advice += "☀️ DRY SEASON RICE MANAGEMENT:\n"
                advice += "• Ensure consistent irrigation supply\n"
                advice += "• Use drip or sprinkler irrigation\n"
                advice += "• Apply water every 2-3 days\n"
                advice += "• Mulch to retain soil moisture\n"
        
        elif "corn" in crop:
            advice += "🌽 CORN WATER MANAGEMENT:\n"
            advice += "• Water deeply but less frequently\n"
            advice += "• Critical periods: tasseling and grain filling\n"
            advice += "• Avoid waterlogging in clay soils\n"
            advice += "• Use furrow irrigation for better efficiency\n"
        
        elif "banana" in crop:
            advice += "🍌 BANANA WATER MANAGEMENT:\n"
            advice += "• Maintain consistent soil moisture\n"
            advice += "• Install drainage in monsoon season\n"
            advice += "• Water 2-3 times per week in dry season\n"
            advice += "• Use mulching to conserve moisture\n"
        
        advice += "\n⚠️ IMPORTANT REMINDERS:\n"
        advice += "• Check weather forecasts regularly\n"
        advice += "• Adjust irrigation based on rainfall\n"
        advice += "• Monitor soil moisture with simple tools\n"
        
        return advice
    
    def _get_pest_disease_advice(self, context: FarmingContext) -> str:
        """Pest and disease management advice"""
        crop = context.crop.lower()
        
        advice = f"🐛 PEST & DISEASE CONTROL for {context.crop.upper()}\n"
        advice += f"Location: {context.location} | Climate: {context.climate}\n\n"
        
        if "rice" in crop:
            advice += "🌾 COMMON RICE PESTS & DISEASES:\n"
            advice += "• Brown Planthopper: Use resistant varieties, avoid over-fertilizing\n"
            advice += "• Stem Borer: Apply neem oil, use pheromone traps\n"
            advice += "• Rice Blast: Improve air circulation, avoid excess nitrogen\n"
            advice += "• Bacterial Leaf Blight: Use certified seeds, crop rotation\n"
        
        elif "corn" in crop:
            advice += "🌽 COMMON CORN PESTS & DISEASES:\n"
            advice += "• Fall Armyworm: Early morning inspection, biological control\n"
            advice += "• Corn Borer: Remove crop residues, use Bt corn varieties\n"
            advice += "• Downy Mildew: Improve drainage, use resistant varieties\n"
            advice += "• Corn Rust: Apply fungicides preventively\n"
        
        elif "banana" in crop:
            advice += "🍌 COMMON BANANA PESTS & DISEASES:\n"
            advice += "• Bunchy Top Virus: Remove infected plants, control aphids\n"
            advice += "• Panama Disease: Use resistant varieties, soil sterilization\n"
            advice += "• Banana Weevil: Use pheromone traps, remove plant debris\n"
            advice += "• Black Sigatoka: Improve air circulation, fungicide application\n"
        
        advice += "\n🛡️ INTEGRATED PEST MANAGEMENT (IPM):\n"
        advice += "• Regular field monitoring (2-3 times per week)\n"
        advice += "• Use biological control agents when possible\n"
        advice += "• Rotate pesticides to prevent resistance\n"
        advice += "• Maintain field sanitation\n"
        advice += "• Plant trap crops around main crop\n"
        
        return advice
    
    def _get_soil_health_advice(self, context: FarmingContext) -> str:
        """Soil health management advice"""
        soil_type = context.soil_type.lower()
        
        advice = f"🌱 SOIL HEALTH MANAGEMENT\n"
        advice += f"Soil Type: {context.soil_type} | Crop: {context.crop}\n\n"
        
        if "sandy" in soil_type:
            advice += "🏖️ SANDY SOIL MANAGEMENT:\n"
            advice += "• Add organic matter (compost, manure)\n"
            advice += "• Use cover crops to prevent erosion\n"
            advice += "• Apply fertilizers in small, frequent doses\n"
            advice += "• Improve water retention with mulching\n"
        
        elif "clay" in soil_type:
            advice += "🧱 CLAY SOIL MANAGEMENT:\n"
            advice += "• Improve drainage with raised beds\n"
            advice += "• Add organic matter to improve structure\n"
            advice += "• Avoid working soil when wet\n"
            advice += "• Use gypsum to improve soil structure\n"
        
        elif "loamy" in soil_type:
            advice += "🌿 LOAMY SOIL MANAGEMENT:\n"
            advice += "• Maintain organic matter levels\n"
            advice += "• Practice crop rotation\n"
            advice += "• Regular soil testing (every 2-3 years)\n"
            advice += "• Balanced fertilization program\n"
        
        advice += "\n📊 SOIL TESTING RECOMMENDATIONS:\n"
        advice += "• Test pH levels (ideal: 6.0-7.0 for most crops)\n"
        advice += "• Check NPK levels\n"
        advice += "• Monitor organic matter content\n"
        advice += "• Test for micronutrients if needed\n"
        
        advice += "\n🌾 SOIL IMPROVEMENT PRACTICES:\n"
        advice += "• Apply compost or well-rotted manure\n"
        advice += "• Practice green manuring\n"
        advice += "• Use appropriate crop rotation\n"
        advice += "• Minimize soil compaction\n"
        
        return advice
    
    def _get_yield_improvement_advice(self, context: FarmingContext) -> str:
        """Yield improvement strategies"""
        crop = context.crop.lower()
        
        advice = f"📈 YIELD IMPROVEMENT for {context.crop.upper()}\n"
        advice += f"Location: {context.location} | Soil: {context.soil_type}\n\n"
        
        advice += "🎯 KEY STRATEGIES:\n"
        advice += "• Use high-quality, certified seeds\n"
        advice += "• Optimize planting density\n"
        advice += "• Implement proper fertilization program\n"
        advice += "• Ensure adequate water management\n"
        advice += "• Control pests and diseases effectively\n"
        advice += "• Practice proper crop spacing\n"
        
        if "rice" in crop:
            advice += "\n🌾 RICE-SPECIFIC TIPS:\n"
            advice += "• Use System of Rice Intensification (SRI) method\n"
            advice += "• Transplant young seedlings (14-21 days)\n"
            advice += "• Maintain proper plant spacing (25x25 cm)\n"
            advice += "• Apply balanced NPK fertilization\n"
        
        elif "corn" in crop:
            advice += "\n🌽 CORN-SPECIFIC TIPS:\n"
            advice += "• Plant at optimal density (60,000-75,000 plants/ha)\n"
            advice += "• Side-dress with nitrogen at V6 stage\n"
            advice += "• Ensure adequate phosphorus at planting\n"
            advice += "• Control weeds early in season\n"
        
        advice += "\n⏰ TIMING IS CRUCIAL:\n"
        advice += "• Plant at optimal time for your region\n"
        advice += "• Monitor growth stages closely\n"
        advice += "• Apply inputs at right growth stages\n"
        advice += "• Harvest at proper maturity\n"
        
        return advice
    
    def _get_weather_advice(self, context: FarmingContext) -> str:
        """Weather-related farming advice"""
        climate = context.climate.lower()
        
        advice = f"🌤️ WEATHER PLANNING for {context.crop.upper()}\n"
        advice += f"Current Climate: {context.climate} | Location: {context.location}\n\n"
        
        if "wet" in climate or "monsoon" in climate:
            advice += "🌧️ WET SEASON PREPARATIONS:\n"
            advice += "• Ensure proper field drainage\n"
            advice += "• Prepare for potential flooding\n"
            advice += "• Increase disease monitoring\n"
            advice += "• Adjust fertilizer application timing\n"
            advice += "• Harvest before heavy rains if possible\n"
        
        elif "dry" in climate:
            advice += "☀️ DRY SEASON PREPARATIONS:\n"
            advice += "• Secure irrigation water sources\n"
            advice += "• Plan water-efficient crops\n"
            advice += "• Use drought-resistant varieties\n"
            advice += "• Apply mulching to conserve moisture\n"
            advice += "• Monitor for heat stress in crops\n"
        
        advice += "\n📱 WEATHER MONITORING TOOLS:\n"
        advice += "• PAGASA weather forecasts\n"
        advice += "• Local weather apps\n"
        advice += "• Agricultural weather stations\n"
        advice += "• Community weather updates\n"
        
        advice += "\n🚨 EXTREME WEATHER PREPAREDNESS:\n"
        advice += "• Typhoon: Harvest early, secure equipment\n"
        advice += "• Drought: Water conservation, crop insurance\n"
        advice += "• Flooding: Drainage systems, elevated storage\n"
        advice += "• El Niño/La Niña: Adjust cropping calendar\n"
        
        return advice
    
    def _get_general_advice(self, context: FarmingContext) -> str:
        """General farming advice"""
        advice = f"🌾 GENERAL FARMING ADVICE for {context.crop.upper()}\n"
        advice += f"Location: {context.location} | Climate: {context.climate} | Soil: {context.soil_type}\n\n"
        
        advice += "📋 FARMING BEST PRACTICES:\n"
        advice += "• Plan your cropping calendar\n"
        advice += "• Keep detailed farm records\n"
        advice += "• Regular field monitoring\n"
        advice += "• Maintain equipment properly\n"
        advice += "• Stay updated with new technologies\n"
        
        advice += "\n💰 ECONOMIC CONSIDERATIONS:\n"
        advice += "• Monitor market prices regularly\n"
        advice += "• Consider crop insurance\n"
        advice += "• Plan for input costs\n"
        advice += "• Explore value-adding opportunities\n"
        
        advice += "\n🤝 RESOURCES & SUPPORT:\n"
        advice += "• Contact local agricultural extension office\n"
        advice += "• Join farmer cooperatives\n"
        advice += "• Attend agricultural training programs\n"
        advice += "• Connect with fellow farmers\n"
        
        return advice