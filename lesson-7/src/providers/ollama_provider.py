from providers.provider import LLMProvider
from langchain_community.llms import Ollama

DEFAULT_TEMPERATURE=0.8
DEFAULT_MAX_TOKENS=128
DEFAULT_TOP_P=0.9
DEFAULT_TOP_K=40
DEFAULT_REPEAT_PENALTY=1.1
DEFAULT_CONTEXT_SIZE=2048

class OllamaProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        base_url = self.config['base_url']

        # Set the default parameters
        parameters = {
            'temperature': DEFAULT_TEMPERATURE,
            'max_tokens': DEFAULT_MAX_TOKENS,
            'top_p': DEFAULT_TOP_P,
            'top_k': DEFAULT_TOP_K,
            'repeat_penalty': DEFAULT_REPEAT_PENALTY,
            'context_size': DEFAULT_CONTEXT_SIZE
        }

        # Overwrite default values with the one in the YAML file
        if 'parameters' in self.config:
            parameters.update(self.config['parameters'])

        # Create the model using the specified paremeters
        self.model = Ollama(
            model=model_name,
            base_url=base_url,
            temperature=parameters['temperature'],
            num_predict=parameters['max_tokens'],
            top_p=parameters['top_p'],
            top_k=parameters['top_k'],
            repeat_penalty=parameters['repeat_penalty'],
            num_ctx=parameters['context_size'],
        )

    def generate(self, prompt):
        result = self.model.invoke(prompt)
        return result