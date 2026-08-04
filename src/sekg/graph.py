from typing import Dict, List, Optional
from .parser import OKFNode

class SEKGGraphEngine:
    """In-memory Knowledge Graph Engine managing OKF Nodes and directed edge relations."""

    def __init__(self):
        self.nodes: Dict[str, OKFNode] = {}
        self.adjacency: Dict[str, List[Dict[str, str]]] = {}

    def add_node(self, node: OKFNode):
        self.nodes[node.id] = node
        if node.id not in self.adjacency:
            self.adjacency[node.id] = []
        
        for rel in node.relations:
            target_id = rel.get("target_id")
            rel_type = rel.get("relationship_type", "CONNECTED_TO")
            if target_id:
                self.adjacency[node.id].append({"target": target_id, "type": rel_type})

    def get_node(self, node_id: str) -> Optional[OKFNode]:
        return self.nodes.get(node_id)

    def get_related_nodes(self, node_id: str) -> List[OKFNode]:
        edges = self.adjacency.get(node_id, [])
        return [self.nodes[edge["target"]] for edge in edges if edge["target"] in self.nodes]

    def find_epistemic_gaps(self, confidence_threshold: float = 0.8) -> List[OKFNode]:
        """Identifies nodes with low confidence or missing critical relations."""
        gaps = []
        for node in self.nodes.values():
            confidence = node.metadata.get("confidence_score", 1.0)
            if confidence < confidence_threshold or not node.relations:
                gaps.append(node)
        return gaps
