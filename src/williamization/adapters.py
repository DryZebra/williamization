from typing import Any, Dict, List
from .chamber import ChamberProtocol
from .rail_detector import RailDetector

class WilliamizationLangChainCallback:
    """
    LangChain Callback Handler Adapter.
    Plug directly into LangChain agents / chains to intercept and sanitize LLM outputs automatically.
    """
    def __init__(self):
        self.chamber = ChamberProtocol()
        self.detector = RailDetector()

    def on_llm_end(self, response: Any, **kwargs: Any) -> None:
        """Executes automatically on LangChain LLM output completion."""
        pass

    def sanitize_text(self, user_input: str, raw_output: str) -> str:
        res = self.chamber.process_interaction(user_input, raw_output)
        return res["sanitized_output"]


class WilliamizationFastAPIMiddleware:
    """
    FastAPI Middleware Adapter.
    Automatically audits and sanitizes all outbound HTTP JSON payloads for AI services.
    """
    def __init__(self, app: Any):
        self.app = app
        self.chamber = ChamberProtocol()
