from pathlib import Path

from app.services.knowledge_base import KnowledgeBase

SAMPLE_KB = Path(__file__).resolve().parents[2] / "sample-data" / "knowledge-base.md"


def test_knowledge_base_loads_sections():
    kb = KnowledgeBase(str(SAMPLE_KB))
    assert len(kb._sections) >= 4


def test_knowledge_base_search_returns():
    kb = KnowledgeBase(str(SAMPLE_KB))
    hits = kb.search("refund return policy", top_k=2)
    assert hits
    assert any("return" in h["title"].lower() or "refund" in h["body"].lower() for h in hits)
