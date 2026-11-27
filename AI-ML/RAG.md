# 🔎 Retrieval-Augmented Generation (RAG)

## Core Concepts
- [ ] Document loading
- [ ] Text cleaning and chunking
- [ ] Embedding generation
- [ ] Vector database
- [ ] Similarity search
- [ ] Metadata filtering
- [ ] Retrieval and reranking
- [ ] Context construction
- [ ] Source citations
- [ ] Retrieval and answer evaluation

## Build Plan: Document Q&A
1. Accept a document.
2. Extract and clean its text.
3. Split text into meaningful chunks.
4. Generate embeddings.
5. Store chunks and metadata.
6. Retrieve relevant passages for a question.
7. Generate an answer grounded in retrieved context.
8. Show sources and handle questions with insufficient evidence.

## Evaluation Questions
- Did retrieval find the right passages?
- Is the answer supported by those passages?
- Are citations accurate?
- What happens when the answer is not in the documents?
