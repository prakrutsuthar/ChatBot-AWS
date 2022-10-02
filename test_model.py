import torch
from sentence_transformers import util

class TestModel:
    def __init__(self):
        pass

    def test(self, metadata, embeddings, query, embedder, doc_count):
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, embeddings)[0]
        top_results = torch.topk(cos_scores, k=doc_count)
        relevant_docs = []
        for score, idx in zip(top_results[0], top_results[1]):
            data_dict = metadata[idx]
            data_dict.update({"relevancy_score" : float(score)})
            relevant_docs.append(data_dict)
        return relevant_docs