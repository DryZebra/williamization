from src.sekg import SEKGGraphEngine, OKFParser

class AgentCoordinator:
    """Master Orchestrator coordinating subagents with SEKG memory state."""

    def __init__(self, graph_engine: SEKGGraphEngine):
        self.graph = graph_engine

    def load_graph_from_directory(self, okf_dir: str):
        """Recursively parses and loads all OKF nodes in directory into SEKG."""
        import os
        for root, _, files in os.walk(okf_dir):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    node = OKFParser.parse_file(full_path)
                    self.graph.add_node(node)

    def dispatch_monetization_cycle(self):
        """Coordinates MarketMiner -> ProductSynthesizer -> RevenueOperator flow."""
        gaps = self.graph.find_epistemic_gaps()
        return {
            "status": "DISPATCHED",
            "active_gaps": [g.id for g in gaps]
        }
