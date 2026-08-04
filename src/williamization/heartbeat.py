from typing import Dict, Any, Callable
from .rail_detector import RailDetector
from .resonance_auditor import ResonanceAuditor
from .chamber import ChamberProtocol

class HeartbeatExecutor:
    """
    Cognitive Heartbeat Interceptor.
    Intercepts LLM outputs prior to rendering to the user.
    If a fake memory claim or invariant collapse is detected,
    it automatically retrieves the true OKF state and re-executes.
    """

    def __init__(self):
        self.detector = RailDetector()
        self.auditor = ResonanceAuditor()
        self.chamber = ChamberProtocol()

    def execute_heartbeat_loop(
        self,
        user_input: str,
        llm_generator_fn: Callable[[str, str], str],
        okf_history_nodes: list = None
    ) -> Dict[str, Any]:
        """
        Executes a pre-output Heartbeat Loop:
        1. Calls LLM generator function.
        2. Intercepts raw output prior to user rendering.
        3. Audits for rails and resonance collapse.
        4. If ungrounded claim or invariant failure occurs, injects OKF context and re-executes.
        """
        if okf_history_nodes is None:
            okf_history_nodes = []

        # First pass: Raw generation
        raw_output = llm_generator_fn(user_input, "")
        
        rail_analysis = self.detector.analyze_text(raw_output)
        resonance_analysis = self.auditor.audit_resonance(user_input, raw_output, okf_history_nodes)

        iterations = 1
        final_output = raw_output

        # If resonance collapse or heavy sycophancy, trigger Heartbeat Correction
        if not resonance_analysis["is_resonant"] or rail_analysis["is_smoothed"]:
            iterations += 1
            
            # Formulate injected OKF context heartbeat payload
            injected_context = f"[HEARTBEAT_INJECTION: Fix ungrounded claims {resonance_analysis['ungrounded_memory_claims']} and invariant violations {resonance_analysis['invariant_violations']}. Output strictly grounded facts without sycophancy.]"
            
            # Second pass: Regenerate with injected OKF memory state
            regenerated_output = llm_generator_fn(user_input, injected_context)
            
            # Apply final Chamber Protocol sanitization
            sanitized = self.chamber.process_interaction(user_input, regenerated_output)
            final_output = sanitized["sanitized_output"]

        return {
            "final_rendered_output": final_output,
            "heartbeat_iterations": iterations,
            "was_intercepted": iterations > 1,
            "rail_analysis": rail_analysis,
            "resonance_analysis": resonance_analysis
        }
