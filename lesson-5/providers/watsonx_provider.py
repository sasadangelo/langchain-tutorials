from typing import Union
from providers.provider import LLMProvider
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class WatsonXProvider(LLMProvider):
    def create_model(self):
        self.url = self.config["api_url"]
        self.project_id = self.config["project_id"]
        self.parameters = self.config.get("parameters", {})
        self.system_message = self.config['system_message']

        self.model = WatsonxLLM(
            model_id=self.config["model"],
            url=self.url,
            project_id=self.project_id,
            params=self.parameters
        )

    def generate(self, messages):
        formatted_prompt = self.__format_messages(messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")
        return self.model.invoke(formatted_prompt)

    # Convert the prompt messages list format
    def __format_messages(self, messages) -> str:
        # Construct the prompt by iterating through the messages
        prompt = []
        prompt.append("<|system|>")
        prompt.append(self.system_message)
        for message in messages:
            prompt.append(self.__get_role(message))
            prompt.append(message.content)
        return '\n'.join(prompt)

    # Depending on message type in input it returns:
    # - system
    # - user
    # - assistant
    def __get_role(self, message: Union[SystemMessage, HumanMessage, AIMessage]) -> str:
        if isinstance(message, HumanMessage):
            return "<|user|>"
        elif isinstance(message, AIMessage):
            return "<|assistant|>"
        else:
            return "<|system|>"
