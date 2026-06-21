"use client";

import { useCallback, useEffect, useState } from "react";
import {
  chat,
  deleteDocument,
  listDocuments,
  uploadDocument,
  type ChatResponse,
  type DocumentInfo,
} from "@/lib/api";

type Message = { role: "user" | "assistant"; content: string; meta?: ChatResponse };

export default function Home() {
  const [docs, setDocs] = useState<DocumentInfo[]>([]);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [useRag, setUseRag] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const refreshDocs = useCallback(async () => {
    try {
      setDocs(await listDocuments());
    } catch {
      setDocs([]);
    }
  }, []);

  useEffect(() => {
    refreshDocs();
  }, [refreshDocs]);

  async function handleUpload(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setError("");
    setLoading(true);
    try {
      await uploadDocument(file);
      await refreshDocs();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Upload failed");
    } finally {
      setLoading(false);
      e.target.value = "";
    }
  }

  async function handleAsk(e: React.FormEvent) {
    e.preventDefault();
    if (!input.trim()) return;
    const question = input.trim();
    setInput("");
    setError("");
    setMessages((m) => [...m, { role: "user", content: question }]);
    setLoading(true);
    try {
      const res = await chat(question, useRag);
      setMessages((m) => [...m, { role: "assistant", content: res.answer, meta: res }]);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Chat failed");
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(docId: string) {
    await deleteDocument(docId);
    await refreshDocs();
  }

  return (
    <main style={{ display: "grid", gridTemplateColumns: "280px 1fr", minHeight: "100vh" }}>
      <aside style={{ borderRight: "1px solid #334155", padding: "1.25rem" }}>
        <h1 style={{ fontSize: "1.1rem", marginTop: 0 }}>RAG Assistant</h1>
        <p style={{ fontSize: "0.85rem", color: "#94a3b8" }}>Upload docs → ask questions → get cited answers</p>

        <label style={labelStyle}>
          Upload (.txt, .md, .pdf)
          <input type="file" accept=".txt,.md,.pdf" onChange={handleUpload} disabled={loading} style={{ marginTop: 8 }} />
        </label>

        <h2 style={{ fontSize: "0.9rem", marginTop: "1.5rem" }}>Indexed documents</h2>
        <ul style={{ listStyle: "none", padding: 0, fontSize: "0.85rem" }}>
          {docs.length === 0 && <li style={{ color: "#64748b" }}>No documents yet</li>}
          {docs.map((d) => (
            <li key={d.doc_id} style={{ marginBottom: 8, display: "flex", justifyContent: "space-between", gap: 8 }}>
              <span>{d.filename}</span>
              <button type="button" onClick={() => handleDelete(d.doc_id)} style={btnSmall}>
                ×
              </button>
            </li>
          ))}
        </ul>
      </aside>

      <section style={{ display: "flex", flexDirection: "column", padding: "1.25rem" }}>
        <div style={{ flex: 1, overflowY: "auto", marginBottom: "1rem" }}>
          {messages.length === 0 && (
            <p style={{ color: "#64748b" }}>
              Try: upload <code>sample-docs/company-policy.txt</code> then ask &quot;What is the refund policy?&quot;
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
                maxWidth: "90%",
                marginLeft: m.role === "user" ? "auto" : 0,
              }}
            >
              <div style={{ fontSize: "0.7rem", color: "#94a3b8", marginBottom: 4 }}>
                {m.role === "user" ? "You" : m.meta?.mode === "rag" ? "RAG Assistant" : "Plain LLM"}
              </div>
              <div style={{ whiteSpace: "pre-wrap" }}>{m.content}</div>
              {m.meta?.sources && m.meta.sources.length > 0 && (
                <details style={{ marginTop: 8, fontSize: "0.8rem", color: "#94a3b8" }}>
                  <summary>{m.meta.sources.length} source(s)</summary>
                  {m.meta.sources.map((s, j) => (
                    <div key={j} style={{ marginTop: 6, padding: 8, background: "#0f172a", borderRadius: 4 }}>
                      <strong>{s.filename}</strong> (score {s.score})
                      <div style={{ marginTop: 4 }}>{s.text.slice(0, 200)}…</div>
                    </div>
                  ))}
                </details>
              )}
            </div>
          ))}
        </div>

        {error && <p style={{ color: "#f87171", fontSize: "0.85rem" }}>{error}</p>}

        <form onSubmit={handleAsk} style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <label style={{ display: "flex", alignItems: "center", gap: 6, fontSize: "0.85rem" }}>
            <input type="checkbox" checked={useRag} onChange={(e) => setUseRag(e.target.checked)} />
            RAG mode
          </label>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about your documents…"
            disabled={loading}
            style={{ flex: 1, padding: "0.65rem 0.85rem", borderRadius: 8, border: "1px solid #334155", background: "#1e293b", color: "#e2e8f0" }}
          />
          <button type="submit" disabled={loading} style={btnPrimary}>
            {loading ? "…" : "Send"}
          </button>
        </form>
      </section>
    </main>
  );
}

const labelStyle: React.CSSProperties = { display: "block", fontSize: "0.85rem", marginTop: "1rem" };
const btnPrimary: React.CSSProperties = {
  padding: "0.65rem 1.2rem",
  borderRadius: 8,
  border: "none",
  background: "#3b82f6",
  color: "#fff",
  cursor: "pointer",
};
const btnSmall: React.CSSProperties = {
  background: "transparent",
  border: "1px solid #475569",
  color: "#94a3b8",
  borderRadius: 4,
  cursor: "pointer",
  padding: "0 6px",
};
