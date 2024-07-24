from providers.provider import LLMProvider
from langchain_community.llms import Ollama

class OllamaProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        self.model = Ollama(model=model_name)

    def generate(self, messages):
        result = self.model.invoke(messages[0]['content'])
        return result