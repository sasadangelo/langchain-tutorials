from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        temperature = self.config['temperature']
        self.model = ChatOpenAI(temperature=temperature, model_name=model_name)
        self.chat_prompt_template = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

    def generate(self, prompt):
        print("****************************************************************")
        print("Prompt:")
        print(prompt)
        print("****************************************************************")

        result = self.model.invoke(prompt)
        return result