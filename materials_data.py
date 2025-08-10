"""
Civil engineering materials density database
Densities are in kg/m³ at standard conditions
"""

import pandas as pd

# Material density data (kg/m³)
MATERIALS_DATA = {
    "콘크리트 (일반)": {"density": 2400, "category": "콘크리트"},
    "콘크리트 (고강도)": {"density": 2500, "category": "콘크리트"}, 
    "콘크리트 (경량)": {"density": 1800, "category": "콘크리트"},
    "철근콘크리트": {"density": 2500, "category": "콘크리트"},
    "아스팔트 콘크리트": {"density": 2350, "category": "아스팔트"},
    "구조용 강재": {"density": 7850, "category": "강재"},
    "철근": {"density": 7850, "category": "강재"},
    "강관": {"density": 7850, "category": "강재"},
    "자갈 (20-40mm)": {"density": 1600, "category": "골재"},
    "자갈 (40-80mm)": {"density": 1550, "category": "골재"},
    "모래 (세사)": {"density": 1600, "category": "골재"},
    "모래 (조사)": {"density": 1500, "category": "골재"},
    "쇄석 (10-20mm)": {"density": 1650, "category": "골재"},
    "쇄석 (20-40mm)": {"density": 1600, "category": "골재"},
    "시멘트": {"density": 1440, "category": "시멘트"},
    "석회": {"density": 1200, "category": "기타"},
    "석고": {"density": 1300, "category": "기타"},
    "점토": {"density": 1900, "category": "흙"},
    "사질토": {"density": 1700, "category": "흙"},
    "실트": {"density": 1500, "category": "흙"},
    "자연석 (화강암)": {"density": 2650, "category": "석재"},
    "자연석 (사암)": {"density": 2200, "category": "석재"},
    "벽돌": {"density": 1800, "category": "벽돌"},
    "블록 (콘크리트)": {"density": 2000, "category": "블록"},
    "목재 (침엽수)": {"density": 500, "category": "목재"},
    "목재 (활엽수)": {"density": 700, "category": "목재"},
    "물": {"density": 1000, "category": "기타"},
}

def get_materials_df():
    """Convert materials data to pandas DataFrame"""
    data = []
    for material, info in MATERIALS_DATA.items():
        data.append({
            "재료명": material,
            "밀도 (kg/m³)": info["density"],
            "분류": info["category"]
        })
    return pd.DataFrame(data)

def get_material_density(material_name):
    """Get density for a specific material"""
    return MATERIALS_DATA.get(material_name, {}).get("density", 0)

def get_materials_by_category():
    """Group materials by category"""
    categories = {}
    for material, info in MATERIALS_DATA.items():
        category = info["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(material)
    return categories
