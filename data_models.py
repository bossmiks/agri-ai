"""
Data models for agriculture context and responses
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FarmingContext:
    """Represents the farming context provided by user"""
    crop: str
    location: str
    climate: str
    soil_type: str
    main_concern: str

@dataclass
class AgricultureAdvice:
    """Represents advice response from the AI system"""
    title: str
    recommendations: List[str]
    additional_tips: List[str] = None
    warnings: List[str] = None

class PhilippinesAgriData:
    """Static data about Philippine agriculture"""
    
    COMMON_CROPS = {
        "rice": {
            "seasons": ["wet", "dry"],
            "regions": ["central_luzon", "cagayan_valley", "ilocos"],
            "soil_preference": ["clay", "loamy"]
        },
        "corn": {
            "seasons": ["dry", "wet"],
            "regions": ["mindanao", "northern_luzon"],
            "soil_preference": ["sandy_loam", "loamy"]
        },
        "banana": {
            "seasons": ["year_round"],
            "regions": ["mindanao", "southern_luzon"],
            "soil_preference": ["sandy_loam", "loamy"]
        },
        "coconut": {
            "seasons": ["year_round"],
            "regions": ["bicol", "eastern_visayas", "mindanao"],
            "soil_preference": ["sandy", "sandy_loam"]
        }
    }
    
    PEST_DISEASES = {
        "rice": ["brown_planthopper", "stem_borer", "blast_disease"],
        "corn": ["corn_borer", "fall_armyworm", "downy_mildew"],
        "banana": ["bunchy_top_virus", "panama_disease", "banana_weevil"],
        "coconut": ["rhinoceros_beetle", "red_palm_weevil", "bud_rot"]
    }
    
    CLIMATE_PATTERNS = {
        "wet_season": {"months": ["June", "July", "August", "September", "October"]},
        "dry_season": {"months": ["November", "December", "January", "February", "March", "April", "May"]},
        "monsoon": {"months": ["June", "July", "August", "September"]}
    }