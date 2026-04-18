"""
碳排放计算器模块
基于 GB/T 32151.24-2024 标准
"""
import json
import os

class CarbonCalculator:
    """碳排放计算器"""
    
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'emission_factors.json')
        self.load_data()
    
    def load_data(self):
        """加载排放因子数据"""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.gwp_values = data.get('gwp_values', {})
            self.fuel_factors = data.get('fuel_factors', {})
            self.grid_factor = data.get('grid_emission_factor', {}).get('value', 0.5777)
            self.heat_factor = data.get('heat_emission_factor', {}).get('value', 0.11)
        except:
            # 默认值
            self.gwp_values = {
                "NF3": {"gwp": 17900},
                "SF6": {"gwp": 25200},
                "CF4": {"gwp": 7380}
            }
            self.fuel_factors = {
                "天然气": {"ncv": 38931, "ef": 2.1622},
                "柴油": {"ncv": 42652, "ef": 2.9251}
            }
            self.grid_factor = 0.5777
            self.heat_factor = 0.11
    
    def calc_combustion_emission(self, fuel_type, consumption, unit='kg'):
        """
        计算燃烧排放
        fuel_type: 燃料类型
        consumption: 消耗量
        unit: 单位 (kg 或 m³)
        """
        # 兼容中文和英文字段名
        fuel_data = self.fuel_factors.get(fuel_type, {})
        ncv = fuel_data.get('ncv') or fuel_data.get('低位发热量', 40000)
        ef = fuel_data.get('ef') or fuel_data.get('排放因子', 2.5)
        
        # 计算排放量: E = AD × NCV × EF
        # AD: 活动数据（消耗量）
        # NCV: 低位发热量 (MJ/kg 或 MJ/m³)
        # EF: 排放因子 (kgCO2/MJ)
        emission = consumption * ncv * ef / 1000  # 转换为 tCO2
        
        return {
            'emission': round(emission, 4),
            'ncv': ncv,
            'ef': ef,
            'formula': f'E = {consumption} × {ncv} × {ef} / 1000 = {round(emission, 4)} tCO2'
        }
    
    def calc_process_emission(self, gas_type, consumption, abatement_rate=0):
        """
        计算过程排放
        gas_type: 工艺气体类型 (NF3, SF6, CF4 等)
        consumption: 消耗量 (kg)
        abatement_rate: 尾气处理效率 (0-1)
        """
        gas_data = self.gwp_values.get(gas_type, {})
        gwp = gas_data.get('gwp') or gas_data.get('GWP', 10000)
        
        # 计算排放量: E = (消耗量 - 处理量) × GWP
        net_emission = consumption * (1 - abatement_rate)
        emission = net_emission * gwp / 1000  # 转换为 tCO2eq
        
        return {
            'emission': round(emission, 4),
            'gwp': gwp,
            'abatement': abatement_rate * 100,
            'formula': f'E = {consumption} × (1 - {abatement_rate}) × {gwp} / 1000 = {round(emission, 4)} tCO2eq'
        }
    
    def calc_electricity_emission(self, consumption):
        """
        计算电力间接排放
        consumption: 电力消耗量 (MWh)
        """
        emission = consumption * self.grid_factor
        
        return {
            'emission': round(emission, 4),
            'factor': self.grid_factor,
            'formula': f'E = {consumption} × {self.grid_factor} = {round(emission, 4)} tCO2'
        }
    
    def calc_heat_emission(self, consumption):
        """
        计算热力间接排放
        consumption: 热力消耗量 (GJ)
        """
        emission = consumption * self.heat_factor
        
        return {
            'emission': round(emission, 4),
            'factor': self.heat_factor,
            'formula': f'E = {consumption} × {self.heat_factor} = {round(emission, 4)} tCO2'
        }
    
    def calc_total(self, combustion=0, process=0, electricity=0, heat=0, 
                   output_elec=0, output_heat=0):
        """
        计算总排放量
        E = E燃烧 + E过程 + E购入电 + E购入热 - E输出电 - E输出热
        """
        total = combustion + process + electricity + heat - output_elec - output_heat
        
        return {
            'combustion': combustion,
            'process': process,
            'electricity': electricity,
            'heat': heat,
            'output_elec': output_elec,
            'output_heat': output_heat,
            'total': round(total, 4),
            'formula': f'E = {combustion} + {process} + {electricity} + {heat} - {output_elec} - {output_heat} = {round(total, 4)} tCO2eq'
        }
