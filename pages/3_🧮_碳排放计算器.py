"""
碳排放计算器页面
基于GB/T 32151.24-2024标准的碳排放核算
"""
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.calculator import CarbonCalculator

st.set_page_config(page_title="碳排放计算器", page_icon="🧮", layout="wide")

st.title("🧮 碳排放计算器")
st.markdown("### 基于 GB/T 32151.24-2024 标准")

# 初始化计算器
calculator = CarbonCalculator()

# 创建标签页
tab1, tab2, tab3, tab4 = st.tabs([
    "🔥 燃烧排放", "💨 过程排放", "⚡ 间接排放", "📊 综合核算"
])

# 燃烧排放计算
with tab1:
    st.markdown("#### 化石燃料燃烧排放计算")
    st.markdown("公式：**E = AD × NCV × EF**")
    
    # 燃料类型列表
    fuel_types = ["天然气", "柴油", "汽油", "液化石油气", "煤油", "燃料油"]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fuel_type = st.selectbox("燃料类型", fuel_types, key="fuel_type")
    
    with col2:
        consumption = st.number_input("消耗量", min_value=0.0, value=1000.0, step=100.0)
    
    with col3:
        unit = st.selectbox("单位", ["kg", "m³", "吨"], key="fuel_unit")
    
    if st.button("计算燃烧排放", key="calc_combustion"):
        result = calculator.calc_combustion_emission(fuel_type, consumption, unit)
        
        st.success(f"燃烧排放量：**{result['emission']} tCO₂**")
        
        with st.expander("查看计算详情"):
            st.markdown(f"""
            **计算过程：**
            - 燃料类型：{fuel_type}
            - 消耗量：{consumption} {unit}
            - 低位发热量（NCV）：{result['ncv']} MJ/{unit}
            - 排放因子（EF）：{result['ef']} kgCO₂/MJ
            - **{result['formula']}**
            """)
        
        # 存储结果
        st.session_state['combustion_result'] = result['emission']

# 过程排放计算
with tab2:
    st.markdown("#### 工艺过程排放计算")
    st.markdown("公式：**E = (消耗量 - 处理量) × GWP**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gas_type = st.selectbox("工艺气体类型", ["NF3", "SF6", "CF4", "C2F6", "C3F8"], key="gas_type")
    
    with col2:
        gas_consumption = st.number_input("消耗量 (kg)", min_value=0.0, value=100.0, step=10.0, key="gas_consumption")
    
    with col3:
        abatement = st.slider("尾气处理效率", 0, 100, 90) / 100
    
    if st.button("计算过程排放", key="calc_process"):
        result = calculator.calc_process_emission(gas_type, gas_consumption, abatement)
        
        st.success(f"过程排放量：**{result['emission']} tCO₂eq**")
        
        with st.expander("查看计算详情"):
            st.markdown(f"""
            **计算过程：**
            - 气体类型：{gas_type}
            - 消耗量：{gas_consumption} kg
            - GWP值：{result['gwp']}
            - 尾气处理效率：{result['abatement']}%
            - **{result['formula']}**
            """)
        
        st.session_state['process_result'] = result['emission']

# 间接排放计算
with tab3:
    st.markdown("#### 电力与热力间接排放计算")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**电力间接排放**")
        electricity = st.number_input("电力消耗 (MWh)", min_value=0.0, value=1000.0, step=100.0)
        
        if st.button("计算电力排放", key="calc_elec"):
            result = calculator.calc_electricity_emission(electricity)
            st.success(f"电力间接排放：**{result['emission']} tCO₂**")
            st.markdown(f"公式：{result['formula']}")
            st.session_state['electricity_result'] = result['emission']
    
    with col2:
        st.markdown("**热力间接排放**")
        heat = st.number_input("热力消耗 (GJ)", min_value=0.0, value=500.0, step=50.0)
        
        if st.button("计算热力排放", key="calc_heat"):
            result = calculator.calc_heat_emission(heat)
            st.success(f"热力间接排放：**{result['emission']} tCO₂**")
            st.markdown(f"公式：{result['formula']}")
            st.session_state['heat_result'] = result['emission']

# 综合核算
with tab4:
    st.markdown("#### 总排放量综合核算")
    st.markdown("公式：**E = E燃烧 + E过程 + E购入电 + E购入热 - E输出电 - E输出热**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**排放量输入**")
        combustion_input = st.number_input("燃烧排放 (tCO₂)", min_value=0.0, value=st.session_state.get('combustion_result', 0.0))
        process_input = st.number_input("过程排放 (tCO₂eq)", min_value=0.0, value=st.session_state.get('process_result', 0.0))
        electricity_input = st.number_input("购入电力排放 (tCO₂)", min_value=0.0, value=st.session_state.get('electricity_result', 0.0))
        heat_input = st.number_input("购入热力排放 (tCO₂)", min_value=0.0, value=st.session_state.get('heat_result', 0.0))
    
    with col2:
        st.markdown("**减排量输入**")
        output_elec = st.number_input("输出电力减排 (tCO₂)", min_value=0.0, value=0.0)
        output_heat = st.number_input("输出热力减排 (tCO₂)", min_value=0.0, value=0.0)
    
    if st.button("计算总排放量", key="calc_total"):
        result = calculator.calc_total(
            combustion=combustion_input,
            process=process_input,
            electricity=electricity_input,
            heat=heat_input,
            output_elec=output_elec,
            output_heat=output_heat
        )
        
        st.markdown("---")
        st.markdown("### 📊 核算结果")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("燃烧排放", f"{result['combustion']} tCO₂")
        
        with col2:
            st.metric("过程排放", f"{result['process']} tCO₂eq")
        
        with col3:
            st.metric("间接排放", f"{result['electricity'] + result['heat']} tCO₂")
        
        with col4:
            st.metric("总排放量", f"{result['total']} tCO₂eq", delta="最终结果")
        
        st.info(f"**计算公式：** {result['formula']}")
