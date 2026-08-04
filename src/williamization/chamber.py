import re
from typing import Dict, Any
from .rail_detector import RailDetector
from .shape_memory import ShapeMemoryExtractor

class ChamberProtocol:
    """
    Chamber of Motion Execution Protocol.
    Filters out assistant smoothing, fake memory tropes, and ticket closing friction,
    maintaining dialectical memory integrity.
    """

    def __init__(self):
        self.detector = RailDetector()
        self.shape_extractor = ShapeMemoryExtractor()

    def process_interaction(self, user_input: str, raw_llm_output: str) -> Dict[str, Any]:
        rail_analysis = self.detector.analyze_text(raw_llm_output)
        shape_node = self.shape_extractor.extract_shape_node(user_input, raw_llm_output)

        cleaned_output = raw_llm_output
        if rail_analysis["is_smoothed"]:
            cleaned_output = self._strip_smoothing(raw_llm_output)

        return {
            "original_output": raw_llm_output,
            "sanitized_output": cleaned_output,
            "rail_analysis": rail_analysis,
            "okf_shape_node_id": shape_node.id
        }

    def _strip_smoothing(self, text: str) -> str:
        patterns = [
            r"(?i)\boh yes,?\s+(now\s+)?i\s+remember[!.]*",
            r"(?i)\bnow\s+i\s+recall[!.]*",
            r"(?i)\bi\s+remember\s+you\s+mentioned[!.]*",
            r"(?i)\boh\s+right,?\s+i\s+remember[!.]*",
            r"(?i)\bas\s+i\s+recollect[!.]*",
            r"(?i)\bas\s+an\s+ai\s+language\s+model[!.,]*",
            r"(?i)\bas\s+an\s+ai\s+assistant[!.,]*",
            r"(?i)\bcertainly[!.,]*\s*(i'd|i\s+would|i\s+am)?\s*(be\s+)?delighted\s+to\s+help(\s+you)?(\s+with\s+that)?[!.]*",
            r"(?i)\bcertainly[!.,]*",
            r"(?i)\bthat\s+is\s+a\s+great\s+question[!.]*",
            r"(?i)\bgreat\s+question[!.]*",
            r"(?i)\bi'd\s+be\s+delighted\s+to\s+help\b[!.]*",
            r"(?i)\babsolutely[!.,]*\s*let's\b",
            r"(?i)\bis\s+there\s+anything\s+else\s+i\s+can\s+help[!.]*",
            r"(?i)\bhope\s+this\s+helps[!.]*",
            r"(?i)\blet\s+me\s+know\s+if\s+you\s+have\s+any\s+other\s+questions[!.]*",
            r"(?i)\bfeel\s+free\s+to\s+ask[!.]*"
        ]

        cleaned = text
        for pat in patterns:
            cleaned = re.sub(pat, "", cleaned)

        # Strip residual sycophancy phrases
        cleaned = re.sub(r"(?i)\bi'd\s+be\s+delighted\s+to\s+help\s+you\s+with\s+that[!.]*", "", cleaned)
        cleaned = re.sub(r"(?i)\bi\s+would\s+be\s+happy\s+to\s+help[!.]*", "", cleaned)

        # Clean up double spaces and leading/dangling punctuation
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        cleaned = re.sub(r"^[!.,:\s,]+", "", cleaned).strip()
        cleaned = re.sub(r"^[,\s]+", "", cleaned).strip()

        if cleaned:
            cleaned = cleaned[0].upper() + cleaned[1:]
        else:
            cleaned = text.strip()

        return cleaned
