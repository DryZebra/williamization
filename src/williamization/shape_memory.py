import hashlib
from datetime import datetime
from typing import Dict, List, Any
from src.sekg import OKFNode

class ShapeMemoryExtractor:
    """
    Extracts dialectical 'shape of motion' and core philosophical/cognitive nodes
    from raw conversation turns into Open Knowledge Format (OKF).
    """

    def extract_shape_node(self, user_turn: str, assistant_turn: str) -> OKFNode:
        now = datetime.now().isoformat()
        content_combined = f"USER: {user_turn}\nASSISTANT: {assistant_turn}"
        
        # Generate abstract deterministic node ID
        node_hash = hashlib.sha256(content_combined.encode('utf-8')).hexdigest()[:12]
        node_id = f"okf:shape:{node_hash}"

        # Extract abstract themes & dialectical turns
        words_u = user_turn.split()
        words_a = assistant_turn.split()

        metadata = {
            "id": node_id,
            "type": "ShapeOfMotionNode",
            "title": f"Dialectical Motion Node {node_hash}",
            "created_at": now,
            "turn_word_ratio": len(words_a) / max(1, len(words_u)),
            "relations": [
                {
                    "target_id": "okf:framework:williamization",
                    "relationship_type": "EMBEDDED_IN"
                }
            ]
        }

        body_content = f"""# Dialectical Motion Node {node_hash}

## Abstract Continuity Shape
- User Turn Words: {len(words_u)}
- Assistant Turn Words: {len(words_a)}

## Structural Excerpt
{user_turn[:300]}
---
{assistant_turn[:300]}
"""

        return OKFNode(
            id=node_id,
            type="ShapeOfMotionNode",
            title=metadata["title"],
            metadata=metadata,
            content=body_content,
            relations=metadata["relations"]
        )
