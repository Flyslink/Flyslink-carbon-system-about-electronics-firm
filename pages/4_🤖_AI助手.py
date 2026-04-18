"""
AI助手页面
集成DeepSeek API的专业问答
"""
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ai_helper import AIAssistant
from config import AI_ASSISTANT_NAME

st.set_page_config(page_title="AI助手", page_icon="🤖", layout="wide")

st.title(f"🤖 AI助手：{AI_ASSISTANT_NAME}")
st.markdown("### 专业碳排放核算问答")

# 初始化AI助手
if 'ai_assistant' not in st.session_state:
    st.session_state['ai_assistant'] = AIAssistant()

assistant = st.session_state['ai_assistant']

# 检查API配置
if not assistant.is_available():
    st.warning("⚠️ AI助手暂未配置API密钥")
    
    with st.expander("配置说明"):
        st.markdown("""
        **如何配置DeepSeek API：**
        
        1. 访问 [DeepSeek官网](https://www.deepseek.com/) 注册账号
        2. 在API设置中获取API Key
        3. 在部署时设置环境变量 `DEEPSEEK_API_KEY`
        
        **本地运行时：**
        ```bash
        export DEEPSEEK_API_KEY="your-api-key"
        streamlit run app.py
        ```
        
        **Streamlit Cloud部署时：**
        在Settings → Secrets中添加：
        ```
        DEEPSEEK_API_KEY="your-api-key"
        ```
        """)
    
    # 手动输入API Key
    api_key_input = st.text_input("临时输入API Key", type="password")
    if api_key_input:
        st.session_state['ai_assistant'] = AIAssistant(api_key=api_key_input)
        assistant = st.session_state['ai_assistant']
        st.rerun()

else:
    st.success(f"✅ AI助手 {AI_ASSISTANT_NAME} 已就绪")
    
    # 初始化对话历史
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    
    # 快捷问题
    st.markdown("#### 💡 快捷问题")
    quick_questions = assistant.get_quick_questions()
    
    cols = st.columns(3)
    for idx, question in enumerate(quick_questions):
        with cols[idx % 3]:
            if st.button(question, key=f"quick_{idx}"):
                st.session_state['current_question'] = question
                st.rerun()
    
    # 对话区域
    st.markdown("---")
    st.markdown("#### 💬 对话区域")
    
    # 显示历史对话
    for msg in st.session_state['chat_history']:
        with st.chat_message(msg['role']):
            st.write(msg['content'])
    
    # 输入框
    user_input = st.chat_input("输入您的问题...")
    
    # 处理输入
    current_q = st.session_state.get('current_question', '')
    if user_input or current_q:
        question = user_input or current_q
        st.session_state['current_question'] = ''
        
        # 显示用户问题
        with st.chat_message("user"):
            st.write(question)
        
        # 获取AI回复
        with st.chat_message("assistant"):
            with st.spinner(f"{AI_ASSISTANT_NAME} 正在思考..."):
                response = assistant.chat(question, st.session_state['chat_history'])
                st.write(response)
        
        # 保存对话历史
        st.session_state['chat_history'].append({'role': 'user', 'content': question})
        st.session_state['chat_history'].append({'role': 'assistant', 'content': response})
        
        st.rerun()
    
    # 清空对话
    if st.button("清空对话历史"):
        st.session_state['chat_history'] = []
        st.rerun()
