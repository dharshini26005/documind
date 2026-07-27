from services.embedding import EmbeddingService


class SemanticSearchService:

    @staticmethod
    def search(query, top_k=5):

        model = EmbeddingService.get_model()

        query_embedding = model.encode(query).tolist()

        results = EmbeddingService.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k

        )

        return results