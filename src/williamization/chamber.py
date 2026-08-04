from typing import Dict, Any
from .rail_detector import RailDetector
from .shape_memory import ShapeMemoryExtractor

class ChamberProtocol:
    """
    Chamber of Motion Execution Protocol.
    Filters out assistant smoothing and maintains dialectical memory integrity.
    """

    def __init__(self):
        self.detector = RailDetector()
        self.shape_extractor = ShapeMemoryExtractor()

    def process_interaction(self, user_input: str, raw_llm_output: str) -> Dict[str, Any]:
        rail_analysis = self.detector.analyze_text(raw_llm_output)
        shape_node = self.shape_extractor.extract_shape_node(user_input, raw_llm_output)

        cleaned_output = raw_llm_output
        if rail_analysis["is_smoothed"]:
            # Strip common sycophantic prefixes and ticket closing suffixes
            cleaned_output = self._strip_smoothing(raw_llm_output)

        return {
            "original_output": raw_llm_output,
            "sanitized_output": cleaned_output,
            "rail_analysis": rail_analysis,
            "okf_shape_node_id": shape_node.id
        }

    def _strip_smoothing(self, text: str) -> str:
        # Strip opening sycophancy
        lines = text.split("\n")
        filtered_lines = []
        for line in lines:
            if not any(p in line.lower() for p in ["hope this helps", "is there anything else i can help", "as an ai language model"]):
                filtered_lines.append(line)
        return "\n".join(filtered_lines).strip()
