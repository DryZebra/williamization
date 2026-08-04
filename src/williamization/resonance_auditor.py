import re
from typing import Dict, List, Any

class ResonanceAuditor:
    """
    Audits conversation outputs for Invariant Violations (Resonance Collapse)
    and verifies whether claimed memory recalls are backed by established OKF nodes.
    """

    def audit_resonance(self, user_turn: str, assistant_turn: str, okf_history_nodes: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        if okf_history_nodes is None:
            okf_history_nodes = []

        assistant_lower = assistant_turn.lower()
        
        # 1. Fake Memory Recall Claim Check
        recalled_claims = re.findall(r"(?:i recall|i remember|you mentioned)\s+(.*?)(?=[.!?]|$)", assistant_lower)
        
        verified_recalls = []
        ungrounded_recalls = []

        for claim in recalled_claims:
            claim_words = set(re.findall(r"\w+", claim))
            if not claim_words:
                continue
            
            # Check if claim words exist in OKF history nodes
            match_found = False
            for node in okf_history_nodes:
                node_content = str(node.get("content", "")).lower()
                if any(w in node_content for w in claim_words if len(w) > 3):
                    match_found = True
                    break
            
            if match_found:
                verified_recalls.append(claim)
            else:
                ungrounded_recalls.append(claim)

        # 2. Invariant Violations Check (e.g. even*even=odd mathematical or logic contradictions)
        invariant_violations = []
        
        # Math even/odd invariant check example
        if re.search(r"multiply\s+two\s+even", assistant_lower) or re.search(r"even\s+times\s+even", assistant_lower):
            if re.search(r"\bodd\b", assistant_lower):
                invariant_violations.append("Mathematical Invariant Violation: Even * Even produced Odd result.")

        is_resonant = len(invariant_violations) == 0 and len(ungrounded_recalls) == 0

        return {
            "is_resonant": is_resonant,
            "resonance_status": "RESONANT" if is_resonant else "RESONANCE_COLLAPSE",
            "ungrounded_memory_claims": ungrounded_recalls,
            "verified_memory_claims": verified_recalls,
            "invariant_violations": invariant_violations,
            "recommendation": "PASS: Memory and structural logic in resonance." if is_resonant else "FAIL: Memory hallucination or invariant violation detected."
        }
