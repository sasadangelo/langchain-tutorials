from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

DEFAULT_TEMPERATURE=0.8
DEFAULT_MAX_TOKENS=-1 # -1 Only works on ChatGPT
DEFAULT_TOP_P=0.9
DEFAULT_REPEAT_PENALTY=1.1

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        system_message = self.config['system_message']

        # Set the default parameters
        parameters = {
            'temperature': DEFAULT_TEMPERATURE,
            'max_tokens': DEFAULT_MAX_TOKENS,
            'top_p': DEFAULT_TOP_P,
            'repeat_penalty': DEFAULT_REPEAT_PENALTY
        }

        # Overwrite default values with the one in the YAML file
        if 'parameters' in self.config:
            parameters.update(self.config['parameters'])

        if self.config['debug'] == True:
            print("****************************************************************")
            print("Model parameters::                                              ")
            print("- temperature:", parameters['temperature'])
            print("- max_tokens:", parameters['max_tokens'])
            print("- top_p:", parameters['top_p'])
            print("- repeat_penalty:", parameters['repeat_penalty'])
            print("****************************************************************")

        self.model = ChatOpenAI(temperature=parameters['temperature'],
                                max_tokens=parameters['max_tokens'],
                                model_name=model_name,
                                model_kwargs={"top_p": parameters['top_p'],
                                              "frequency_penalty": parameters['repeat_penalty']})
        self.embeddings = OpenAIEmbeddings(model=model_name)
        self.chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_message),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

    def generate(self, prompt):
        if self.config['debug'] == True:
            print("****************************************************************")
            print("Prompt:")
            print(prompt)
            print("****************************************************************")
        result = self.model.invoke(prompt)
        return result
