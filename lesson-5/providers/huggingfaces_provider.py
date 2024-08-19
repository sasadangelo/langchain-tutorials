from providers.provider import LLMProvider
from transformers import pipeline

class HuggingFacesProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        tokenizer_name = self.config['model']
        self.model = pipeline("text-generation", model=model_name, tokenizer=tokenizer_name)

    def generate(self, prompt):
        result = self.model(prompt, max_length=300)
        return result[0]["generated_text"]