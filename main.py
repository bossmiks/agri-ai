#!/usr/bin/env python3
"""
Agri-AI: Agriculture Assistant for Philippines
Main application entry point
"""

from agriculture_assistant import AgricultureAssistant
from data_models import FarmingContext
import json

def main():
    assistant = AgricultureAssistant()
    
    print("🌾 Welcome to Agri-AI - Your Agriculture Assistant for the Philippines! 🌾")
    print("=" * 60)
    
    # Get user input
    context = get_farming_context()
    
    # Generate response
    response = assistant.get_advice(context)
    
    # Display response
    print("\n📋 RECOMMENDATIONS:")
    print("=" * 40)
    print(response)

def get_farming_context():
    """Collect farming context from user"""
    print("\nPlease provide your farming details:")
    
    # Crop selection
    crops = ["Rice", "Corn", "Banana", "Coconut", "Sugarcane", "Vegetables", "Other"]
    print(f"\n1. Crop Type: {', '.join(crops)}")
    crop = input("Enter your crop: ").strip()
    
    # Location
    print("\n2. Location (e.g., Central Luzon, Mindanao, Visayas)")
    location = input("Enter your location: ").strip()
    
    # Climate
    climates = ["Dry season", "Wet season", "Monsoon", "Year-round"]
    print(f"\n3. Climate: {', '.join(climates)}")
    climate = input("Enter current climate: ").strip()
    
    # Soil type
    soils = ["Sandy loam", "Clay", "Loamy", "Sandy", "Silt"]
    print(f"\n4. Soil Type: {', '.join(soils)}")
    soil = input("Enter soil type: ").strip()
    
    # Issues
    issues = ["Water Management", "Pest Control", "Disease Control", "Soil Health", "Yield Improvement", "Weather Planning"]
    print(f"\n5. Main Concern: {', '.join(issues)}")
    issue = input("Enter your main concern: ").strip()
    
    return FarmingContext(crop, location, climate, soil, issue)

if __name__ == "__main__":
    main()