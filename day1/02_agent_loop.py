# -*- coding: utf-8 -*-
"""
第一天 · 第 2 步：手写一个 AI Agent（Agent Loop）

Agent 的本质 = while 循环：
    模型想调工具 → 我们执行工具 → 结果塞回对话 → 模型再思考 → ... → 给出最终答案

运行：python 02_agent_loop.py
"""
import json
import os
from openai import OpenAI

API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    print("❌ 没找到 DEEPSEEK_API_KEY 环境变量")
    print('   PowerShell 里先运行:  $env:DEEPSEEK_API_KEY="sk-你的key"')
    raise SystemExit(1)

client = OpenAI(base_url="https://api.deepseek.com", api_key=API_KEY)


# ── 工具 1：计算器 ──────────────────────────────────────────────
# ⚠️ eval 只是为了教学方便，生产环境绝不能用（有代码注入风险）
def calc(expression: str) -> str:
    try:
        # 第二、三个参数禁掉内置函数，只留纯算术
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as e:
        return f"计算出错: {e}"


# ── 工具 2：查天气（假数据，先把流程跑通）───────────────────────
WEATHER_DB = {
    "北京": "晴，22°C，北风 2 级",
    "上海": "多云，26°C，东南风 3 级",
    "广州": "雷阵雨，30°C，湿度 85%",
}

def get_weather(city: str) -> str:
    return WEATHER_DB.get(city, f"没有 {city} 的数据（只有：{list(WEATHER_DB)}）")


# ── 把工具"声明"给模型（JSON Schema：告诉模型工具叫什么、参数长啥样）──
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calc",
            "description": "计算一个数学表达式",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "数学表达式，如 '3*4+2'"}
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询某个城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名，如 北京"}
                },
                "required": ["city"],
            },
        },
    },
]

TOOL_FUNCS = {"calc": calc, "get_weather": get_weather}


def agent(task: str, max_turns: int = 10) -> str:
    """核心：Agent Loop。模型不断思考→调工具→看结果，直到给出最终答案。"""
    messages = [
        {"role": "system", "content": "你是一个助手，会先用工具算/查，再回答用户。"},
        {"role": "user", "content": task},
    ]

    for turn in range(1, max_turns + 1):
        resp = client.chat.completions.create(
            model="deepseek-flash", messages=messages, tools=TOOLS
        )
        msg = resp.choices[0].message

        if msg.tool_calls:  # ← 模型想调工具（注意：模型只输出"调用意图"，真正执行的是你）
            messages.append(msg)  # 把这条"带工具请求"的消息放回上下文
            for tc in msg.tool_calls:
                name = tc.function.name
                args = json.loads(tc.function.arguments)
                print(f"  第{turn}轮 → 调用工具 {name}({args})")
                result = TOOL_FUNCS[name](**args)
                # 执行结果以 role="tool" 的消息回填，tool_call_id 必须对上
                messages.append(
                    {"role": "tool", "tool_call_id": tc.id, "content": result}
                )
        else:  # ← 模型觉得信息够了，输出最终答案
            return msg.content

    return "⚠️ 超过最大轮数，仍未完成任务（这就是 W2 要学的'防死循环'）"


if __name__ == "__main__":
    import sys
    # 支持两种用法：
    #   python 02_agent_loop.py                          → 用默认问题
    #   python 02_agent_loop.py "给我讲个笑话"            → 用你传的问题
    question = (
        sys.argv[1] if len(sys.argv) > 1
        else "帮我算一下 123*456 等于多少，顺便告诉我北京今天天气怎么样"
    )
    print("👤 问：", question)
    print("🤖 答：", agent(question))
