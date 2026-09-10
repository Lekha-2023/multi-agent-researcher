from .agents import analyst, critic, planner, researcher, synthesizer
from .state import ResearchState


def run_research(question: str, evidence: list[tuple[str, str]]) -> ResearchState:
    state = planner(ResearchState(question))
    for source, finding in evidence:
        state = researcher(state, source, finding)
    state = analyst(state)
    state = critic(state)
    return synthesizer(state)
