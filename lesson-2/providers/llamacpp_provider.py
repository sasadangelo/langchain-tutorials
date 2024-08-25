import os
from providers.provider import LLMProvider
from langchain_community.llms import LlamaCpp

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']
        chat_format = self.config['chat_format']
        transformers_path = os.path.expanduser(self.config['transformers_path'])
        self.model = LlamaCpp(model_path=transformers_path + "/" + model_path, chat_format=chat_format)

    def generate(self, messages):
        result = self.model.invoke(messages[0]['content'])
        return result
