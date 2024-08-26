from providers.provider import LLMProvider
from langchain_community.llms import Ollama
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class OllamaProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        self.model = Ollama(model=model_name)
        # self.chat_prompt_template = ChatPromptTemplate.from_messages(
        #     [
        #         MessagesPlaceholder(variable_name="messages"),
        #     ]
        # )

    def generate(self, prompt):
        print("****************************************************************")
        print("Prompt:")
        print(prompt)
        print("****************************************************************")

        result = self.model.invoke(prompt)
        return result