from dataclasses import dataclass
from typing import Protocol


class LLMProvider(Protocol):
    name: str

    def complete(self, prompt: str, *, system: str = "") -> str:
        ...


@dataclass
class MockProvider:
    name: str = "mock"

    def complete(self, prompt: str, *, system: str = "") -> str:
        if "refund" in prompt.lower():
            return "I am sorry for the frustration. We will refund you and follow up soon."
        return "I will help with a safe, accurate, and policy-aware response."


def provider_from_name(name: str) -> LLMProvider:
    return MockProvider()
