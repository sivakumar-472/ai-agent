# 🎯 Multi-Agent Finance Assistant - Morning Market Brief

A voice-enabled multi-agent financial assistant that delivers spoken market insights every morning. Built using FastAPI microservices, Langchain-compatible logic, and a Streamlit interface.

## 💡 Use Case
> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

The assistant answers:
> “Today, your Asia tech allocation is 22% of AUM, up from 18% yesterday.  
> TSMC beat estimates by 4%, Samsung missed by 2%.  
> Regional sentiment is neutral with a cautionary tilt due to rising yields.”

---

## ⚙️ Architecture Overview

### 🧠 Agents (FastAPI Services)
| Agent            | Description |
|------------------|-------------|
| API Agent        | Fetches real-time market data using Yahoo Finance. |
| Scraping Agent   | Scrapes financial filings using BeautifulSoup. |
| Retriever Agent  | Retrieves top-k relevant info from FAISS embeddings. |
| Analysis Agent   | Analyzes risk exposure, calculates changes. |
| Language Agent   | Synthesizes narrative using LLM-like logic. |
| Voice Agent      | Handles STT (Whisper) and TTS (pyttsx3). |

### 🎛️ Orchestrator
Orchestrates flow: `Voice → STT → Agents → RAG → LLM → TTS`.

### 🖥️ Streamlit Frontend
Single-click interface to hear market briefs.

---

## 🧪 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/multi-agent-finance-assistant.git
cd multi-agent-finance-assistant
