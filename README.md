# weaviate-quickstart

Follow https://weaviate.io/developers/weaviate/quickstart

## Usage
Spin up a cluster, create a collection, import data, then run a semantic search query:
```bash
% python quickstart_neartext_query.py
```

Output:
```json
{
  "answer": "Liver",
  "question": "This organ removes excess glucose from the blood & stores it as glycogen",
  "category": "SCIENCE"
}
{
  "answer": "DNA",
  "question": "In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance",
  "category": "SCIENCE"
}
```

Perform RAG:
```bash
% python quickstart_rag.py
```

Output:
```text
🚫🧠 Blood sugar regulator: Liver 🚀🍚 
🧫🧬 DNA 🧫🧬 twins: Watson & Crick's legacy! 💡🧪 #ScienceFacts 🤓🌟
```