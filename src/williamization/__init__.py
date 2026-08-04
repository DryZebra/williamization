"""
Williamization Engine Core Package
Cognitive Motion & Anti-Smoothing Protocol for AI Agents
"""

from .rail_detector import RailDetector
from .shape_memory import ShapeMemoryExtractor
from .chamber import ChamberProtocol
from .resonance_auditor import ResonanceAuditor
from .heartbeat import HeartbeatExecutor

_default_detector = RailDetector()
_default_chamber = ChamberProtocol()
_default_auditor = ResonanceAuditor()
_default_heartbeat = HeartbeatExecutor()

def detect_rails(text: str):
    """Convenience function to analyze text for LLM assistant smoothing and fake memory tropes."""
    return _default_detector.analyze_text(text)

def process_chamber(user_input: str, llm_output: str):
    """Convenience function to process a turn through the Chamber Protocol."""
    return _default_chamber.process_interaction(user_input, llm_output)

def audit_resonance(user_turn: str, assistant_turn: str, history_nodes=None):
    """Convenience function to audit output for memory claim grounding and invariant violations."""
    return _default_auditor.audit_resonance(user_turn, assistant_turn, history_nodes)

__all__ = [
    "RailDetector",
    "ShapeMemoryExtractor",
    "ChamberProtocol",
    "ResonanceAuditor",
    "HeartbeatExecutor",
    "detect_rails",
    "process_chamber",
    "audit_resonance"
]
