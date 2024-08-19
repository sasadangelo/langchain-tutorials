import os
from providers.provider import LLMProvider
from llama_cpp import Llama

DEFAULT_TEMPERATURE=0.8
DEEFAULT_MAX_TOKENS=16
DEFAULT_TOP_P = 0.9
DEFAULT_TOP_K = 40
DEFAULT_CONTEXT_SIZE=512

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']

        # Set the default parameters
        #parameters = {
        #    'context_size': DEFAULT_CONTEXT_SIZE
        #}

        # Overwrite default values with the one in the YAML file
        #if 'parameters' in self.config:
        #    parameters.update(self.config['parameters'])

        transformers_path = os.path.expanduser(self.config['transformers_path'])
        #self.model = Llama(model_path=transformers_path + "/" + model_path, n_ctx=parameters['context_size'])
        self.model = Llama(model_path=transformers_path + "/" + model_path)

    def generate(self, prompt):
        # Set the default parameters
        #parameters = {
        #    'temperature': DEFAULT_TEMPERATURE,
        #    'max_tokens': DEEFAULT_MAX_TOKENS,
        #    'top_p': DEFAULT_TOP_P,
        #    'top_k': DEFAULT_TOP_K,
        #}

        # Overwrite default values with the one in the YAML file
        #if 'parameters' in self.config:
        #    parameters.update(self.config['parameters'])

        result = self.model(prompt, max_tokens=None)
        #result = self.model(prompt, max_tokens=parameters['max_tokens'])
                             #, temperature=parameters['temperature'])
#                            top_p=parameters['top_p'],
#                            top_k=parameters['top_k'])
        answer = result['choices'][0]['text']

        # Cleanup the answer
        answer_cleaned_up = answer.split(': ', 1)[-1]
        if answer_cleaned_up.startswith('\n'):
            answer_cleaned_up = answer_cleaned_up[1:]

        return answer_cleaned_up
