"use client";

import { useCallback, useEffect, useState } from "react";
import { chat, listTickets, type ChatResponse, type TicketInfo } from "@/lib/api";

type Message = { role: "user" | "assistant"; content: string; meta?: ChatResponse };

const SUGGESTIONS = [
  "What's your refund policy?",
  "Where is order ORD-1001?",
  "I was charged twice on my card",
  "I want to speak to a human",
];

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [sessionId, setSessionId] = useState<string>();
  const [tickets, setTickets] = useState<TicketInfo[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const refreshTickets = useCallback(async () => {
    try {
      setTickets(await listTickets());
    } catch {
      setTickets([]);
    }
  }, []);

  useEffect(() => {
    refreshTickets();
  }, [refreshTickets]);

  async function sendMessage(text: string) {
    if (!text.trim()) return;
    setError("");
    setMessages((m) => [...m, { role: "user", content: text.trim() }]);
    setLoading(true);
    try {
      const res = await chat(text.trim(), sessionId);
      setSessionId(res.session_id);
      setMessages((m) => [...m, { role: "assistant", content: res.answer, meta: res }]);
      await refreshTickets();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Chat failed");
    } finally {
      setLoading(false);
    }
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    const text = input;
    setInput("");
    await sendMessage(text);
  }

  return (
    <main style={{ display: "grid", gridTemplateColumns: "300px 1fr", minHeight: "100vh" }}>
      <aside style={{ borderRight: "1px solid #334155", padding: "1.25rem" }}>
        <h1 style={{ fontSize: "1.1rem", marginTop: 0 }}>Support Agent</h1>
        <p style={{ fontSize: "0.85rem", color: "#94a3b8" }}>
          Multi-agent customer support — triage → specialist → supervisor
        </p>

        <h2 style={{ fontSize: "0.9rem", marginTop: "1.5rem" }}>Try asking</h2>
        <ul style={{ listStyle: "none", padding: 0, fontSize: "0.82rem" }}>
          {SUGGESTIONS.map((s) => (
            <li key={s} style={{ marginBottom: 8 }}>
              <button type="button" onClick={() => sendMessage(s)} disabled={loading} style={chipBtn}>
                {s}
              </button>
            </li>
          ))}
        </ul>

        <h2 style={{ fontSize: "0.9rem", marginTop: "1.5rem" }}>Open tickets</h2>
        <ul style={{ listStyle: "none", padding: 0, fontSize: "0.8rem" }}>
          {tickets.length === 0 && <li style={{ color: "#64748b" }}>None yet</li>}
          {tickets.map((t) => (
            <li key={t.ticket_id} style={{ marginBottom: 10, padding: 8, background: "#1e293b", borderRadius: 6 }}>
              <strong>{t.ticket_id}</strong>
              <div style={{ color: "#94a3b8", marginTop: 4 }}>{t.reason}</div>
            </li>
          ))}
        </ul>
      </aside>

      <section style={{ display: "flex", flexDirection: "column", padding: "1.25rem" }}>
        <div style={{ flex: 1, overflowY: "auto", marginBottom: "1rem" }}>
          {messages.length === 0 && (
            <p style={{ color: "#64748b" }}>
              AcmeShop support demo. Agents: <strong>triage</strong>, <strong>knowledge</strong>,{" "}
              <strong>orders</strong>, <strong>escalation</strong>, <strong>supervisor</strong>.
            </p>
          )}
          {messages.map((m, i) => (
            <div
              key={i}
              style={{
                marginBottom: "1rem",
                padding: "0.75rem 1rem",
                borderRadius: 8,
                background: m.role === "user" ? "#1e293b" : "#172554",
                maxWidth: "92%",
                marginLeft: m.role === "user" ? "auto" : 0,
              }}
            >
              <div style={{ fontSize: "0.7rem", color: "#94a3b8", marginBottom: 4 }}>
                {m.role === "user" ? "Customer" : `Agents: ${m.meta?.agents_used?.join(" → ") ?? "support"}`}
              </div>
              <div style={{ whiteSpace: "pre-wrap" }}>{m.content}</div>

              {m.meta && m.role === "assistant" && (
                <details style={{ marginTop: 10, fontSize: "0.78rem", color: "#94a3b8" }}>
                  <summary>
                    Agent trace · intent={m.meta.intent} · confidence={(m.meta.confidence * 100).toFixed(0)}%
                  </summary>
                  <ol style={{ paddingLeft: 18, marginTop: 8 }}>
                    {m.meta.trace.map((step, j) => (
                      <li key={j} style={{ marginBottom: 6 }}>
                        <strong>{step.agent}</strong> — {step.action}
                        <div>{step.detail}</div>
                        {step.output && <div style={{ color: "#64748b" }}>{step.output}</div>}
                      </li>
                    ))}
                  </ol>
                  {m.meta.sources.length > 0 && (
                    <div style={{ marginTop: 8 }}>
                      <strong>Sources</strong>
                      {m.meta.sources.map((s, j) => (
                        <div key={j} style={{ marginTop: 4, padding: 6, background: "#0f172a", borderRadius: 4 }}>
                          {s.title}: {s.snippet.slice(0, 120)}…
                        </div>
                      ))}
                    </div>
                  )}
                </details>
              )}
            </div>
          ))}
        </div>

        {error && <p style={{ color: "#f87171", fontSize: "0.85rem" }}>{error}</p>}

        <form onSubmit={handleSubmit} style={{ display: "flex", gap: 8 }}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Describe your issue…"
            disabled={loading}
            style={inputStyle}
          />
          <button type="submit" disabled={loading} style={btnPrimary}>
            {loading ? "…" : "Send"}
          </button>
        </form>
      </section>
    </main>
  );
}

const inputStyle: React.CSSProperties = {
  flex: 1,
  padding: "0.65rem 0.85rem",
  borderRadius: 8,
  border: "1px solid #334155",
  background: "#1e293b",
  color: "#e2e8f0",
};

const btnPrimary: React.CSSProperties = {
  padding: "0.65rem 1.2rem",
  borderRadius: 8,
  border: "none",
  background: "#10b981",
  color: "#fff",
  cursor: "pointer",
};

const chipBtn: React.CSSProperties = {
  width: "100%",
  textAlign: "left",
  padding: "0.5rem 0.65rem",
  borderRadius: 6,
  border: "1px solid #334155",
  background: "#1e293b",
  color: "#cbd5e1",
  cursor: "pointer",
  fontSize: "0.82rem",
};
