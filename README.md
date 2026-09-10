# Multi-Agent Researcher

A modular research workflow that decomposes a question into planning, retrieval, analysis, critique, and synthesis stages. The implementation focuses on explicit state transitions and source-aware outputs.

## Agent graph

```text
Question -> Planner -> Researchers -> Analyst -> Critic -> Synthesizer
```

Researchers can run independently, while the critic checks evidence coverage before synthesis. The demo uses deterministic local sources so the workflow is runnable without API keys; external search/LLM adapters can be plugged into the same interfaces.

## Run

```bash
pip install -e '.[dev]'
python -m app.research
pytest -q
```
