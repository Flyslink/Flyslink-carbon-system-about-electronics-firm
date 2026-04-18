"""
AI助手模块
集成DeepSeek API提供专业问答
"""
import os
from openai import OpenAI

class AIAssistant:
    """AI助手类"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("DEEPSEEK_API_KEY", "")
        self.name = "克里斯汀娜"
        self.client = None
        
        if self.api_key:
            try:
                self.client = OpenAI(
                    api_key=self.api_key,
                    base_url="https://api.deepseek.com/v1"
                )
            except:
                self.client = None
    
    def is_available(self):
        """检查API是否可用"""
        return self.client is not None
    
    def chat(self, message, history=None):
        """
        与AI助手对话
        message: 用户消息
        history: 历史对话记录
        """
        if not self.is_available():
            return "抱歉，AI助手暂未配置API密钥。请在设置中配置DeepSeek API Key后重试。"
        
        system_prompt = f"""你是{self.name}，一位专业的碳排放核算助手。
你的专长是：
1. 解答GB/T 32151.24-2024《温室气体排放核算与报告要求 第24部分：电子设备制造企业》相关问题
2. 帮助用户理解碳排放核算方法和计算公式
3. 提供电子设备制造行业的碳排放数据和建议
4. 解释温室气体排放因子的含义和应用

请用专业、友好、简洁的方式回答问题。如果问题超出你的专业范围，请诚实告知。"""

        messages = [{"role": "system", "content": system_prompt}]
        
        if history:
            for h in history:
                messages.append({"role": h.get("role", "user"), "content": h.get("content", "")})
        
        messages.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                max_tokens=2000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"抱歉，AI助手遇到了一些问题：{str(e)}"
    
    def get_quick_questions(self):
        """获取快捷问题列表"""
        return [
            "什么是碳排放核算边界？",
            "如何计算工艺气体的过程排放？",
            "电子设备制造行业的主要排放源有哪些？",
            "GWP值是什么意思？如何使用？",
            "如何确定电力间接排放因子？",
            "碳排放核算报告应包含哪些内容？"
        ]
