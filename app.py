"""
电子设备制造企业碳排放核算系统
基于 GB/T 32151.24-2024 标准
"""
import streamlit as st
from config import APP_TITLE, APP_ICON, APP_CONFIG

# 页面配置
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #4A90D9 0%, #67B8E3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #64748B;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .feature-card:hover {
        transform: translateY(-2px);
    }
    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        border-left: 4px solid #4A90D9;
    }
</style>
""", unsafe_allow_html=True)

# 主标题
st.markdown('<p class="main-header">🏭 电子设备制造企业碳排放核算系统</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">基于 GB/T 32151.24-2024 标准 | 科学核算 · 精准减排</p>', unsafe_allow_html=True)

# 核心公式展示
st.markdown("---")
st.markdown("### 📐 核算公式框架")
st.latex(r"E = E_{燃烧} + E_{过程} + E_{购入电} + E_{购入热} - E_{输出电} - E_{输出热}")

st.markdown("""
<div style="background: #F1F5F9; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
    <b>公式说明：</b><br>
    • <b>E<sub>燃烧</sub></b>：化石燃料燃烧产生的直接排放<br>
    • <b>E<sub>过程</sub></b>：工艺过程排放（含氟气体等）<br>
    • <b>E<sub>购入电</sub></b>：外购电力间接排放<br>
    • <b>E<sub>购入热</sub></b>：外购热力间接排放<br>
    • <b>E<sub>输出电</sub></b>、<b>E<sub>输出热</sub></b>：输出能源的减排量
</div>
""", unsafe_allow_html=True)

# 功能模块介绍
st.markdown("---")
st.markdown("### 🎯 系统功能模块")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>📊 工艺流程可视化</h4>
        <p>展示电子设备制造（半导体）全流程，包括主要设备设施、能源和资源消耗信息</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h4>⚡ 能流图分析</h4>
        <p>使用Plotly创建交互式Sankey能流图，清晰展示能源输入、转换、输出全流程</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🧮 碳排放计算器</h4>
        <p>支持参数调节自动核算，严格遵循GB/T 32151.24-2024标准计算公式</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h4>🤖 AI助手</h4>
        <p>集成DeepSeek API，AI助手"克里斯汀娜"专业解答碳排放核算问题</p>
    </div>
    """, unsafe_allow_html=True)

# 快速数据展示
st.markdown("---")
st.markdown("### 📈 关键排放因子")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="电网排放因子",
        value="0.5777 tCO₂/MWh",
        delta="2024年全国平均"
    )

with col2:
    st.metric(
        label="SF₆ GWP值",
        value="25,200",
        delta="IPCC AR6"
    )

with col3:
    st.metric(
        label="NF₃ GWP值",
        value="17,900",
        delta="IPCC AR6"
    )

# 页脚
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94A3B8; padding: 1rem;">
    <small>GB/T 32151.24-2024 温室气体排放核算与报告要求 第24部分：电子设备制造企业</small>
</div>
""", unsafe_allow_html=True)
