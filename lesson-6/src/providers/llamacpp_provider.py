import os
from providers.provider import LLMProvider
from langchain_community.llms import LlamaCpp

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']
        chat_format = self.config['chat_format']
        transformers_path = os.path.expanduser(self.config['transformers_path'])
        self.model = LlamaCpp(model_path=transformers_path + "/" + model_path, chat_format=chat_format, n_ctx=2048)

    def generate(self, prompt):
        print("****************************************************************")
        print("Prompt:")
        print(prompt)
        print("****************************************************************")
        result = self.model.invoke(prompt)
        return result
