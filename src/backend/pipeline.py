import cohere
import os
import numpy as np
import pandas as pd
import os
from backend.source.embedding_generator import EmbeddingGenerator
from backend.source.semantic_searcher import SemanticSearcher
from backend.source.text_parser import TextParser

key = os.getenv("COHERE_KEY")

class Pipeline:

    def __init__(self, key):
        # Instantiate API
        self.co = cohere.Client(key)

        # print(os.listdir('backend/'))
        os.chdir('backend/')

        # Load data
        self.dataset = pd.read_csv('without_lyric_commercial.csv')
        self.embeddings = np.load('embeddings.npy')
        print("Loaded dataset and embeddings")

        self.text_parser = TextParser(self.co)
        
        self.embedding_generator = EmbeddingGenerator(self.co, 
                                                     self.dataset['lyrics'])
        
        self.semantic_searcher = SemanticSearcher(self.co, 
                                                     self.dataset['lyrics'], 
                                                     self.embeddings)
        
    def execute_pipeline(self, text):
        texts = self.text_parser.parse_text(text)
        embeddings = self.embedding_generator.generate_embeddings(texts)
        return self.semantic_searcher.semantic_search(embeddings, self.dataset)
