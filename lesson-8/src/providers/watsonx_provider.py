import os

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ibm import WatsonxLLM
from providers.provider import LLMProvider


class WatsonXProvider(LLMProvider):
    def create_model(self):
        self.url = self.config["api_url"]
        self.parameters = self.config.get("parameters", {})
        # Retrieve the project ID from the environment variable
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.system_message = self.config["system_message"]

        self.model = WatsonxLLM(
            model_id=self.config["model"], url=self.url, project_id=self.project_id, params=self.parameters
        )

    def generate(self, chat_history_messages, user_message):
        # Concatenate the user message to the chat history to create a context for the LLM
        chat_messages = chat_history_messages + [user_message]
        formatted_prompt = self.__format_messages(chat_messages)
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
        return "\n".join(prompt)

    # Depending on message type in input it returns:
    # - system
    # - user
    # - assistant
    def __get_role(self, message: SystemMessage | HumanMessage | AIMessage) -> str:
        if isinstance(message, HumanMessage):
            return "<|user|>"
        elif isinstance(message, AIMessage):
            return "<|assistant|>"
        else:
            return "<|system|>"
