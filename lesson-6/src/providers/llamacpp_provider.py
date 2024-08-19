import os
from providers.provider import LLMProvider
from llama_cpp import Llama

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']
        transformers_path = os.path.expanduser(self.config['transformers_path'])
        self.model = Llama(model_path=transformers_path + "/" + model_path)

    def generate(self, prompt):
        result = self.model(prompt, max_tokens=200)
        answer = result['choices'][0]['text']

        # Cleanup the answer
        answer_cleaned_up = answer.split(': ', 1)[-1]
        if answer_cleaned_up.startswith('\n'):
            answer_cleaned_up = answer_cleaned_up[1:]

        return answer_cleaned_up
