from providers.provider import LLMProvider
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

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
        system_message = self.config['system_message']

        # Set the default parameters
        parameters = {
            'max_tokens': DEFAULT_MAX_TOKENS,
            'temperature': DEFAULT_TEMPERATURE,
            'top_p': DEFAULT_TOP_P,
            'top_k': DEFAULT_TOP_K,
            'repeat_penalty': DEFAULT_REPEAT_PENALTY,
            'context_size': DEFAULT_CONTEXT_SIZE
        }

        # Overwrite default values with the one in the YAML file
        if 'parameters' in self.config:
            parameters.update(self.config['parameters'])

        if self.config['debug'] == True:
            print("****************************************************************")
            print("DEBUG.                                                          ")
            print("Model parameters::                                              ")
            print("- max_tokens:", parameters['max_tokens'])
            print("- temperature:", parameters['temperature'])
            print("- top_p:", parameters['top_p'])
            print("- top_k:", parameters['top_k'])
            print("- repeat_penalty:", parameters['repeat_penalty'])
            print("- context_size:", parameters['context_size'])
            print("****************************************************************")

        # Create the model using the specified paremeters
        self.model = Ollama(model=model_name,
            base_url=base_url,
            temperature=parameters['temperature'],
            num_predict=parameters['max_tokens'],
            top_p=parameters['top_p'],
            top_k=parameters['top_k'],
            repeat_penalty=parameters['repeat_penalty'],
            num_ctx=parameters['context_size'],
        )
        self.chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_message),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

    def generate(self, messages):
        # Generate the prompt with the template
        formatted_prompt = self.chat_prompt_template.format(messages=messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")
        result = self.model.invoke(formatted_prompt)
        return result
