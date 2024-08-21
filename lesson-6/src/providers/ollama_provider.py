from providers.provider import LLMProvider
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

class OllamaProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        system_message = self.config['system_message']
        self.model = Ollama(model=model_name)
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
