## 1. Core mindset

- **Treat coding agents like junior engineers, not magic:** they work best when you give clear instructions about both the goal and the approach.
- **Human judgment still matters:** agents perform much better when you understand the codebase well enough to guide, review, and verify their work.
- **Bottom line:** agents do not replace engineers; they amplify engineers who can scope, guide, verify, and parallelize work effectively.

## 2. Prompting and instruction quality

- **Prompting is iterative engineering:** good results come from testing prompts, inspecting failures, and refining instructions systematically.
- **Context is the main lever:** agents do not know your local codebase, team conventions, workflow, or constraints unless you provide them explicitly.
- **Be direct and concrete:** specify the approach, point to the right files and docs, reduce ambiguity, and give access to tests, linters, type checks, and CI feedback.
- **Use the model to improve the prompt:** when results are weak, ask what was unclear, conflicting, or underspecified.
- **Use examples carefully:** examples help enforce formatting or patterns, but overly literal ones can make the model imitate instead of reason.

## 3. Where agents work best

- **Agents are strongest for bounded practical work:** small bug fixes, feature tweaks, documentation, side prototypes, and other well-scoped tasks are often ideal.
- **A major benefit is reducing interruption cost:** you can delegate the first pass on incoming requests instead of constantly breaking focus yourself.
- **They are also useful for exploring alternatives:** asking an agent to try multiple implementations can make tradeoffs more concrete.
- **Preview deployments help a lot for frontend tasks:** they make AI-generated UI changes easier to review and judge.
- **The best ROI is usually medium-size tasks:** roughly the kind of work that would take a human around 1–6 hours.

## 4. How to handle larger or more complex tasks

- **Large tasks should not be fully hands-off:** a better pattern is to let the agent draft, then review, iterate, and keep manual control over correctness and polish.
- **For vague or complex work, plan before coding:** let the agent first explore the codebase, identify relevant components, and answer discovery questions.
- **Use checkpoints for long tasks:** break work into stages such as planning, implementation, testing, fixing, and review.

## 5. Testing, feedback, and workflow design

- **Teaching agents how to verify improves results:** feedback should include not only what failed, but how you tested it.
- **Strong tests are one of the best force multipliers:** if agents frequently touch an area, better test coverage there usually pays off quickly.
- **Agents are useful for repetitive workflows:** dependency bumps, feature-flag cleanup, test maintenance, and repeated review checks are good candidates.
- **Reusable prompt playbooks improve reliability:** standardized workflows make repetitive agent tasks more scalable.
- **Agents can help with code review and rule enforcement:** especially for recurring team-specific mistakes that are hard to encode in standard lint rules.
- **They can assist with incidents, but not fully own production debugging:** they are better at surfacing suspicious changes than independently fixing live systems.

## 6. Context management

- **More context does not automatically help:** larger context windows can hurt performance if the extra material is noisy, stale, or conflicting.
- **The main context failure modes are poisoning, distraction, confusion, and clash.**
- **Poisoning:** one wrong fact in the context can get repeated and derail the whole run.
- **Distraction and confusion:** too much history, too many documents, or too many tools can pull the agent away from the actual task.
- **Clash:** conflicting instructions or mixed sources in context can lead to unstable behavior.
- **The real lesson is context management:** strong agent systems do not just stuff in more information; they select, prune, isolate, and refresh context carefully.

## 7. Infrastructure and tooling

- **Environment quality strongly affects success:** the agent should run in a setup that matches the real team environment, including dependencies, versions, auth, and secrets flow.
- **Custom tools can raise performance a lot:** simple CLI utilities, MCP integrations, helper scripts, and targeted test commands make the agent’s job easier.
- **A persistent knowledge base helps:** storing architecture notes, common commands, testing norms, and workflow rules prevents repeated mistakes.

## 8. Limitations and practical guardrails

- **Current limitations are still real:** debugging remains weak for complex bugs, visual reasoning is poor for pixel-level UI work, and knowledge cutoffs can cause outdated patterns unless current docs are provided.
- **Time management matters:** if an agent starts looping, drifting, or ignoring instructions, it is often better to stop early.
- **Restarting cleanly is often better than endless correction:** agents often recover poorly from messy runs but do better with a fresh attempt and better initial instructions.
- **Diversifying experiments helps:** try different prompts and task types, then double down on the settings where the agent naturally performs well.

## 9. Security

- **Security needs care:** use separate accounts, prefer staging or development environments, avoid unnecessary production access, and use readonly credentials when possible.

<!-- related:start -->
## 相关笔记

- [RAG与Agent索引](RAG%E4%B8%8EAgent%E7%B4%A2%E5%BC%95.md)
- [ucloud](../../interview-prep/logs/2024/ucloud.md)
- [上海ym](../../interview-prep/logs/2025/%E4%B8%8A%E6%B5%B7ym.md)
- [商汤绝影](../../interview-prep/logs/2025/%E5%95%86%E6%B1%A4%E7%BB%9D%E5%BD%B1.md)
- [术锐](../../interview-prep/logs/2025/%E6%9C%AF%E9%94%90.md)
- [RAG](RAG.md)
- [types_of_promp_engineering](types_of_promp_engineering.md)
<!-- related:end -->
