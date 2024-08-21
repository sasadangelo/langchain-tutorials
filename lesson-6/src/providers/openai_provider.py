from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        temperature = self.config['temperature']
        system_message = self.config['system_message']
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)
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
