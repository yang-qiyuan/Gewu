# Model Context Protocal
Definition:
> MCP is essentially a universal adapter between AI applications and external tools or data sources. It defines a common protocol (built on JSON-RPC 2.0) that lets an AI assistant invoke functions, fetch data, or use predefined prompts from external services in a structured manner. 

Merits
- Allow plug in new capabilities without custom-coding each from scratch.
- Empowers more autonomous AI behavior. Agents are not limited to their built-in knowledge.
- Developers avoid the fragmentation of maintaining separate integrations.
-  Enforces a consistent request/response format across tools. This means your AI app doesn’t have to handle one HTTP response for Service A, another XML for Service B, etc. (all in json format)
-  Support the integration of contexts that could empower back-and-forth with various data source.
  

MCP OAuth 2.0

Useful Tricks over MCP
- Tool Suggestions, a call to a search_cities tool could return a structured list of cities and a suggestion of what to call next:
```
city_name,population,country,region
Tokyo,37194000,Japan,Asia
Delhi,32941000,India,Asia
Shanghai,28517000,China,Asia

Suggestion: To get more specific information (weather, attractions, demographics), try calling get_city_details with the city_name parameter.
```

