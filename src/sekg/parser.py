import os
import yaml
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class OKFNode:
    id: str
    type: str
    title: str
    metadata: Dict[str, Any]
    content: str
    relations: List[Dict[str, str]] = field(default_factory=list)
    file_path: Optional[str] = None

class OKFParser:
    """Parses Open Knowledge Format (OKF) Markdown files with YAML frontmatter."""

    @staticmethod
    def parse_file(file_path: str) -> OKFNode:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()

        frontmatter, content = OKFParser._split_frontmatter(raw_text)
        meta = yaml.safe_load(frontmatter) if frontmatter else {}

        node_id = meta.get("id", f"okf:generated:{os.path.basename(file_path)}")
        node_type = meta.get("type", "Unknown")
        node_title = meta.get("title", os.path.splitext(os.path.basename(file_path))[0])
        relations = meta.get("relations", [])

        return OKFNode(
            id=node_id,
            type=node_type,
            title=node_title,
            metadata=meta,
            content=content.strip(),
            relations=relations,
            file_path=file_path
        )

    @staticmethod
    def _split_frontmatter(text: str):
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                return parts[1], parts[2]
        return "", text
