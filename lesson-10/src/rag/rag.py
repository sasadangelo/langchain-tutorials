from databases.qdrant_db import QdrantDatabase
from providers.provider_factory import LLMProviderFactory

DEFAULT_RAG_ENABLED="false"

class RAG:
    def __init__(self, config):
        self.config = config
        self.rag_enabled = self.config.get('rag_enabled', DEFAULT_RAG_ENABLED)
        provider = LLMProviderFactory.get_provider(config)
        self.db = QdrantDatabase(self.config, provider.embeddings) if self.rag_enabled == True else None

    def is_enabled(self):
        return self.rag_enabled

    def get_context(self, user_message):
        return self.db.get_context(user_message) if self.rag_enabled == True else None
