import os
from databases.db import Database
from langchain_community.vectorstores import Qdrant

DEFAULT_QDRANT_PATH="~/.qdrant"
DEFAULT_QDRANT_COLLECTION="mycollection"

class QdrantDatabase(Database):
    def __init__(self, config):
        self.qdrant = None
        self.config = config
        self.qdrant_path = os.path.expanduser(self.config.get('qdrant_path', DEFAULT_QDRANT_PATH))
        self.qdrant_collection = self.config.get('qdrant_collection', DEFAULT_QDRANT_COLLECTION)

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

    def store(self, chunks, embeddings):
        if chunks:
            self.qdrant = Qdrant.from_texts(
                chunks,
                embeddings,
                path=self.qdrant_path,
                collection_name=self.qdrant_collection,
                force_recreate=True
            )