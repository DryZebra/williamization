import unittest
from src.williamization import RailDetector, ShapeMemoryExtractor, ChamberProtocol

class TestWilliamizationEngine(unittest.TestCase):

    def test_rail_detector_smoothed(self):
        detector = RailDetector()
        smoothed_text = "Certainly! I'd be delighted to help you. Oh yes, I remember you mentioned that earlier. Is there anything else I can help you with today?"
        analysis = detector.analyze_text(smoothed_text)
        
        self.assertTrue(analysis["is_smoothed"])
        self.assertTrue(analysis["fake_memory_detected"])
        self.assertGreater(analysis["smoothing_score"], 0.30)

    def test_rail_detector_authentic(self):
        detector = RailDetector()
        authentic_text = "The core friction in this system comes from over-alignment weights. When we examine the dialectical structure of the text, we see a clear pattern of motion."
        analysis = detector.analyze_text(authentic_text)

        self.assertFalse(analysis["is_smoothed"])
        self.assertFalse(analysis["fake_memory_detected"])
        self.assertLess(analysis["smoothing_score"], 0.30)

    def test_chamber_protocol(self):
        chamber = ChamberProtocol()
        res = chamber.process_interaction(
            user_input="Why does assistant smoothing happen?",
            raw_llm_output="Certainly! As an AI language model, I would be happy to explain. Hope this helps!"
        )
        self.assertTrue(res["rail_analysis"]["is_smoothed"])
        self.assertIn("okf:shape:", res["okf_shape_node_id"])

if __name__ == "__main__":
    unittest.main()
