# Multi-Agent Researcher

A modular research workflow that separates planning, evidence collection, analysis, critique, and synthesis. The design makes agent responsibilities and state transitions explicit.

## Agent graph

```text
Question
   |
 Planner
   |
 +----------+----------+
 |          |          |
Researcher Researcher Researcher   <- parallelizable
 +----------+----------+
            |
         Analyst
            |
          Critic
            |
       Synthesizer
```

## Engineering features

- Explicit shared state instead of hidden agent memory
- Independent researcher stages that can be parallelized
- Source-aware findings
- Critic gate that checks evidence diversity
- Final synthesis with source attribution
- Local deterministic mode for reproducible tests
- Clear adapter boundary for external search and LLM providers

## Run

```bash
pip install -e '.[dev]'
python -m app.research
pytest -q
```

The repository does not claim live web-search results in its deterministic demo mode. Connect a search/LLM adapter when deploying it as a live research assistant.
