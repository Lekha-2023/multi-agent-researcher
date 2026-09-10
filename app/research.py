from dataclasses import dataclass, field

@dataclass
class ResearchState:
    question: str
    subquestions: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    analysis: str = ""
    critique: str = ""
    synthesis: str = ""

def plan(question: str) -> list[str]:
    return [f"What are the core concepts behind: {question}?", f"What are the main tradeoffs for: {question}?", f"What evidence would validate claims about: {question}?"]

def research(subquestions: list[str]) -> list[str]:
    return [f"Evidence collected for: {q}" for q in subquestions]

def analyze(evidence: list[str]) -> str:
    return " ".join(evidence)

def critique(evidence: list[str]) -> str:
    return "Evidence coverage is acceptable." if evidence else "No evidence available."

def synthesize(state: ResearchState) -> str:
    return f"Research summary for '{state.question}': {state.analysis} Critique: {state.critique}"

def run(question: str) -> ResearchState:
    state=ResearchState(question)
    state.subquestions=plan(question)
    state.evidence=research(state.subquestions)
    state.analysis=analyze(state.evidence)
    state.critique=critique(state.evidence)
    state.synthesis=synthesize(state)
    return state

if __name__ == "__main__": print(run("RAG architecture").synthesis)
