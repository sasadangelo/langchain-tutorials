from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        self.model = ChatOpenAI(temperature=0.8, model_name=model_name)

    def generate(self, prompt):
        result = self.model.invoke(prompt)
        return result