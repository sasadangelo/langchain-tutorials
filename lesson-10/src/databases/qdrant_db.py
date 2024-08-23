import os
from databases.db import Database
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient

DEFAULT_QDRANT_PATH="~/.qdrant"
DEFAULT_QDRANT_COLLECTION="mycollection"
DEFAULT_RAG_TOP_K_CHUNKS=10

class QdrantDatabase(Database):
    def __init__(self, config, embeddings):
        self.config = config
        self.qdrant_path = os.path.expanduser(self.config.get('qdrant_path', DEFAULT_QDRANT_PATH))
        print(self.qdrant_path)
        self.qdrant_collection = self.config.get('qdrant_collection', DEFAULT_QDRANT_COLLECTION)
        print(self.qdrant_collection)

        # Verify if the path exists
        if not os.path.exists(self.qdrant_path):
            # If the path doesn't exist, create it
            os.makedirs(self.qdrant_path)
            print(f"Created the folder: {self.qdrant_path}")
        elif not os.path.isdir(self.qdrant_path):
            # If the path exist but t's not a directory raise an error
            raise NotADirectoryError(f"{self.qdrant_path} exists but is not a directory.")
        else:
            # If the path exists and it is a directory
            print(f"QDrant directory already exists: {self.qdrant_path}")

        qdrant_client = QdrantClient(path=self.qdrant_path)
        self.embeddings = embeddings
        self.qdrant = Qdrant(client=qdrant_client, collection_name=self.qdrant_collection, embeddings=embeddings)
    def get_context(self, user_message):
        context = None
        rag_top_k_chunks = self.config.get('rag_top_k_chunks', DEFAULT_QDRANT_PATH)
        if self.qdrant:
            context = [c.page_content for c in self.qdrant.similarity_search(user_message, k=rag_top_k_chunks)]
        return context

    def store(self, chunks):
        if chunks:
            self.qdrant.from_texts(
                chunks,
                self.embeddings,
                path=self.qdrant_path,
                collection_name=self.qdrant_collection,
                force_recreate=True
            )