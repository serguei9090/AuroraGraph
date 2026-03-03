# AuroraGraph9D
## This is a personal learning project created for educational purposes and to explore different code concepts with ai concepts. 

* **Status:** Personal sandbox / Portfolio piece.
* **License:** This project is open-source and available for public educational use under the MIT License.
* **Purpose:** Academic research and technical skill development.
* 
> [!CAUTION]
> ### ⚠️ EXPERIMENTAL PROJECT — NOT FOR USAGE
> This codebase is a purely experimental research prototype. It is **NOT** intended for production use, general deployment, or any mission-critical applications. The core logic, including metabolic filtering and 9D synapses, is subject to breaking changes without notice.


9D Ingestion with Metabolic Filtering and Deterministic Reasoning.

## Setup

1. Install `uv`: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

### Run from Project Root
```bash
uv run run.py query "your question here"
```

### Ingest a folder
```bash
uv run src/main.py ingest <folderpath>
```

### Query the graph directly
```bash
uv run src/main.py query <your question>
```

## Features
- **Metabolic Filtering**: Processes only the most information-dense units.
- **9D Synapses**: Maps logic across 9 dimensions (Subject, Relation, Object, Context, Source, Time, Content Pointer, Scope, Semantic Identity).
- **Deterministic Reasoning**: Walks the neural paths to provide evidence-backed answers.

---

## Evaluation & Benchmarks

AuroraGraph9D includes a fully automated **LLM-as-a-Judge Evaluation Suite** (`tests/test_auragraph.py`) that scores the system against the RAG Triad: Context Relevance, Faithfulness, and Answer Relevance.

In recent benchmarks using a Golden Dataset of 25 complex questions (History, Math, Code, and Security) on a local Llama 3.1 8B model, **AuroraGraph9D achieved an Overall Score of 0.762 (Grade B).**

### How it compares to traditional Vector RAG:
- **Zero Hallucination:** AuroraGraph scored a perfect 1.00 on Answer Relevance during Negative Knowledge ("Hallucination Trap") tests. Traditional RAG often hallucinates connections due to semantic vector similarity; AuroraGraph's FTS5 BM25 keyword matching returns 0 exact matches, forcing the LLM to refuse the question.
- **Microsecond Retrieval:** FTS5 BM25 search takes ~10-20ms, compared to the 500ms+ required for embedding and cosine similarity searches in standard vector databases.
- **Configurable Context Window:** By leveraging `.env` configurations, users can expand the `FTS5_MATCH_LIMIT` to pull massive amounts of data into Ollama's 256k context window for complex cross-document aggregation.

---

## ⚠️ Status & Warning

This project is under active development and should be treated as an unstable experimental codebase.
- **No Stability Guarantees**: APIs and data schemas change frequently.
- **Experimental Logic**: 9D synaptic mapping is non-standard and strictly for research.
- **Not for Production**: Deployment in any production environment is strictly discouraged.

