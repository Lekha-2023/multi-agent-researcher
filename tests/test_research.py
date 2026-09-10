from app.research import plan, run

def test_plan_decomposes_question():
    assert len(plan("agentic AI")) == 3

def test_run_produces_synthesis():
    state=run("RAG")
    assert state.evidence
    assert "Research summary" in state.synthesis
