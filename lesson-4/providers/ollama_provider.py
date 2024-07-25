from providers.provider import LLMProvider
from langchain_community.llms import Ollama

class OllamaProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        self.model = Ollama(model=model_name)

    def generate(self, prompt_template, messages):
        # Generate the prompt with the template
        formatted_prompt = prompt_template.format(messages=messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")

        result = self.model.invoke(formatted_prompt)
        return result