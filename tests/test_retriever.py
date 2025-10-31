import numpy as np
from sentence_transformers import SentenceTransformer
from src.rag.retriever_faiss import FaissRetriever

def test_faiss_retriever(tmp_path):
    # create a small FAISS index on the fly
    docs = ["India forest cover", "water bodies in India"]
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embs = embedder.encode(docs, convert_to_numpy=True)
    retriever = FaissRetriever()
    retriever.add(embs)
    D, I = retriever.retrieve("forest", topk=1)
    assert isinstance(D, list)
    assert isinstance(I, list)
    assert len(I) == 1
