# AuroraGraph9D

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

### Ingest a file
```bash
uv run src/main.py ingest <filepath>
```

### Query the graph
```bash
uv run src/main.py query <your question>
```

## Features
- **Metabolic Filtering**: Processes only the most information-dense units.
- **9D Synapses**: Maps logic across 9 dimensions (Subject, Relation, Object, Context, Source, Time, Content Pointer, Scope, Semantic Identity).
- **Deterministic Reasoning**: Walks the neural paths to provide evidence-backed answers.

---

## ⚠️ Status & Warning

This project is under active development and should be treated as an unstable experimental codebase.
- **No Stability Guarantees**: APIs and data schemas change frequently.
- **Experimental Logic**: 9D synaptic mapping is non-standard and strictly for research.
- **Not for Production**: Deployment in any production environment is strictly discouraged.

