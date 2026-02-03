from endee import Endee
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class EndeeVectorStore:
    def __init__(self):
        self.db = Endee()

        self.vectors = []
        self.documents = []

    def add_documents(self, texts, embeddings):
        for i, vector in enumerate(embeddings):
            self.vectors.append(vector)
            self.documents.append(texts[i])

    def search(self, query_embedding, top_k=3):
        """
        Perform cosine similarity search over stored embeddings
        """
        similarities = cosine_similarity(
            [query_embedding],
            self.vectors
        )[0]

        top_indices = similarities.argsort()[-top_k:][::-1]
        return [self.documents[i] for i in top_indices]
