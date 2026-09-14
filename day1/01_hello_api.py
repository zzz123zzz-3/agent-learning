# -*- coding: utf-8 -*-
"""
第一天 · 第 1 步：跑通第一个 chat 调用

用法：
    1. 设置 API Key（PowerShell 里临时设置，关窗即失效）：
       $env:DEEPSEEK_API_KEY="sk-你的key"
       想永久保存：系统设置 → 环境变量 → 新建 DEEPSEEK_API_KEY
    2. 安装依赖：pip install openai
    3. 运行：python 01_hello_api.py
"""
import os
from openai import OpenAI

API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    print("❌ 没找到 DEEPSEEK_API_KEY 环境变量")
    print('   PowerShell 里先运行:  $env:DEEPSEEK_API_KEY="sk-你的key"')
    raise SystemExit(1)

# DeepSeek 用的是 OpenAI 兼容格式，所以直接用 openai 官方包，
# 只改 base_url 和 model 就能切到本地 ollama（后面弱网场景会用到）
client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=API_KEY,
)

resp = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个友好的助手，回答简短。"},
        {"role": "user", "content": "用一句话解释什么是 AI Agent"},
    ],
    temperature=0.7,   # 0=严谨, 1=发散；写代码/做题调 0.2，闲聊调 0.7+
)

print("🤖 回复：", resp.choices[0].message.content)
print("💰 本次消耗 token：", resp.usage.total_tokens)

# ── 顺手体验两个常用能力（把上面 create 调用换掉即可）────────────
# ① 流式输出（逐字蹦出来）：
#     resp = client.chat.completions.create(..., stream=True)
#     for chunk in resp:
#         print(chunk.choices[0].delta.content or "", end="")
# ② 多轮对话：把上一次的 messages 原样带上、append 新消息再调用即可
# ③ JSON 结构化输出：加 response_format={"type": "json_object"}
