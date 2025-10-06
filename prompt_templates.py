"""
Prompt templates for agriculture AI responses
"""

class PromptTemplates:
    """Collection of prompt templates for different agriculture scenarios"""
    
    WATER_MANAGEMENT_TEMPLATE = """
    Based on the farming context:
    - Crop: {crop}
    - Location: {location}
    - Climate: {climate}
    - Soil: {soil_type}
    
    Provide specific water management advice including:
    1. Irrigation techniques suitable for the crop and climate
    2. Water scheduling recommendations
    3. Drainage considerations
    4. Water conservation methods
    5. Climate-specific adjustments
    """
    
    PEST_DISEASE_TEMPLATE = """
    For {crop} farming in {location} during {climate} season:
    
    Provide comprehensive pest and disease management advice:
    1. Common pests and diseases for this crop in Philippines
    2. Prevention strategies
    3. Organic and chemical control options
    4. Integrated Pest Management (IPM) approach
    5. Monitoring and early detection methods
    """
    
    SOIL_HEALTH_TEMPLATE = """
    Soil health management for:
    - Soil Type: {soil_type}
    - Crop: {crop}
    - Climate: {climate}
    
    Include advice on:
    1. Soil-specific management practices
    2. Organic matter improvement
    3. Nutrient management
    4. Soil testing recommendations
    5. Long-term soil conservation
    """
    
    YIELD_IMPROVEMENT_TEMPLATE = """
    Yield optimization strategies for {crop} in {location}:
    
    Cover these areas:
    1. Variety selection
    2. Planting techniques and timing
    3. Fertilization program
    4. Crop management practices
    5. Harvest timing and methods
    """
    
    WEATHER_PLANNING_TEMPLATE = """
    Weather-based farming advice for {climate} in {location}:
    
    Provide guidance on:
    1. Seasonal planning
    2. Weather risk mitigation
    3. Climate-appropriate practices
    4. Extreme weather preparedness
    5. Weather monitoring resources
    """
    
    GENERAL_ADVICE_TEMPLATE = """
    Comprehensive farming advice for:
    - Crop: {crop}
    - Location: {location}
    - Climate: {climate}
    - Soil: {soil_type}
    - Main Concern: {main_concern}
    
    Provide holistic farming guidance covering:
    1. Best practices for the specific context
    2. Resource management
    3. Economic considerations
    4. Available support systems
    5. Technology recommendations
    """
    
    def format_template(self, template_type: str, **kwargs) -> str:
        """Format a template with provided context"""
        templates = {
            'water': self.WATER_MANAGEMENT_TEMPLATE,
            'pest': self.PEST_DISEASE_TEMPLATE,
            'soil': self.SOIL_HEALTH_TEMPLATE,
            'yield': self.YIELD_IMPROVEMENT_TEMPLATE,
            'weather': self.WEATHER_PLANNING_TEMPLATE,
            'general': self.GENERAL_ADVICE_TEMPLATE
        }
        
        template = templates.get(template_type, self.GENERAL_ADVICE_TEMPLATE)
        return template.format(**kwargs)