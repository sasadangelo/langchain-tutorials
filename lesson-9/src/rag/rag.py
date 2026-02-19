# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from databases.qdrant_db import QdrantDatabase
from embeddings import EmbeddingProtocol, EmbeddingProtocolFactory

DEFAULT_RAG_ENABLED = "false"


class RAG:
    def __init__(self) -> None:
        self.rag_enabled = chatterpy_config.rag.enabled
        embedding_protocol: EmbeddingProtocol = EmbeddingProtocolFactory.get_embedding_protocol()
        self.db = QdrantDatabase(embeddings=embedding_protocol.embeddings) if self.rag_enabled is True else None

    def is_enabled(self) -> bool:
        return self.rag_enabled

    def get_context(self, user_message):
        return self.db.get_context(user_message) if self.rag_enabled is True else None
