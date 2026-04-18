"""
工艺流程可视化页面
展示电子设备制造（半导体）全流程
"""
import streamlit as st
import json
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="工艺流程可视化", page_icon="📊", layout="wide")

# 加载数据
@st.cache_data
def load_process_data():
    try:
        with open('data/process_flow.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

@st.cache_data
def load_equipment_data():
    try:
        with open('data/equipment_info.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

# 页面标题
st.title("📊 工艺流程可视化")
st.markdown("### 电子设备制造工艺流程概览")

process_data = load_process_data()
equipment_data = load_equipment_data()

if process_data:
    # 创建流程图
    stages = process_data.get('stages', [])
    
    fig = go.Figure()
    
    # 定义节点位置
    y_positions = list(range(len(stages), 0, -1))
    x_center = 0
    
    # 添加节点
    for i, stage in enumerate(stages):
        # 主节点
        fig.add_trace(go.Scatter(
            x=[x_center],
            y=[y_positions[i]],
            mode='markers+text',
            marker=dict(
                size=60,
                color='#4A90D9',
                line=dict(color='white', width=2)
            ),
            text=stage['name'],
            textposition='middle center',
            textfont=dict(size=14, color='white'),
            hovertemplate=f"<b>{stage['name']}</b><br>{stage['description']}<extra></extra>",
            showlegend=False
        ))
        
        # 添加箭头连接
        if i < len(stages) - 1:
            fig.add_annotation(
                x=x_center,
                y=y_positions[i+1] + 0.3,
                ax=x_center,
                ay=y_positions[i] - 0.3,
                arrowhead=2,
                arrowsize=1,
                arrowcolor='#94A3B8',
                showarrow=True
            )
    
    fig.update_layout(
        title=dict(text="半导体制造工艺流程", x=0.5, font=dict(size=20)),
        showlegend=False,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        height=600,
        paper_bgcolor='#F8FAFC',
        margin=dict(l=20, r=20, t=60, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # 详细信息展示
    st.markdown("---")
    st.markdown("### 各工艺阶段详情")
    
    for stage in stages:
        with st.expander(f"**{stage['id']}. {stage['name']}**", expanded=False):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**📝 工艺描述**")
                st.write(stage.get('description', '暂无描述'))
            
            with col2:
                st.markdown("**⚙️ 主要设备**")
                for equip in stage.get('equipment', []):
                    st.markdown(f"- {equip}")
            
            with col3:
                st.markdown("**⚡ 能源/资源消耗**")
                for energy in stage.get('energy', []):
                    st.markdown(f"- {energy}")
                
                st.markdown("**💨 排放类型**")
                for emission in stage.get('emissions', []):
                    st.markdown(f"- {emission}")

else:
    st.warning("未能加载工艺流程数据")

# 设备信息展示
if equipment_data:
    st.markdown("---")
    st.markdown("### 🔧 设备设施信息")
    
    categories = equipment_data.get('categories', [])
    
    for cat in categories:
        st.markdown(f"#### {cat.get('icon', '📌')} {cat['name']}")
        
        equipment_list = cat.get('equipment', [])
        cols = st.columns(min(len(equipment_list), 3))
        
        for idx, equip in enumerate(equipment_list):
            col_idx = idx % 3
            with cols[col_idx]:
                st.markdown(f"""
                <div style="background: #EEF2FF; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem;">
                    <b>{equip['name']}</b><br>
                    <small>功率: {equip.get('power', 'N/A')}</small><br>
                    <small>{equip.get('description', '')}</small>
                </div>
                """, unsafe_allow_html=True)
