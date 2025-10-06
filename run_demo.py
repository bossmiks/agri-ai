#!/usr/bin/env python3
"""
Demo script to showcase Agri-AI capabilities
"""

from agriculture_assistant import AgricultureAssistant
from data_models import FarmingContext

def run_demo():
    """Run demonstration of different farming scenarios"""
    assistant = AgricultureAssistant()
    
    print("🌾 AGRI-AI DEMONSTRATION")
    print("=" * 50)
    
    # Demo scenarios
    scenarios = [
        {
            "title": "Rice Farming - Water Management",
            "context": FarmingContext("Rice", "Central Luzon", "Wet season", "Clay", "Water Management")
        },
        {
            "title": "Corn Farming - Pest Control", 
            "context": FarmingContext("Corn", "Mindanao", "Dry season", "Sandy loam", "Pest Control")
        },
        {
            "title": "Banana Farming - Soil Health",
            "context": FarmingContext("Banana", "Southern Luzon", "Monsoon", "Sandy", "Soil Health")
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📋 DEMO {i}: {scenario['title']}")
        print("-" * 40)
        
        advice = assistant.get_advice(scenario['context'])
        print(advice)
        
        print("\n" + "="*50)
        
        if i < len(scenarios):
            input("Press Enter to continue to next demo...")

if __name__ == "__main__":
    run_demo()