from providers.provider import LLMProvider
from transformers import pipeline

#DEFAULT_TEMPERATURE = 1.0

class HuggingFacesProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        tokenizer_name = self.config['model']
        #temperature = DEFAULT_TEMPERATURE
        #if 'parameters' in self.config and 'temperature' in self.config['parameters']:
        #    temperature = self.config['parameters']['temperature']
        #model_kwargs = { "temperature": 1.0 }
        self.model = pipeline("text-generation", model=model_name, tokenizer=tokenizer_name)

    def generate(self, prompt):
        # result = self.model(prompt, max_length=300, truncation=True)
        result = self.model(prompt, max_length=300)
        print(result)
        return result[0]["generated_text"]