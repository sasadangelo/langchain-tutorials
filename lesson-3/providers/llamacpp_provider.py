import os
from providers.provider import LLMProvider
from llama_cpp import Llama
from llama_cpp import Llama

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']
        transformers_path = os.path.expanduser(self.config['transformers_path'])
        self.model = Llama(model_path=transformers_path + "/" + model_path)

    def generate(self, prompt_template, messages):
        result = self.model.create_chat_completion([messages[-1]], max_tokens=None)
        return result['choices'][0]['message']['content']
