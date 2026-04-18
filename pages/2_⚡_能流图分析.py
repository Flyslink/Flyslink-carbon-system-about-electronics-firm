"""
Sankey能流图分析页面
使用Plotly创建交互式能量流动图
"""
import streamlit as st
import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.sankey_chart import create_sankey_chart, create_emission_sankey

st.set_page_config(page_title="能流图分析", page_icon="⚡", layout="wide")

st.title("⚡ 能流图分析")
st.markdown("### 电子设备制造企业能源流动可视化")

# 创建标签页
tab1, tab2 = st.tabs(["能源流动图", "碳排放流向图"])

with tab1:
    st.markdown("""
    **能源流动说明：**
    - 左侧为能源输入端，包括外购电力、天然气、柴油、工艺气体、外购热力
    - 中间为能源转换环节
    - 右侧为终端用能环节和排放输出
    """)
    
    fig = create_sankey_chart()
    st.plotly_chart(fig, use_container_width=True)
    
    # 能源流向解读
    st.markdown("---")
    st.markdown("### 📊 能源流向分析")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="外购电力占比",
            value="65%",
            delta="主要能源来源"
        )
    
    with col2:
        st.metric(
            label="工艺设备能耗",
            value="2,000 MWh",
            delta="最大用能环节"
        )
    
    with col3:
        st.metric(
            label="CO₂排放量",
            value="3,500 tCO₂",
            delta="核算结果"
        )

with tab2:
    st.markdown("""
    **碳排放流向说明：**
    - 展示各类排放源对总排放的贡献
    - 减排量从总排放中扣除
    - 最终得到净排放量
    """)
    
    fig2 = create_emission_sankey()
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📈 排放结构分析")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="燃烧排放", value="500 tCO₂")
    
    with col2:
        st.metric(label="过程排放", value="1,200 tCO₂eq")
    
    with col3:
        st.metric(label="电力间接排放", value="3,000 tCO₂")
    
    with col4:
        st.metric(label="净排放量", value="4,200 tCO₂eq")
