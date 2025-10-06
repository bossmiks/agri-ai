"""
Data models for Philippine agriculture context
"""

from dataclasses import dataclass
from typing import List, Dict

@dataclass
class PhilippineCrop:
    """Philippine crop information"""
    name: str
    local_name: str
    regions: List[str]
    seasons: List[str]
    varieties: List[str]

class PhilippinesAgriData:
    """Philippine agriculture data and knowledge base"""
    
    MAJOR_CROPS = {
        "rice": PhilippineCrop(
            name="Rice",
            local_name="Palay",
            regions=["Central Luzon", "Cagayan Valley", "Ilocos", "Bicol"],
            seasons=["Wet season", "Dry season"],
            varieties=["PSB Rc82", "NSIC Rc222", "NSIC Rc216", "PSB Rc18"]
        ),
        "corn": PhilippineCrop(
            name="Corn", 
            local_name="Mais",
            regions=["Northern Mindanao", "SOCCSKSARGEN", "Cagayan Valley"],
            seasons=["Wet season", "Dry season"],
            varieties=["Pioneer", "Dekalb", "NK", "Local varieties"]
        ),
        "banana": PhilippineCrop(
            name="Banana",
            local_name="Saging", 
            regions=["Davao", "Northern Mindanao", "SOCCSKSARGEN"],
            seasons=["Year-round"],
            varieties=["Cavendish", "Lakatan", "Latundan", "Saba"]
        )
    }
    
    REGIONS = {
        "luzon": ["Central Luzon", "Cagayan Valley", "Ilocos", "CALABARZON", "Bicol"],
        "visayas": ["Western Visayas", "Central Visayas", "Eastern Visayas"],
        "mindanao": ["Northern Mindanao", "Davao", "SOCCSKSARGEN", "CARAGA", "ARMM"]
    }
    
    COMMON_PESTS = {
        "rice": ["Brown Planthopper", "Stem Borer", "Rice Bug", "Golden Apple Snail"],
        "corn": ["Fall Armyworm", "Corn Borer", "Cutworm", "Corn Earworm"],
        "banana": ["Banana Weevil", "Nematodes", "Thrips", "Aphids"]
    }
    
    DISEASES = {
        "rice": ["Rice Blast", "Bacterial Leaf Blight", "Sheath Blight", "Tungro"],
        "corn": ["Downy Mildew", "Corn Rust", "Ear Rot", "Stalk Rot"],
        "banana": ["Panama Disease", "Black Sigatoka", "Bunchy Top", "Bacterial Wilt"]
    }