from .graph import SEKGGraphEngine
from .arbiter import LLMArbiter

class SEKGEvolutionLoop:
    """Manages continuous self-evolution cycles for the Knowledge Graph."""

    def __init__(self, graph_engine: SEKGGraphEngine, arbiter: LLMArbiter):
        self.graph = graph_engine
        self.arbiter = arbiter

    def run_evolution_cycle(self):
        """Executes a single graph evolution cycle: gap detection & conflict cleanup."""
        gaps = self.graph.find_epistemic_gaps()
        # Dispatches queries or flag gaps for subagents
        return {
            "gaps_detected": len(gaps),
            "total_nodes": len(self.graph.nodes)
        }
