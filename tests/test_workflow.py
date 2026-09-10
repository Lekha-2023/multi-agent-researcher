from app.workflow import run_research


def test_research_workflow_collects_and_cites_sources():
    state = run_research("AI evaluation", [("source-a", "Evaluation measures quality."), ("source-b", "Evaluation catches regressions.")])
    assert len(state.plan) == 4
    assert len(state.findings) == 2
    assert "source-a" in state.synthesis
    assert "source-b" in state.synthesis
    assert "sufficient" in state.critique
