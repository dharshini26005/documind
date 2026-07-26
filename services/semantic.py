from services.embedding import EmbeddingService


class SemanticSearchService:

    @staticmethod
    def search(query, top_k=5):

        results = EmbeddingService.collection.query(

            query_texts=[query],
            n_results=top_k

        )

        return results