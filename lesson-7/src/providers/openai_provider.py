from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI

DEFAULT_TEMPERATURE = 1.0

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        temperature = DEFAULT_TEMPERATURE
        if 'parameters' in self.config and 'temperature' in self.config['parameters']:
            temperature = self.config['parameters']['temperature']
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)

    def generate(self, prompt):
        result = self.model.invoke(prompt)
        return result