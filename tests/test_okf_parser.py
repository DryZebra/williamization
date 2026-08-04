import os
import unittest
from src.sekg import OKFParser, SEKGGraphEngine

class TestOKFParser(unittest.TestCase):
    def test_parser(self):
        sample_path = os.path.join("okf", "graph", "markets", "sample_market_node.md")
        if os.path.exists(sample_path):
            node = OKFParser.parse_file(sample_path)
            self.assertEqual(node.type, "MarketOpportunity")
            self.assertIn("okf:market:", node.id)
            self.assertTrue(len(node.relations) > 0)

    def test_graph_engine(self):
        sample_path = os.path.join("okf", "graph", "markets", "sample_market_node.md")
        if os.path.exists(sample_path):
            node = OKFParser.parse_file(sample_path)
            graph = SEKGGraphEngine()
            graph.add_node(node)
            self.assertIn(node.id, graph.nodes)

if __name__ == "__main__":
    unittest.main()
