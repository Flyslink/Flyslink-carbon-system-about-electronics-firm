# 电子设备制造企业碳排放核算系统

基于 GB/T 32151.24-2024《温室气体排放核算与报告要求 第24部分：电子设备制造企业》标准开发的碳排放核算系统。

## 功能模块

1. **工艺流程可视化** - 展示电子设备制造（半导体）全流程
2. **Sankey能流图分析** - 交互式能量流动可视化
3. **碳排放计算器** - 基于标准的自动核算
4. **AI助手"克里斯汀娜"** - 专业碳排放问答

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 运行应用
streamlit run app.py
```

## 部署到 Streamlit Cloud

### 步骤1：创建GitHub仓库

1. 登录 GitHub
2. 创建新仓库（如 `carbon-emission-calculator`）
3. 上传整个项目文件夹

### 步骤2：部署到Streamlit Cloud

1. 访问 [share.streamlit.io](https://share.streamlit.io)
2. 使用GitHub账号登录
3. 点击 "New app"
4. 选择你的仓库
5. Main file path 填写 `app.py`
6. 点击 "Deploy!"

### 步骤3：配置API Key（可选）

如需使用AI助手功能：

1. 在Streamlit Cloud应用页面点击 "Settings"
2. 选择 "Secrets"
3. 添加以下内容：
```toml
DEEPSEEK_API_KEY = "your-api-key-here"
```
4. 保存并重新部署

## 项目结构

```
碳排放核算系统-部署版/
├── app.py                    # 主入口
├── config.py                 # 配置文件
├── requirements.txt          # 依赖清单
├── .streamlit/
│   └── config.toml          # Streamlit配置
├── data/
│   ├── emission_factors.json # 排放因子数据
│   ├── process_flow.json     # 工艺流程数据
│   └── equipment_info.json   # 设备信息数据
├── pages/
│   ├── 1_📊_工艺流程可视化.py
│   ├── 2_⚡_能流图分析.py
│   ├── 3_🧮_碳排放计算器.py
│   └── 4_🤖_AI助手.py
└── utils/
    ├── __init__.py
    ├── calculator.py         # 碳排放计算逻辑
    ├── sankey_chart.py       # Sankey图生成
    └── ai_helper.py          # AI助手模块
```

## 核心公式

根据GB/T 32151.24-2024标准：

$$E = E_{燃烧} + E_{过程} + E_{购入电} + E_{购入热} - E_{输出电} - E_{输出热}$$

## 关键参数

| 参数 | 值 | 来源 |
|------|-----|------|
| NF₃ GWP | 17,900 | IPCC AR6 |
| SF₆ GWP | 25,200 | IPCC AR6 |
| CF₄ GWP | 7,380 | IPCC AR6 |
| 电网排放因子 | 0.5777 tCO₂/MWh | 2024年全国平均 |

## 技术栈

- Python 3.8+
- Streamlit
- Plotly
- DeepSeek API

## 许可证

MIT License
