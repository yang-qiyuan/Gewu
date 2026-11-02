## FAQ_Of_LLM_Interview

大模型算法岗面试题(含答案):
常见问题和概念解析 "大模型面试题"、"算法岗面试"、"面试常见问题"、"大模型算法面试"、"大模型应用基础"

- [面试必问问题](../interview-prep/%E9%9D%A2%E8%AF%95%E5%BF%85%E9%97%AE%E9%97%AE%E9%A2%98.md)

### Prompt--授人以鱼不如授人以渔
```
以老师教导学生的风格，教授我 [xxx]，循序渐进，言简意赅。  
1. 从日常生活中的实际场景引入，激发兴趣。  
2. 逐步引导，推导核心概念或公式[需要用$符号包围]，用通俗语言解释清楚（如果适用）。  
3. 深入讲解关键细节或进阶内容，保持清晰。[非常重要--深入讲解]  
4. 最后提供相关代码示例（如果适用），并简要解释代码逻辑。  
确保每步逻辑连贯，语言亲切，像老师一样耐心引导。
```

### 个人理解

```
第一是对于模型的了解,大模型涉及很宽,需要花费很多时间学习,但是一通百通
    以下4个内容复习完再去看大模型就像张无忌学了九阳神功一样，可以修炼模型大挪移了：
    - 复习线性代数：理解矩阵与样本数据特征值间的变换关系。
    - 复习(多元)微积分及(偏)导数：理解神经网络反向更新。
    - 复习统计学：理解特征值分布与模型基于概率预测原理（llm、diffusion都是）。
    - 复习pytorch: 训练模型逻辑如何,架构如何,损失函数如何。

第二是对于文档的处理,不管什么项目都需要处理文档,非常重要
    可以看看IBM的RAG竞赛的冠军方案

(现在还需要对于强化学习了解才行..)
```

### 目录

```text
llm/
├── 01-深度学习基础/          CNN、RNN、PyTorch、YOLO、激活函数、优化器
├── 02-Transformer与模型架构/ Transformer、位置编码、主流模型架构、MoE、多模态
├── 03-训练与评估/            训练流程、泛化能力、模型评估
├── 04-微调/                  LoRA、P-Tuning、Prefix-Tuning、PEFT、fine_tune 实战
├── 05-分布式训练与GPU/       Accelerate、DeepSpeed、大规模训练、CUDA
├── 06-推理与部署/            推理、量化、Docker、Kubernetes、Redis
├── 07-强化学习/              强化学习基础、GRPO
├── 08-数据/                  数据不平衡
├── 09-RAG与Agent/            RAG、向量数据库、MCP、Agent 框架、Prompt 工程
├── 10-业务场景/              金融风控、工业制造
├── thoughts_on_llm/          随笔
└── resources/                图片、论文、示例代码与练习文件
```

### 必备知识

在阅读本库前，建议补充一些数学/模型相关知识。

### 特别鸣谢
- [张老师](https://github.com/zyxcambridge)(提供了此库的最开始的思路,没有他就没有此库)
- [赵老师](https://未提供链接,hh.com)(无偿回答了很多问题)
- [Kesoft](https://github.com/Kesoft)(添加了pr)
- [胜算云AI团队](https://www.shengsuanyun.com/?from=CH_GRT40E7E)(胜算云模型API服务)
>**胜算云AI开发者扶持计划**：胜算云平台聚合了全球主流大模型 API（Claude、Gemini、GPT-4 等），目前已有超过 8 万开发者使用，由“长三角国家技术创新中心”的国家基金专项扶持，解决国内开发者在科研/项目中使用海外模型难、成本高的问题。平台与亚马逊云、微软azure、Google云（GCP）三大巨头官方合作，高折扣，非逆向，支付宝/微信、可发票，实名/邀请好友享更多代金券，点击此处进行注册：[渠道链接](https://www.shengsuanyun.com/?from=CH_GRT40E7E)
![](resources/img/z_ads/390a15b3f8dbcda1449e3365da3384f.png)

### 吐槽

```text
大模型这方向真的卷,新paper,新模型疯狂出,东西出的比我读的还快.
```

### 欢迎PR和联系我

![微信公众号二维码--随缘](resources/wechat/self_qr.png)

### *Star History*
[![Star History Chart](https://api.star-history.com/svg?repos=aceliuchanghong/FAQ_Of_LLM_Interview&type=Date)](https://www.star-history.com/#aceliuchanghong/FAQ_Of_LLM_Interview&Date)

<!-- related:start -->
## 相关笔记

- [深度学习基础索引](01-%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%9F%BA%E7%A1%80/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%9F%BA%E7%A1%80%E7%B4%A2%E5%BC%95.md)
- [Transformer与模型架构索引](02-Transformer%E4%B8%8E%E6%A8%A1%E5%9E%8B%E6%9E%B6%E6%9E%84/Transformer%E4%B8%8E%E6%A8%A1%E5%9E%8B%E6%9E%B6%E6%9E%84%E7%B4%A2%E5%BC%95.md)
- [训练与评估索引](03-%E8%AE%AD%E7%BB%83%E4%B8%8E%E8%AF%84%E4%BC%B0/%E8%AE%AD%E7%BB%83%E4%B8%8E%E8%AF%84%E4%BC%B0%E7%B4%A2%E5%BC%95.md)
- [微调索引](04-%E5%BE%AE%E8%B0%83/%E5%BE%AE%E8%B0%83%E7%B4%A2%E5%BC%95.md)
- [分布式训练与GPU索引](05-%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E4%B8%8EGPU/%E5%88%86%E5%B8%83%E5%BC%8F%E8%AE%AD%E7%BB%83%E4%B8%8EGPU%E7%B4%A2%E5%BC%95.md)
- [推理与部署索引](06-%E6%8E%A8%E7%90%86%E4%B8%8E%E9%83%A8%E7%BD%B2/%E6%8E%A8%E7%90%86%E4%B8%8E%E9%83%A8%E7%BD%B2%E7%B4%A2%E5%BC%95.md)
- [强化学习索引](07-%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0%E7%B4%A2%E5%BC%95.md)
- [数据索引](08-%E6%95%B0%E6%8D%AE/%E6%95%B0%E6%8D%AE%E7%B4%A2%E5%BC%95.md)
- [RAG与Agent索引](09-RAG%E4%B8%8EAgent/RAG%E4%B8%8EAgent%E7%B4%A2%E5%BC%95.md)
- [业务场景索引](10-%E4%B8%9A%E5%8A%A1%E5%9C%BA%E6%99%AF/%E4%B8%9A%E5%8A%A1%E5%9C%BA%E6%99%AF%E7%B4%A2%E5%BC%95.md)
- [ans](resources/result/ans.md)
<!-- related:end -->
