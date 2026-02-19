# -----------------------------------------------------------------------------
# Copyright (c) 2025 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import os
from collections.abc import Iterable

from core import DistanceFunction, chatterpy_config
from databases.db import Database
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

DEFAULT_QDRANT_PATH = "~/.qdrant"
DEFAULT_QDRANT_COLLECTION = "mycollection"
DEFAULT_RAG_TOP_K_CHUNKS = 10


class QdrantDatabase(Database):
    def __init__(self, embeddings) -> None:
        self.qdrant_path = os.path.expanduser(chatterpy_config.rag.qdrant_path)
        self.qdrant_collection = chatterpy_config.rag.qdrant_collection

        # Verify if the path exists
        if not os.path.exists(path=self.qdrant_path):
            # If the path doesn't exist, create it
            os.makedirs(name=self.qdrant_path)
            print(f"Created the folder: {self.qdrant_path}")
        elif not os.path.isdir(self.qdrant_path):
            # If the path exist but t's not a directory raise an error
            raise NotADirectoryError(f"{self.qdrant_path} exists but is not a directory.")
        else:
            # If the path exists and it is a directory
            print(f"Qdrant directory already exists: {self.qdrant_path}")

        qdrant_client: QdrantClient = QdrantClient(path=self.qdrant_path)
        self.embeddings = embeddings
        # Check if the collection already exists in the QDrant path
        try:
            qdrant_client.get_collection(collection_name=self.qdrant_collection)
            print(f"Qdrant collection {self.qdrant_collection} already exists.")
        except ValueError:
            print(f"Qdrant collection {self.qdrant_collection} does not exist. Creating the collection...")
            embedding_vector_size: int = chatterpy_config.rag.embedding_vector_size
            embedding_distance_function: DistanceFunction = chatterpy_config.rag.embedding_distance_function
            qdrant_client.create_collection(
                collection_name=self.qdrant_collection,
                vectors_config=VectorParams(size=embedding_vector_size, distance=Distance(embedding_distance_function)),
            )
            print(f"Collection {self.qdrant_collection} created.")
        self.qdrant = QdrantVectorStore(
            client=qdrant_client, collection_name=self.qdrant_collection, embedding=embeddings
        )

    def store(self, chunks: Iterable[str]) -> None:
        if chunks:
            self.qdrant.add_texts(texts=chunks)

    def get_context(self, user_message):
        context = None
        rag_top_k_chunks = self.config.get("rag_top_k_chunks", DEFAULT_QDRANT_PATH)
        if self.qdrant:
            context = [c.page_content for c in self.qdrant.similarity_search(user_message, k=rag_top_k_chunks)]
        return context
