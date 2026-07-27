from sentence_transformers import SentenceTransformer
import chromadb


class EmbeddingService:

    model = None

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        "documents"
    )

    @classmethod
    def get_model(cls):

        if cls.model is None:

            print("Loading SentenceTransformer model...")

            cls.model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        return cls.model

    @classmethod
    def save_embeddings(
        cls,
        document_id,
        chunks
    ):

        model = cls.get_model()

        embeddings = model.encode(chunks)

        for i, chunk in enumerate(chunks):

            cls.collection.add(

                ids=[f"{document_id}_{i}"],

                documents=[chunk],

                embeddings=[embeddings[i].tolist()],

                metadatas=[
                    {
                        "document_id": document_id,
                        "chunk": i
                    }
                ]

            )