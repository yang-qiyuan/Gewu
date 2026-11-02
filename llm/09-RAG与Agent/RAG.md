1. RAG的优缺点
```Text
优点：
1. 降低幻觉。
2. 知识更新快，适合动态信息。
3. 参数规模要求低。
缺点：
1.依赖检索质量
2. 上下文长度限制
3. 文档切分 & 向量化难题
    分段太小：丢上下文。 --大模型参与分块
    分段太大：检索不准。
    缺乏全局视角
    向量化质量直接影响召回效果。
4. 知识冲突
```
2. RAG常用框架

<!-- related:start -->
## 相关笔记

- [RAG与Agent索引](RAG%E4%B8%8EAgent%E7%B4%A2%E5%BC%95.md)
- [上海ym](../../interview-prep/logs/2025/%E4%B8%8A%E6%B5%B7ym.md)
- [喆塔信息](../../interview-prep/logs/2025/%E5%96%86%E5%A1%94%E4%BF%A1%E6%81%AF.md)
- [个人存储的各方向速成问题及解答-2025](../../interview-prep/%E4%B8%AA%E4%BA%BA%E5%AD%98%E5%82%A8%E7%9A%84%E5%90%84%E6%96%B9%E5%90%91%E9%80%9F%E6%88%90%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E7%AD%94-2025.md)
- [agent_framework](agent_framework.md)
- [prompt_engineering_guide](prompt_engineering_guide.md)
- [向量数据库](%E5%90%91%E9%87%8F%E6%95%B0%E6%8D%AE%E5%BA%93.md)
- [常见大模型调用代码](%E5%B8%B8%E8%A7%81%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%B0%83%E7%94%A8%E4%BB%A3%E7%A0%81.md)
- [阿里云工业制造](../10-%E4%B8%9A%E5%8A%A1%E5%9C%BA%E6%99%AF/%E9%98%BF%E9%87%8C%E4%BA%91%E5%B7%A5%E4%B8%9A%E5%88%B6%E9%80%A0.md)
<!-- related:end -->
