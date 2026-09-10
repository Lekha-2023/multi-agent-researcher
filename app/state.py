from dataclasses import dataclass, field


@dataclass
class ResearchState:
    question: str
    plan: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)
    analysis: str = ""
    critique: str = ""
    synthesis: str = ""
    sources: list[str] = field(default_factory=list)

    def add_finding(self, finding: str, source: str) -> None:
        self.findings.append(finding)
        self.sources.append(source)
