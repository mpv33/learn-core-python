from app.agents.triage import TriageAgent


def test_triage_keyword_fallback_order():
    agent = TriageAgent(llm=None)  # type: ignore[arg-type]
    intent, confidence, order_id = agent._keyword_fallback("Where is my order ORD-1001?")
    assert intent == "order_status"
    assert order_id == "ORD-1001"
    assert confidence >= 0.7


def test_triage_keyword_fallback_human():
    agent = TriageAgent(llm=None)  # type: ignore[arg-type]
    intent, _, _ = agent._keyword_fallback("I want to speak to a human please")
    assert intent == "human_handoff"
