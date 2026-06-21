const API = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export type Source = {
  text: string;
  filename: string;
  doc_id: string;
  chunk_index: number;
  score: number;
};

export type ChatResponse = {
  answer: string;
  sources: Source[];
  mode: string;
};

export type DocumentInfo = {
  doc_id: string;
  filename: string;
};

export async function uploadDocument(file: File) {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${API}/api/v1/documents/upload`, { method: "POST", body: form });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function listDocuments(): Promise<DocumentInfo[]> {
  const res = await fetch(`${API}/api/v1/documents`);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

export async function deleteDocument(docId: string) {
  const res = await fetch(`${API}/api/v1/documents/${docId}`, { method: "DELETE" });
  if (!res.ok) throw new Error(await res.text());
}

export async function chat(question: string, useRag: boolean): Promise<ChatResponse> {
  const res = await fetch(`${API}/api/v1/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, use_rag: useRag }),
  });
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}
