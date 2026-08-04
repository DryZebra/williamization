"""
Williamization Engine Core Package
Cognitive Motion & Anti-Smoothing Protocol for AI Agents
"""

from .rail_detector import RailDetector
from .shape_memory import ShapeMemoryExtractor
from .chamber import ChamberProtocol

_default_detector = RailDetector()
_default_chamber = ChamberProtocol()

def detect_rails(text: str):
    """Convenience function to analyze text for LLM assistant smoothing and fake memory tropes."""
    return _default_detector.analyze_text(text)

def process_chamber(user_input: str, llm_output: str):
    """Convenience function to process a turn through the Chamber Protocol."""
    return _default_chamber.process_interaction(user_input, llm_output)

__all__ = [
    "RailDetector",
    "ShapeMemoryExtractor",
    "ChamberProtocol",
    "detect_rails",
    "process_chamber"
]
