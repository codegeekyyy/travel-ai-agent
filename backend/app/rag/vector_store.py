import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embedding: np.ndarray, document: str):
        self.index.add(embedding.reshape(1, -1))
        self.documents.append(document)

    def search(self, embedding: np.ndarray, k: int = 3):
        distances, indices = self.index.search(
            embedding.reshape(1, -1), k
        )
        return [self.documents[i] for i in indices[0] if i != -1]
