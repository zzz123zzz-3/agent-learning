# agent-learning

从零开始学习 AI Agent 开发的完整记录 —— **先手写原理，再用框架**。

> 起点：2026.09.10 · 计算机大二 · 目标：12 周内掌握 Agent 开发核心能力并做出可展示的项目

## 学习路线与进度

| 周 | 主题 | 状态 |
|---|---|---|
| W1 | 调通 LLM API + **手写 Agent Loop** + 手写 ReAct | 🚧 进行中 |
| W2 | Tool Calling 原理、防死循环、上下文管理 | ⬜ |
| W3 | RAG：Embedding、向量检索、引用溯源 | ⬜ |
| W4 | 全离线 RAG 栈（ollama + Chroma + 本地 embedding） | ⬜ |
| W5-6 | LangGraph：State / 条件路由 / checkpoint / human-in-the-loop | ⬜ |
| W7 | MCP 协议 + 自写 MCP Server | ⬜ |
| W8 | 项目一：知识库问答（RAG）+ 评估集 + Langfuse tracing | ⬜ |
| W9-10 | 项目二：多 Agent 流水线（推荐 + 文案生成） | ⬜ |
| W11 | 前沿：A2A / Agent Skills / coding agent 架构拆解 | ⬜ |
| W12 | 简历与八股复盘 | ⬜ |

## 目录结构

```
day1/
├── 01_hello_api.py      # 最小 API 调用：跑通第一次握手
├── 02_agent_loop.py     # 手写 Agent Loop：模型决策 + 代码执行工具
└── 第一天任务清单.md
```

## 快速开始

```bash
# 1. 安装依赖
pip install openai

# 2. 配置 API Key（Windows PowerShell，永久生效）
setx DEEPSEEK_API_KEY "sk-你的key"     # 设置后需重开终端

# 3. 运行
python day1/01_hello_api.py            # 基础调用
python day1/02_agent_loop.py "北京天气怎么样"   # Agent Loop（支持传参）
```

**切换模型后端**：代码里 LLM 后端可插拔，改 `base_url` 即可切换——云端 API 与本地
ollama（`http://localhost:11434/v1`）共用同一套逻辑，弱网环境下也能开发调试。

## Day 1 · 手写 Agent Loop（2026.09.10）

### 实现内容

一个不依赖任何框架的最小 Agent：把两个工具（计算器、查天气）以 JSON Schema 的形式
"声明"给模型，然后在一个 `while` 循环里完成 **思考 → 调用工具 → 回填结果 → 再思考**，
直到模型不再请求工具为止。

```python
for turn in range(1, max_turns + 1):
    resp = client.chat.completions.create(model="deepseek-flash",
                                          messages=messages, tools=TOOLS)
    msg = resp.choices[0].message
    if msg.tool_calls:                    # 模型请求调用工具
        messages.append(msg)
        for tc in msg.tool_calls:         # 一次可能请求多个工具（并行调用）
            result = TOOL_FUNCS[tc.function.name](**json.loads(tc.function.arguments))
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})
    else:
        return msg.content                # 模型给出最终答案，循环结束
```

### 实测观察

| 提问 | 工具调用次数 | 说明 |
|---|---|---|
| "123*456 等于多少，北京天气怎么样" | **2 次（同一轮内并行）** | 模型在一次响应里同时请求了两个工具 |
| "上海天气怎么样" | 1 次 | 只调天气工具 |
| "给我讲个笑话" | **0 次** | 模型自主判断不需要工具 |

### 关键认知

1. **控制权发生了转移**：代码里没有任何一行 `if 用户问天气 then 调天气工具`。
   该不该调、调哪个、传什么参数，全部由模型决定——代码退化为"执行器 + 循环"。
2. **工具给事实，模型给推理**：工具只返回 `晴，22°C，北风 2 级` 一行字，
   而"22 度穿短袖是否合适"的分层建议完全是模型自己推理生成的。
3. **模型只输出"调用意图"**，真正执行工具的是我们的代码 —— 这条边界就是
   Agent 的安全边界（可在执行前加参数校验与权限控制）。
4. **`description` 就是新的代码**：模型靠工具描述来决定用哪个工具，描述写得含糊就会选错。

## 环境

- Python 3.13
- openai SDK 2.44（OpenAI 兼容格式）
- 模型：DeepSeek `deepseek-flash`（云端）/ `qwen3:8b`（本地 ollama 离线）
- 硬件：RTX 5060 Laptop 8GB / 16GB RAM
