# Agent 学习与实习方案 v3（终版 · 2026.09 → 12月）

> 个人画像：计算机大二上（2026.09.10 起步）、双非本科、就业导向（大二/大三实习 → 大四中大厂校招）、坐标北京、每天可投入 3-4 小时、API 预算 100 元/月、无职转生爱好者。
> 本方案由 12 条共识（grilling 会话产出）定制而成，非通用模板。

---

## 0. 十二项共识（决策记录，已确认）

1. **终点**：就业导向。大二/大三实习 → 大四中大厂校招，不读研。
2. **时间**：每天 3-4 小时，双轨制——教学楼弱网做离线任务，宿舍做在线任务（见第 2 节）。
3. **API**：预算 100 元/月。DeepSeek flash 主力 + Gemini/智谱免费层；无外币卡，OpenAI/Claude 网页版白嫖，2027 年前不碰中转站/虚拟卡（除非后期做英文前沿实验再议）。
4. **简历补强**：不进实验室 → 博客每两周一篇 + 开源 PR（11 月底前合并第一个）+ 比赛随缘。
5. **硬件**：RTX 5060 Laptop（8GB 显存）+ 16GB 内存 + 200GB 磁盘 → ollama 跑 `qwen3:8b`（Q4）做离线兜底。
6. **项目一**：无职转生 RAG 知识库问答（语料：萌娘百科/维基/Bangumi）。
7. **项目二**：多 Agent 流水线——追番推荐 + 安利文案生成（同样绑二次元主题）。
8. **算法**：零基础起步，代码随想录免费专题 + LeetCode 简单题每天 1-2 题（30-45 分钟），周日复盘，跟数据结构课同步。
9. **富余时间**：每周一拆（拆解清单见第 7 节），拆解笔记发博客。
10. **实习**：北京、公司类型不限、每周到岗 3 天+；12 月试投 = 创业公司/中小厂为主 + 大厂 2-3 家练手 + 远程兜底。
11. **课程边界**：平时自学优先，考前 1-2 周课程让路，GPA 保底线 80 分/3.0。
12. **里程碑**：12 月前完成 2 个硬核项目 + 第一个开源 PR + 简历 v1 试投。

---

## 1. 五条学习铁律

1. **先手写原理，再用框架**。ReAct、function calling、RAG 的原理不变，框架半年一换代；面试只考原理。
2. **每周有可跑产出，push 到 GitHub**。12 周 = 12 个 commit 周。
3. **项目驱动，不囤课**。看完 1 门课 + 官方文档，剩下全部写代码。写一个烂项目 > 看十个好教程。
4. **AI 当陪练**：卡住 30 分钟就问 ChatGPT/Claude/Cursor（弱网时问本地 qwen）；但每个解决过的问题必须能向别人讲清楚"为什么"。
5. **拆解防囤积**：想"多了解项目"就按"每周一拆"结构化执行，禁止泛泛浏览。

---

## 2. 双轨制：教学楼弱网 vs 宿舍在线

核心：任务切成"离线可做"和"必须在线"，教学楼只做离线类。

**离线任务（教学楼）**：
- 本地模型调试 agent：代码把 LLM 后端写成可插拔（`base_url` 切换 DeepSeek API ↔ 本地 ollama `qwen3:8b`），网再差也能跑
- 读源码：smolagents、langgraph 等仓库 clone 到本地断网读
- 写代码：工具定义、prompt 模板、解析逻辑、单元测试，全都不需要网
- 全离线 RAG：Chroma 本地库 + bge-m3 本地 embedding + 本地 LLM，语料提前爬好
- 纯脑力活：背八股、写博客草稿（Obsidian 离线）、整理笔记、读论文 PDF
- 提前缓存：官方文档仓库 git clone 本地看、课程笔记、PDF 下好

**在线任务（宿舍）**：API 调试、看视频课、爬取语料、推送 GitHub、发博客。

**一次性配置清单（本周末 2 小时搞定）**：装 ollama + 拉 `qwen3:8b` 和 bge-m3 → clone 4 个仓库（smolagents/langgraph/Dify/OpenHands）→ 镜像 2 个文档站 → 下 5 篇论文 PDF → 配好 `.env`。

---

## 3. 到 12 月的"前沿"清单（每月自查）

- [ ] 能用手写代码解释 ReAct 和 function calling 的完整原理
- [ ] 能用 LangGraph 搭生产级多步/多 Agent 工作流（State、条件路由、checkpoint、human-in-the-loop）
- [ ] 写过自己的 MCP Server，了解 MCP 生态（registry、鉴权、stateless 趋势）
- [ ] 知道 A2A 协议解决什么问题
- [ ] 了解 Agent Skills 打包格式，能把自己的工具打包成 skills
- [ ] 给自己的 Agent 做过完整评估：20+ 条测试集、指标、Langfuse tracing
- [ ] 拆解过 OpenHands（coding agent）架构
- [ ] 读过 2-3 篇 2025-2026 年 Agent 论文/技术报告，能讲清一个前沿方向（推理模型 + Agent、RL for Agents、Computer Use 等）
- [ ] 部署过完整服务：FastAPI + Docker + 云服务器，有线上 demo 链接

---

## 4. 十二周路线（2026.09.10 → 12.02）

| 周 | 日期 | 主线任务 | 每周一拆 | 周产出 |
|---|---|---|---|---|
| W1 | 9.10-9.16 | Python 补漏 + 调通 DeepSeek API + 手写 30 行 Agent Loop；**建 GitHub/掘金、申请学生包、开始每日刷题** | smolagents | 命令行助手 v1 + 第一篇博客 |
| W2 | 9.17-9.23 | 手写 ReAct（Thought→Action→Observation），接 5+ 工具，防死循环 | LangChain Hub 的 ReAct 实现 | ReAct Agent + 原理博客 |
| W3 | 9.24-9.30 | RAG 原理 → 无职转生语料抓取入库（Chroma + embedding） | Dify 的 RAG 实现 | RAG 问答 v1 |
| W4 | 10.1-10.7 | **国庆黑客松**：全离线 RAG 栈 + chunk 实验 + 引用溯源 | ollama+Chroma+bge 离线栈 | RAG v2 + 实验数据博客 |
| W5 | 10.8-10.14 | LangGraph 上：State/Node/Edge/条件路由，官方 tutorial 改造 | LangGraph multi-agent 示例 | 第一个 LangGraph 工作流 |
| W6 | 10.15-10.21 | LangGraph 下：checkpoint、断点续跑、human-in-the-loop | checkpoint/human-in-the-loop 例子 | 多步工作流项目 |
| W7 | 10.22-10.28 | MCP 周：用现成 Server → 自写一个 MCP Server | 一个 MCP Server 生态项目 | 自制 MCP Server |
| W8 | 10.29-11.4 | 项目一工程化：20 题评估集 + Langfuse tracing | Ragas | 项目一 v3（简历可用） |
| W9 | 11.5-11.11 | 项目二：追番推荐 + 安利文案多 Agent 流水线（考试周弹性） | GitHub 动漫推荐类项目 | 项目二 v1 |
| W10 | 11.12-11.18 | 项目二完善 + FastAPI/Docker 部署 | OpenHands | 项目二 v2 + 线上 demo |
| W11 | 11.19-11.25 | 前沿周：A2A/Agent Skills + 1 篇论文；**11 月底前合并第一个 PR** | A2A/Agent Skills 示例 + 论文 | 前沿笔记 + 第一个 PR |
| W12 | 11.26-12.2 | 简历 v1 + 八股自测 + 试投 5-10 家 | 3-5 个高星 AI 项目 README | 简历 + 面试复盘 |

每日固定件：刷题 30-45 分钟（早/晚自选）+ 睡前 10 分钟复盘。期中考试周（10 月底-11 月）主线弹性让路，GPA 保 80/3.0。

---

## 5. 技术栈与 API（2026.09 实价）

**核心栈（学习顺序）**：OpenAI 兼容 API → 手写原理 → Chroma → LangGraph → MCP → Langfuse → FastAPI/Docker

**API 方案**（预算 100 元/月，实际花不完）：
- 主力：**DeepSeek `deepseek-flash`（V4.1-Flash）**——输入缓存命中空闲时段 0.02 元/百万 token、未命中 1 元、输出 4 元；1M 上下文（[官方定价](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/)）
- 免费层辅助：Gemini（限额以 ai.google.dev 为准，2025 年有收紧先例）、智谱 GLM
- 网页版白嫖：ChatGPT / Claude，当陪练老师，不为 API 付费
- 本地离线：ollama `qwen3:8b`（Q4 约 5.5GB，8GB 显存放得下）+ bge-m3（本地 embedding）
- 代码里 LLM 后端可插拔：`base_url` + `model` 配置切换，不写死任何一家

```python
from openai import OpenAI
import json

client = OpenAI(base_url="https://api.deepseek.com", api_key="你的key")  # 切本地: base_url="http://localhost:11434/v1", model="qwen3:8b"

def agent(task):
    messages = [{"role": "system", "content": "你是助手"},
                {"role": "user", "content": task}]
    for _ in range(10):                      # 最多思考 10 轮
        resp = client.chat.completions.create(
            model="deepseek-flash", messages=messages, tools=TOOLS)
        msg = resp.choices[0].message
        if msg.tool_calls:                   # 模型想调工具
            messages.append(msg)
            for tc in msg.tool_calls:
                result = call_tool(tc.function.name,
                                   json.loads(tc.function.arguments))
                messages.append({"role": "tool",
                                 "tool_call_id": tc.id, "content": result})
        else:
            return msg.content               # 模型给出最终答案
```

---

## 6. 项目专项：无职转生主题（两个项目一条故事线）

### 项目一：无职转生知识库问答（RAG）

**RAG 大白话**：给大模型外挂"私人资料库"，回答前先检索再生成。三步：建库（切块→向量化→存 Chroma）→ 检索（语义最相关的几块）→ 生成（拼进 prompt 带出处回答）。好处：回答训练集外内容、有依据、少幻觉、可溯源。

**语料来源与抓取**：
- 萌娘百科"无职转生"相关词条（MediaWiki API 可批量抓取，结构化好，角色/剧情/世界观分栏）
- 中文维基百科对应条目
- Bangumi 番剧资料（开放 API，api.bgm.tv）
- 版权注意：仅个人学习用途，语料不入库公开仓库、不公开放出抓取数据，README 写清用途

**评估**：自拟 20 条问题（含角色、剧情、设定三类），每题记录"是否答对 + 是否给出处"，作为简历上的指标数字。

### 项目二：追番推荐 + 安利文案生成（多 Agent 流水线）

LangGraph 编排三个 Agent：**偏好分析 Agent**（解析用户"我喜欢无职转生"的输入）→ **推荐 Agent**（从 Bangumi 数据 + wiki 语料中找相似作品）→ **文案 Agent**（生成安利文案）→ 可选 **审查 Agent**（检查设定错误，防"文案把设定写错"）。全套二次元主题，面试故事连贯。

---

## 7. 每周一拆：方法与清单

**五步法**（每拆 1-2 小时）：
1. 读 README + 架构图，一句话讲清"它解决什么问题"——讲不清就不往下读
2. `git clone --depth 1` + 跑最小 demo，看实际输入输出
3. 找入口：main 函数、官方 Concepts 页，顺调用链往下追
4. 带着问题读：核心抽象？状态怎么流转？扩展点在哪？（IDE 跳转 + 全局搜索）
5. 写拆解笔记 + 小实验：改一个参数/换一个组件验证理解

**工具**：Cursor（选中代码让 AI 讲解）/ Excalidraw 画图 / Obsidian 离线笔记 / Langfuse 看 agent 内部轨迹

**笔记模板**（五段，写完发博客）：`一句话定位 / 核心架构 / 关键代码路径 / 我的复现实验 / 学到什么`

拆解清单见第 4 节表格"每周一拆"列。

---

## 8. 算法与课业（大四中大厂的准入项）

- 路径：**代码随想录**（免费，programmercarl.com）按专题走：数组 → 链表 → 栈队列 → 哈希 → 字符串 → 树 → 图，跟着数据结构课进度
- 节奏：LeetCode 简单题每天 1-2 题，先做再对题解；周日复盘错题本
- 认知：Agent 是加分项，算法是准入项——大厂校招笔试先筛算法，双非更要靠笔试过关
- 边界规则：平时自学优先；考前 1-2 周课程让路；GPA 保 80/3.0；大一欠的账用一年细水长流还，不突击

---

## 9. 简历补强：博客 + 开源 PR + 比赛

- **博客**（必做）：掘金/知乎，每两周一篇，第一篇本周就发（哪怕"我调通了 API"）
- **开源 PR**（11 月底前合并第一个）：① 在 LangChain/Dify 找 `good-first-issue` 标签；② 从文档翻译、typo、示例代码修正入手；③ fork → 改 → 提 PR → 按 review 改。合并后你就是 contributor，简历直接写
- **比赛**（随缘）：有好题才打（Kaggle LLM 赛题、服务外包、挑战杯），把现有项目包装参赛
- 简历排序：项目 > 开源 PR > 博客 > 比赛

---

## 10. 面试八股清单（W12 自测）

1. Agent 和普通 LLM 调用有什么区别？
2. ReAct 完整流程？Thought/Action/Observation 各是什么？
3. Function calling 底层原理？模型怎么知道调哪个工具？
4. RAG 全流程？怎么减幻觉？怎么评估检索质量？
5. 上下文窗口不够怎么办？
6. MCP 是什么？解决了什么问题？和直接写工具函数有什么区别？
7. 多 Agent 协作有哪些模式（流水线/辩论/主从）？
8. 怎么评估一个 Agent（成功率/轨迹/tracing/成本）？
9. LangGraph 的 checkpoint 和 human-in-the-loop 是什么？
10. 部署时怎么控制成本和延迟？

---

## 11. 资源清单

**课程（DeepLearning.AI 免费短课，优先级从高到低）**：AI Agents in LangGraph（必看）→ Functions, Tools and Agents with LangChain → Building Agentic RAG with LlamaIndex → Multi AI Agent Systems with crewAI（选看）

**官方文档（主料）**：docs.langchain.com、platform.openai.com/docs、modelcontextprotocol.io、a2a-protocol.org

**GitHub**：hwchase17/langgraph、huggingface/smolagents、All-Hands-AI/OpenHands、e2b-dev/awesome-ai-agents

**免费福利**：GitHub Student Developer Pack（学生邮箱申请，含免费 Copilot Pro、Codespaces；[申请页](https://education.github.com/pack)）

---

## 12. 实习时间线与投递策略

- **12 月（试投期）**：简历 v1 投 5-10 家。名单 = 北京 AI 创业公司/中小厂为主（BOSS 直聘搜"大模型应用开发实习"+北京）+ 大厂日常实习 2-3 家练手（字节/美团/百度 AI 应用岗）+ 远程/项目制兜底。目的：摸清市场 + 攒面试经验 + 按反馈改简历
- **寒假 1-2 月（主投期）**：项目打磨 + 大量投递，重点日常实习/项目制/远程（创业公司响应最快），到岗 3 天以上的岗位优先
- **大二下（持续期）**：边实习边学，为大三暑期实习（大厂转正通道）攒履历
- **渠道**：BOSS 直聘（量最大）→ 牛客 → 实习僧 → 学校就业中心 → 开源社区内推

---

## 13. 本周立即行动清单

1. ☐ 申请 GitHub Student Developer Pack（免费 Copilot）
2. ☐ 注册 DeepSeek 开放平台，充 10 元（够用很久）
3. ☐ 建掘金账号 + GitHub 第一个仓库
4. ☐ 本周末 2 小时：装 ollama + 拉 `qwen3:8b`、bge-m3（一次性配置清单见第 2 节）
5. ☐ 跑通第一个 chat 调用（上面代码片段改 key 就能跑）
6. ☐ 发第一篇博客：《我用 30 行代码写了一个 AI Agent》
