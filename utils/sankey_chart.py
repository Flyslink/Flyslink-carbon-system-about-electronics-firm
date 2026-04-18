"""
Sankey能流图生成模块
使用Plotly创建交互式能量流动图
"""
import plotly.graph_objects as go

def create_sankey_chart():
    """创建电子设备制造企业能源流动Sankey图"""
    
    # 定义节点
    labels = [
        # 源头能源 (0-5)
        "外购电力", "天然气", "柴油", "工艺气体", "外购热力",
        # 中间转换 (5-8)
        "动力设备", "热处理设备", "工艺设备",
        # 终端用能 (8-15)
        "照明", "空调", "生产设备", "刻蚀工艺", "薄膜工艺", 
        "清洗工艺", "检验测试", "其他辅助",
        # 排放 (15-18)
        "CO₂排放", "外供电力", "外供热力"
    ]
    
    # 定义颜色
    colors = [
        "#4A90D9", "#4A90D9", "#4A90D9", "#FF6B6B", "#4A90D9",  # 源头
        "#6C8EBF", "#6C8EBF", "#6C8EBF",  # 中间
        "#95A5A6", "#95A5A6", "#95A5A6", "#E74C3C", "#E74C3C", "#E74C3C", "#95A5A6", "#95A5A6",  # 终端
        "#2C3E50", "#27AE60", "#F39C12"  # 输出
    ]
    
    # 定义流向
    source = [
        # 外购电力流向
        0, 0, 0, 0, 0,
        # 天然气流向
        1, 1,
        # 柴油流向
        2,
        # 工艺气体流向
        3, 3,
        # 外购热力流向
        4,
        # 中间转换流向
        5, 5, 5, 
        6, 6,
        7, 7, 7,
        # 终端流向排放
        8, 9, 10, 11, 12, 13, 14, 15
    ]
    
    target = [
        # 外购电力到中间
        5, 6, 7, 8, 9,
        # 天然气到中间
        6, 10,
        # 柴油
        5,
        # 工艺气体到终端
        11, 12,
        # 外购热力
        10,
        # 中间到终端
        8, 9, 10,
        10, 13,
        11, 12, 14,
        # 终端到排放
        15, 15, 15, 15, 15, 15, 15, 15
    ]
    
    value = [
        # 外购电力
        3000, 1500, 2000, 200, 800,
        # 天然气
        1000, 500,
        # 柴油
        200,
        # 工艺气体
        50, 30,
        # 外购热力
        300,
        # 中间到终端
        200, 800, 2000,
        1200, 300,
        50, 30, 100,
        # 终端到排放
        150, 600, 1500, 800, 500, 200, 80, 100
    ]
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=1),
            label=labels,
            color=colors,
            hovertemplate='%{label}<br>流量: %{value:.0f} MWh<extra></extra>'
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color="rgba(148, 163, 184, 0.3)",
            hovertemplate='%{source.label} → %{target.label}<br>流量: %{value:.0f} MWh<extra></extra>'
        )
    )])
    
    fig.update_layout(
        title=dict(
            text="电子设备制造企业能源流动图",
            font=dict(size=20, color="#1E293B"),
            x=0.5
        ),
        font=dict(size=12, family="sans-serif"),
        paper_bgcolor="#F8FAFC",
        height=600,
        margin=dict(l=10, r=10, t=60, b=10)
    )
    
    return fig


def create_emission_sankey():
    """创建碳排放流向Sankey图"""
    
    labels = [
        "燃烧排放", "过程排放", "电力间接排放", "热力间接排放",
        "CO₂当量", "减排量", "净排放量"
    ]
    
    colors = [
        "#E74C3C", "#E74C3C", "#3498DB", "#F39C12",
        "#2C3E50", "#27AE60", "#C0392B"
    ]
    
    source = [0, 1, 2, 3, 4, 5]
    target = [4, 4, 4, 4, 6, 6]
    value = [500, 1200, 3000, 300, 5000, 800]
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=20,
            thickness=25,
            line=dict(color="white", width=1),
            label=labels,
            color=colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color="rgba(148, 163, 184, 0.3)"
        )
    )])
    
    fig.update_layout(
        title="碳排放流向分析",
        height=400,
        paper_bgcolor="#F8FAFC"
    )
    
    return fig
