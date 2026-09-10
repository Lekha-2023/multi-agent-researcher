from .state import ResearchState


def planner(state: ResearchState) -> ResearchState:
    state.plan = [
        f"Define scope for: {state.question}",
        "Collect independent evidence",
        "Compare findings and identify uncertainty",
        "Synthesize a cited answer",
    ]
    return state


def researcher(state: ResearchState, source_name: str, evidence: str) -> ResearchState:
    state.add_finding(evidence, source_name)
    return state


def analyst(state: ResearchState) -> ResearchState:
    state.analysis = " ".join(state.findings)
    return state


def critic(state: ResearchState) -> ResearchState:
    unique_sources = len(set(state.sources))
    state.critique = "Evidence coverage is sufficient." if unique_sources >= 2 else "Add an independent source before relying on this conclusion."
    return state


def synthesizer(state: ResearchState) -> ResearchState:
    citations = ", ".join(sorted(set(state.sources)))
    state.synthesis = f"{state.analysis}\n\nSources: {citations}"
    return state
