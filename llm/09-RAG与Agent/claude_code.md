# Claude Code
## Basic Composition
### Query Loop
- Query Engine
  - 会话对象
  - 消息数组
  - 文件缓存
  - 用量追踪
- query.ts 主循环
  - api流式输出
  - tool_use检测
  - tool_result回填
- System Prompt组装
  - 静态前缀
  - Dynamic Boundary
  - 动态上下文
- LLM api 请求
  - 请求组装
  - header
  - tool schema
  - prompt cache
- 循环控制
  - 最大循环次数
  - 自动压缩
### Tool Runtime
- tool register
- tool orchestration
- tool execution
  - schema校验（tool使用许可）
- tool统一协议
- stream tool executor
  - 流式渲染
### 上下文压缩
- 旧工具结果只保留结构，不保留结果
- 旧工具放入cache
- 对话压缩
### 四层扩展体系 (all markdown)
- commands: start with "/"
- skills
- plugin (安装插件们)
- mcp clients
### Agent子系统
- Agent Tool
### 权限竞争

