20250519 面试记录
上海乐洺

二选一，完成一个即可，原则上5-7天完成

解答位于主目录:
`projects/Reward_Guided_Code_Optimizer`
`projects/RL_Guided_Code_Assistant_with_RAG_Based_Context_Retrieval`

# 线下算法题目2道
---

## 第一题--Advanced RL Code Optimizer Assignment

```
## Advanced RL Take-Home Assignment: Reward-Guided Code Optimizer

## Objective

Design and evaluate a reinforcement learning agent that **rewrites or transforms Python code snippets** to optimize a specified objective, guided by a reward signal.

---

## Core Task

1. Define or use a small corpus of Python functions (3–10 simple functions is enough).
2. Build a transformation agent that proposes code modifications.
3. Define a **reward function** to evaluate outputs (e.g., runtime speed, brevity, or correctness).
4. Use a **reinforcement learning algorithm** (REINFORCE, PPO, or similar) to train the agent.

---

## Required Components

### ✅ Code Transformation Agent

- Can be a model (e.g., LLM), token-level mutator, or AST-based transformer.
- Must output valid Python code.

### 🎯 Reward Design (Required)

Implement **two types** of rewards:
1. **Heuristic-based** (e.g., token length, `timeit`, static analysis).
2. **Learned reward model** (optional but encouraged):
- Train a small classifier or regressor on pairs (A better than B).

### 🔁 RL Algorithm

Use REINFORCE, PPO, or a simplified variant. Focus on:
- Sample efficiency
- Stability of updates
- Use of baselines or advantage estimators

---

## Stretch Goals

- Add pass/fail test suite signals to the reward
- Apply self-improvement (generate better data over time)
- Evaluate generalization on unseen functions

---

## Dataset Options

- Create synthetic Python snippets (~5–10 lines each)
- Or use [CodeSearchNet](https://huggingface.co/datasets/code_search_net) (Python subset)
- Or write 3–5 common utility functions as your base corpus

---

## Tools

- Libraries: `gym`, `transformers`, `trl`, `peft`, `ast`, `timeit`, `skrl`, or others
- Optional: Use CodeLlama, GPT-2, or a local model for generation

---

## Deliverables

1. **Code** (notebook or repo) with:
    - Agent implementation
    - Reward functions
    - Training loop and logs
2. **Report (1–2 pages or final notebook section)** covering:
    - Reward design decisions
    - Learning curve or before/after examples
    - Observations on model behavior, reward hacking, or generalization

---

## Time Budget: ~6–8 hours

This assignment is open-ended. Focus on demonstrating depth in RL formulation, reward design, and structured experimentation.

You are not expected to productionize your agent — aim for thoughtful design, working prototypes, and insightful evaluation.
```

```翻译
# 高级强化学习代码优化器作业
## 强化学习实践作业：奖励引导的代码优化器
## 目标
设计并评估一个强化学习智能体，该智能体可以**重写或转换Python代码片段**以优化指定目标，通过奖励信号进行引导。
---
## 核心任务

1. 定义或使用一个小规模的Python函数语料库（3-10个简单函数即可）。
2. 构建一个转换智能体来提出代码修改方案。
3. 定义一个**奖励函数**来评估输出结果（如运行速度、简洁性或正确性）。
4. 使用**强化学习算法**（REINFORCE、PPO或类似算法）训练智能体。
---
## 必需组件
### ✅ 代码转换智能体
- 可以是模型（例如LLM）、token级别变异器或基于AST的转换器。
- 必须输出有效的Python代码。
### 🎯 奖励设计（必选）
实现**两种类型**的奖励：
1. **基于启发式**的奖励（例如token长度、`timeit`、静态分析）。
2. **学习得到的奖励模型**（可选但鼓励）：
   - 在成对数据（A比B好）上训练一个小分类器或回归器。
### 🔁 RL算法
使用REINFORCE、PPO或简化变体。重点在于：
- 样本效率
- 更新稳定性
- 使用基线或优势估计器
---
## 扩展目标
- 在奖励中添加通过/失败测试套件信号
- 应用自我改进（随时间生成更好的数据）
- 评估在未见过的函数上的泛化能力
---
## 数据集选项
- 创建合成的Python代码片段（约5-10行每个）
- 或使用[CodeSearchNet](https://huggingface.co/datasets/code_search_net)（Python子集）
- 或编写3-5个常见的实用函数作为基础语料库
---
## 工具
- 库：`gym`、`transformers`、`trl`、`peft`、`ast`、`timeit`、`skrl`或其他
- 可选：使用CodeLlama、GPT-2或本地模型进行生成
---
## 交付内容
1. **代码**（notebook或仓库），包含：
    - 智能体实现
    - 奖励函数
    - 训练循环和日志
2. **报告**（1-2页或最终notebook部分），涵盖：
    - 奖励设计决策
    - 学习曲线或修改前后的示例
    - 关于模型行为、奖励作弊或泛化能力的观察
---
## 时间预算：约6-8小时
此作业是开放式的。重点在于展示RL公式化、奖励设计和结构化实验的深度。
不期望你将智能体产品化 - 旨在展示有思想的设计、可行的原型和有见地的评估。
```

- 题目简单解释
```text
想象你在一家咖啡店工作，店里有一台自动咖啡机，但它做咖啡的步骤有点慢，比如每次都要手动调整水温、磨豆时间、压粉力度等等。你的老板希望你能“优化”这台咖啡机的操作流程，让它更快地做出好喝的咖啡，同时保证咖啡味道不变。你决定用一种“智能”方法：设计一个“咖啡机优化助手”，通过不断尝试调整步骤，找到最佳的操作组合。

这个助手需要：
1. 尝试不同的调整（比如减少磨豆时间、提高水温）。
2. 评估效果（根据咖啡的味道、制作时间等给调整打分）。
3. 学习改进（通过试错，记住哪些调整让咖啡更好、更快）。

这个“咖啡机优化助手”的工作方式，就是这道题的核心思路！只不过，题目不是优化咖啡机，而是优化`Python`代码，用`强化学习（RL）`的方法让代码变得更好（比如运行更快、写得更简洁）。
```

---


## 第二题--ML Eng Assignment Revised
```
# Take-Home Assignment: RL-Guided Code Assistant with RAG-Based Context Retrieval

## Overview

You’re tasked with building a **code-aware assistant** that:
1. Retrieves relevant context (functions, docstrings, examples) from a code corpus to support a query
2. Generates helpful completions or explanations using an LLM
3. **Optimizes** the outputs using a simulated **reward signal**, via Reinforcement Learning or reranking

The focus is on building a small but functional RAG pipeline over code, and applying RL-like techniques to improve the quality of its outputs.

---

## What You’ll Build

### ✅ Core Pipeline

- A query (e.g., “How does `handle_error` work?” or “Give an optimized version of this snippet”) comes in
- You retrieve relevant code chunks (functions, docstrings, usage examples)
- Inject them into a prompt to generate an LLM output (answer, refactor, explanation)

### 🧠 Optional RL Layer

Use **RL (or pseudo-RL)** to improve the outputs:
- Define a **reward function** (e.g., correctness, brevity, style, performance, test case pass rate)
- Apply basic RL loop: reweight, rerank, or fine-tune your model using this reward
- If time is tight: simulate PPO via reranking + weighted sampling from top completions

---

## Corpus / Dataset Options

Choose one of:
- [CodeSearchNet (Python subset)](https://huggingface.co/datasets/code_search_net)
- [LangChain repo](https://github.com/langchain-ai/langchain) — great for retrieval use case
- Your own small repo clone

---

## Sample Tasks Your Agent Could Solve

- “Explain what `retry_with_backoff` does”
- “Optimize this function for fewer lines”
- “Find and fix the bug in this snippet”
- “Suggest how to refactor this async code to be synchronous”

---

## Tech Stack Suggestions

- Hints available if needed

---

## Deliverables

- Code repo or notebook with:
    - RAG pipeline over code
    - A simulated reward function
    - RL component (can be reranking, reward-weighted sampling, or full PPO if feasible)
- A short README:
    - Describe your design
    - Show at least 2–3 examples of inputs → completions → improvements
    - What you’d improve with more time

---

## Time Budget: 4–6 hours

You don’t need to productionize this. We’re looking for:
- Practical understanding of RAG for code
- Creativity in how you simulate or apply RL
- Reasonable, well-reasoned engineering tradeoffs
```

```翻译
# 机器学习工程师作业：基于RAG的代码助手与强化学习优化
## 概述
你需要构建一个**代码感知助手**，它能够：
1. 从代码语料库中检索相关上下文（函数、文档字符串、示例）以支持查询
2. 使用LLM生成有用的补全或解释
3. 通过模拟的**奖励信号**，使用强化学习进行输出优化
重点是构建一个小而功能完整的面向代码的RAG管道，并应用类似RL的技术来改进输出质量。
---
## 需要构建的内容
### ✅ 核心管道
- 收到查询（例如"如何工作`handle_error`？"或"给出这个片段的优化版本"）
- 检索相关的代码块（函数、文档字符串、使用示例）
- 将它们注入提示词中，生成LLM输出（答案、重构、解释）
### 🧠 可选的RL层
使用**强化学习(或伪RL)** 来改进输出：
- 定义一个**奖励函数**（如正确性、简洁性、风格、性能、测试用例通过率）
- 应用基本的RL循环：使用权重、重新排序或微调模型使用这个奖励
- 如果时间紧张：通过重新排序+加权抽样从顶级补全中模拟PPO
---
## 语料库/数据集选项
选择以下之一：
- [CodeSearchNet (Python子集)](https://huggingface.co/datasets/code_search_net) - 包含200万个(注释, 代码)对的数据集
  - 提供Go、Java、JavaScript、PHP、Python和Ruby语言的代码和文档
  - 每个数据点包含函数代码及其文档，以及存储库等元数据
  - 包含训练、测试和验证三个分割集
- [LangChain仓库](https://github.com/langchain-ai/langchain) - 构建LLM驱动应用程序的框架
  - 支持实时数据增强，连接LLM与多样数据源
  - 模型互操作性，可轻松替换模型
  - 可与LangSmith、LangGraph等工具集成
- 自己的小型仓库克隆
---
## 助手可以解决的示例任务
- "解释`retry_with_backoff`的作用"
- "将此函数优化为更少行数"
- "查找并修复此代码段中的bug"
- "建议如何将异步代码重构为同步代码"
---
## 技术栈建议
- 可提供提示信息（根据需要）
---
## 交付内容
- 包含以下内容的代码仓库或笔记本：
    - 面向代码的RAG管道
    - 模拟的奖励函数
    - RL组件（可以是重新排序、奖励加权抽样，或如果可行的话完整的PPO）
- 短README文件：
    - 描述你的设计
    - 展示至少2-3个输入→补全→改进的示例
    - 说明如果有更多时间你会改进什么
---
## 时间预算：4-6小时
不需要将此产品化。我们关注的是：
- 对代码RAG的实际理解
- 在模拟或应用RL时的创造力
- 合理且有根据的工程权衡决策
```

- 题目简单解释

```
想象你在一家图书馆工作，读者经常来问你问题，比如：“有没有一本讲时间管理的书？”或者“能不能帮我找一本更简单的Python入门书？”。你的任务是：
1. 从图书馆的书架上快速找到相关的书或资料（比如书的内容、简介、读者评论）。
2. 根据这些资料，给读者一个清晰、准确的回答（比如推荐一本书，或者解释某本书的核心内容）。
3. 还能根据读者的反馈（比如“这个回答太复杂了”或“这个推荐很实用”），不断优化回答方式，让读者更满意。

这个“图书馆智能助手”的工作方式，就是第二道题的核心！只不过，这里的“图书馆”是**代码库**，读者的问题是关于**代码的问题**（比如解释函数、优化代码），而优化回答的过程用的是**强化学习（RL）**的思路。
```

---

- 题目对比
```
如果：
- **对强化学习不太熟悉**，或者不想花太多时间调试RL算法，**选第二题**。可以用简单的关键词检索+现成LLM+伪RL，快速搭出一个能跑的系统，4–6小时内完成可能性高。
- **对代码分析（比如AST）或RL有经验**，并且喜欢挑战，**第一题**也不错。它的任务更聚焦（只改代码），可以用简单的规则改写+简单的REINFORCE，6–8小时也能完成，但需要更多调试。

**推荐第二题**，因为它更灵活、时间更短、门槛更低，适合快速上手。你可以用现成的代码库和模型，重点放在RAG和简单的优化逻辑，容易出成果。
```
| **维度**            | **第一题（Code Optimizer）**                          | **第二题（Code Assistant with RAG）**                |
|---------------------|----------------------------------------------------|--------------------------------------------------|
| **核心任务**        | 改写代码，优化性能（速度、简洁度）                  | 回答代码问题（解释、优化等），用RAG提供上下文    |
| **技术重点**        | 强化学习（RL）、代码改写                           | RAG（检索+生成）、RL（可伪RL）                  |
| **代码库准备**      | 自己写或找3–10个函数，稍费时                      | 用现成数据集（CodeSearchNet等），更省时          |
| **主要难点**        | RL算法实现（REINFORCE/PPO）、奖励设计              | RAG流程（检索+提示设计）、回答质量优化           |
| **RL难度**          | 必须实现完整RL，调试可能复杂                       | 可伪RL（reranking），门槛低                      |
| **时间预算**        | 6–8小时，稍长                                     | 4–6小时，较短                                   |
| **灵活性**          | 任务聚焦（只改代码），但RL要求高                   | 任务多样（解释、优化等），实现方式更灵活         |


