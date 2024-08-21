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

    def generate(self, messages):
        # Generate the prompt with the template
        formatted_prompt = prompt_template.format(messages=messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")

        result = self.model.invoke(formatted_prompt)
        return result