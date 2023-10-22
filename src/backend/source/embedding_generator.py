import hnswlib
import pandas as pd
import numpy as np

class EmbeddingGenerator:

    def __init__(self, co, docs):
        self.co = co
        self.docs = docs
        print("Built embedding generator")
    
    def generate_embeddings(self, texts):
        print("Generating embeddings")
        query_emb = self.co.embed(texts=texts).embeddings
        return query_emb