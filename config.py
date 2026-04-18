"""
碳排放核算系统配置文件
GB/T 32151.24-2024 电子设备制造企业温室气体排放核算
"""
import os

# 应用信息
APP_TITLE = "电子设备制造企业碳排放核算系统"
APP_ICON = "🏭"

# DeepSeek API配置（部署时通过环境变量设置）
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"

# AI助手名称
AI_ASSISTANT_NAME = "克里斯汀娜"

# GWP值（基于IPCC AR6）
GWP_VALUES = {
    "NF3": 17900,   # 三氟化氮
    "SF6": 25200,   # 六氟化硫
    "CF4": 7380,    # 四氟化碳
    "C2F6": 12200,  # 六氟乙烷
    "C3F8": 9500,   # 八氟丙烷
}

# 电网排放因子（2024年全国电力平均碳足迹因子）
GRID_EMISSION_FACTOR = 0.5777  # tCO2/MWh

# 燃料排放因子默认值
DEFAULT_FUEL_FACTORS = {
    "天然气": {"ncv": 38931, "ef": 2.1622, "unit": "MJ/m³"},
    "柴油": {"ncv": 42652, "ef": 2.9251, "unit": "MJ/kg"},
    "汽油": {"ncv": 43070, "ef": 2.9251, "unit": "MJ/kg"},
    "液化石油气": {"ncv": 50179, "ef": 2.9848, "unit": "MJ/kg"},
    "煤油": {"ncv": 43070, "ef": 2.9251, "unit": "MJ/kg"},
    "燃料油": {"ncv": 41816, "ef": 3.1705, "unit": "MJ/kg"},
}

# 热力排放因子
HEAT_EMISSION_FACTOR = 0.11  # tCO2/GJ

# 应用配置
APP_CONFIG = {
    "title": APP_TITLE,
    "icon": APP_ICON,
    "layout": "wide",
    "gwp_values": GWP_VALUES,
    "grid_emission_factor": GRID_EMISSION_FACTOR,
    "fuel_factors": DEFAULT_FUEL_FACTORS,
    "heat_emission_factor": HEAT_EMISSION_FACTOR,
    "ai_name": AI_ASSISTANT_NAME,
}
