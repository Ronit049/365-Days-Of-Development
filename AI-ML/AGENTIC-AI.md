# 🧠 Agentic AI Notes

## Core Concepts
- [ ] Agent vs. ordinary LLM application
- [ ] Goals and task decomposition
- [ ] Tool calling
- [ ] Planning and execution
- [ ] State and memory
- [ ] Workflow graphs
- [ ] Multi-agent coordination
- [ ] Human approval checkpoints
- [ ] Retries, timeouts, and error handling
- [ ] Tracing and observability
- [ ] Evaluation and safety
- [ ] MCP fundamentals

## Suggested Build Progression
1. Create a single agent that calls one safe tool.
2. Add structured inputs and outputs.
3. Add state and a clear stopping condition.
4. Add retries and logging.
5. Build a multi-step workflow.
6. Introduce multiple agents only when separate roles provide a real benefit.
7. Evaluate reliability, cost, and latency.

## Design Checklist
- What task is the agent allowed to perform?
- Which tools can it access?
- What actions require human approval?
- How are secrets protected?
- How does it recover from tool failure?
- How do I know whether it completed the task correctly?
