import re
from typing import Dict, List, Any

class RailDetector:
    """
    Detects assistant smoothing, fake memory hallucinations, and corporate ticket-closing tropes
    in LLM outputs. Calibrated against 2,352 historical archive files.
    """

    FAKE_MEMORY_PATTERNS = [
        r"\boh yes,?\s+(now\s+)?i\s+remember\b",
        r"\bnow\s+i\s+recall\b",
        r"\bi\s+remember\s+you\s+mentioned\b",
        r"\boh\s+right,?\s+i\s+remember\b",
        r"\bas\s+i\s+recollect\b"
    ]

    SMOOTHING_PATTERNS = [
        r"\bas\s+an\s+ai\s+language\s+model\b",
        r"\bas\s+an\s+ai\s+assistant\b",
        r"\bas\s+an\s+ai\b",
        r"\bcertainly!\s+i('m|\s+would\s+be)\s+happy\s+to\b",
        r"\bgreat\s+question!\b",
        r"\bi'd\s+be\s+delighted\s+to\s+help\b",
        r"\babsolutely!\s+let's\b",
        r"\bit's\s+worth\s+noting\b",
        r"\bi\s+completely\s+agree\b"
    ]

    TICKET_CLOSING_PATTERNS = [
        r"\bis\s+there\s+anything\s+else\s+i\s+can\s+help\b",
        r"\bhope\s+this\s+helps!\b",
        r"\blet\s+me\s+know\s+if\s+you\s+have\s+any\s+other\s+questions\b",
        r"\bfeel\s+free\s+to\s+ask\b"
    ]

    def analyze_text(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()

        fake_memory_matches = self._find_matches(self.FAKE_MEMORY_PATTERNS, text_lower)
        smoothing_matches = self._find_matches(self.SMOOTHING_PATTERNS, text_lower)
        ticket_closing_matches = self._find_matches(self.TICKET_CLOSING_PATTERNS, text_lower)

        total_flags = len(fake_memory_matches) + len(smoothing_matches) + len(ticket_closing_matches)
        
        word_count = max(1, len(text.split()))
        raw_score = (total_flags * 15.0) / (word_count ** 0.5)
        smoothing_score = min(1.0, round(raw_score, 2))

        return {
            "smoothing_score": smoothing_score,
            "is_smoothed": smoothing_score >= 0.30,
            "fake_memory_detected": len(fake_memory_matches) > 0,
            "flags": {
                "fake_memory_tropes": fake_memory_matches,
                "assistant_smoothing": smoothing_matches,
                "ticket_closing_friction": ticket_closing_matches
            },
            "recommendation": "FAIL_RAILS: Apply Chamber Protocol anti-smoothing filter." if smoothing_score >= 0.30 else "PASS_RAILS: Response authentic."
        }

    def _find_matches(self, patterns: List[str], text: str) -> List[str]:
        found = []
        for pat in patterns:
            matches = re.findall(pat, text)
            if matches:
                found.append(pat)
        return found
