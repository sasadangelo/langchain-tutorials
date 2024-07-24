from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        temperature = self.config['temperature']
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)

    def generate(self, messages):
        result = self.model.invoke(messages[0]['content'])
        return result