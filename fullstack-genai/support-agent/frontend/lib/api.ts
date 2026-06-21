const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8001";

export type AgentTraceStep = {
  agent: string;
  action: string;
  detail: string;
  output: string;
};

export type SourceSnippet = {
  title: string;
  snippet: string;
};

export type ChatResponse = {
  answer: string;
  session_id: string;
  intent: string;
  confidence: number;
  agents_used: string[];
  sources: SourceSnippet[];
  trace: AgentTraceStep[];
  metadata: Record<string, unknown>;
};

export type TicketInfo = {
  ticket_id: string;
  session_id: string;
  reason: string;
  customer_message: string;
  status: string;
  created_at: string;
};

export async function chat(message: string, sessionId?: string): Promise<ChatResponse> {
  const res = await fetch(`${API}/api/v1/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, session_id: sessionId }),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function listTickets(): Promise<TicketInfo[]> {
  const res = await fetch(`${API}/api/v1/tickets`);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
