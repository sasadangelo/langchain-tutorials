import yaml
from databases.qdrant_db import QdrantDatabase
from providers.provider_factory import LLMProviderFactory

DEFAULT_RAG_ENABLED="false"

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

def main():
    config = load_config("config.yml")
    rag_enabled = config.get('rag_enabled', DEFAULT_RAG_ENABLED)
    provider = LLMProviderFactory.get_provider(config)
    db = QdrantDatabase(config, provider.embeddings) if rag_enabled == True else None
    context = db.get_context("Who is Xenobi Amilen?")
    print(context)

if __name__ == "__main__":
    # Call the main function when the script is executed.
    main()