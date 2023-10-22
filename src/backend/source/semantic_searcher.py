import hnswlib
from tqdm import tqdm

class SemanticSearcher:

    def __init__(self, co, docs, embeddings):
        self.co = co
        self.docs = docs
        self.index = hnswlib.Index(space='ip', dim=4096)
        self.index.init_index(max_elements=len(embeddings), ef_construction=512, M=64)
        self.index.add_items(embeddings, list(range(len(embeddings))))
        print("Built semantic searcher")
    
    def semantic_search(self, embeddings, df):
        print("Semantic searching")
        

        artists = df['artist_name'].to_list()
        tracks = df['track_name'].to_list()

        results = []

        for emb in tqdm(embeddings):
            doc_ids = self.index.knn_query(emb, k=1)[0][0]

            for doc_id in doc_ids:
                print(self.docs[doc_id], doc_id)
                results.append({"artist": artists[doc_id], "title": tracks[doc_id]})

        return results