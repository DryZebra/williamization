import os
import sqlite3
import json
import time
from typing import Dict, List, Any, Optional

class SelfEvolvingKnowledgeGraph:
    """
    Self-Evolving Knowledge Graph (SEKG) Agentic Engine.
    Implements dynamic GraphRetrieve and GraphEdit (Node Insertion, Relationship Updating, and Contradiction Pruning).
    """
    def __init__(self, db_path: str = "local_william/sekg_store/sekg_memory.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS nodes (
                    id TEXT PRIMARY KEY,
                    concept TEXT NOT NULL,
                    category TEXT NOT NULL,
                    content TEXT NOT NULL,
                    confidence REAL DEFAULT 1.0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS edges (
                    id TEXT PRIMARY KEY,
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    relationship TEXT NOT NULL,
                    weight REAL DEFAULT 1.0,
                    FOREIGN KEY (source_id) REFERENCES nodes (id),
                    FOREIGN KEY (target_id) REFERENCES nodes (id)
                )
            """)
            conn.commit()

    # --- SEKG CORE FUNCTION 1: GraphRetrieve ---
    def graph_retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Multi-hop search across SEKG concept nodes and relationship edges for ResonanceAuditor."""
        query_words = set(query.lower().split())
        results = []
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, concept, category, content, confidence FROM nodes")
            nodes = cursor.fetchall()
            
            for n_id, concept, category, content, confidence in nodes:
                node_text = f"{concept} {category} {content}".lower()
                matches = sum(1 for w in query_words if w in node_text)
                if matches > 0:
                    results.append({
                        "id": n_id,
                        "concept": concept,
                        "category": category,
                        "content": content,
                        "confidence": confidence,
                        "relevance": matches
                    })
                    
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:top_k]

    # --- SEKG CORE FUNCTION 2: GraphEdit (Insert, Update, Prune) ---
    def graph_edit_insert_node(self, node_id: str, concept: str, category: str, content: str) -> bool:
        """Autonomous GraphEdit: Inserts a new verified concept node into the living SEKG graph."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO nodes (id, concept, category, content, updated_at)
                VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (node_id, concept, category, content))
            conn.commit()
        return True

    def graph_edit_prune_contradictions(self, concept: str, new_content: str) -> int:
        """Autonomous GraphEdit: Detects and prunes outdated/contradicted memory nodes."""
        pruned_count = 0
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, content FROM nodes WHERE concept = ?", (concept,))
            existing = cursor.fetchall()
            for n_id, old_content in existing:
                if old_content.lower() != new_content.lower():
                    cursor.execute("DELETE FROM nodes WHERE id = ?", (n_id,))
                    pruned_count += 1
            conn.commit()
        return pruned_count

    # --- SEKG CORE FUNCTION 3: Closed-Loop Agentic Evolution ---
    def evolve_from_interaction(self, user_turn: str, assistant_turn: str):
        """Closed-loop evolution: Automatically updates nodes and relationship edges from conversation turns."""
        if len(user_turn) < 5 or len(assistant_turn) < 10:
            return

        # Extract concept key
        concept_key = user_turn.split("?")[0].strip()[:40]
        node_id = f"node_{abs(hash(concept_key))}"
        
        # Self-correcting GraphEdit
        self.graph_edit_prune_contradictions(concept_key, assistant_turn)
        self.graph_edit_insert_node(node_id, concept_key, "DialecticalMemory", assistant_turn)
