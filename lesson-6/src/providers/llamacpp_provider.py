import os
from typing import List, Union
from providers.provider import LLMProvider
from llama_cpp import Llama
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
import pprint

class LLamaCppProvider(LLMProvider):
    def create_model(self):
        model_path = self.config['model_path']
        chat_format = self.config['chat_format']
        self.system_message = self.config['system_message']
        transformers_path = os.path.expanduser(self.config['transformers_path'])
        self.model = Llama(model_path=transformers_path + "/" + model_path, chat_format=chat_format, n_ctx=512)

    def generate(self, messages):
        format_messages = self.__format_messages(messages)
        pprint.pprint("****************************************************************")
        pprint.pprint("Chat History + Question:")
        pprint.pprint(format_messages)
        pprint.pprint("****************************************************************")
        result = self.model.create_chat_completion(format_messages, max_tokens=None)
        return result['choices'][0]['message']['content']

    # Depending on message type in input it returns:
    # - system
    # - user
    # - assistant
    def __get_role(self, message: Union[SystemMessage, HumanMessage, AIMessage]) -> str:
        if isinstance(message, HumanMessage):
            return "user"
        elif isinstance(message, AIMessage):
            return "assistant"
        else:
            return "system"

    # Convert the prompt messages list format
    def __format_messages(self, messages: List[Union[SystemMessage, HumanMessage, AIMessage]]) -> List[dict]:
        formatted_messages = [{"role": "system", "content": self.system_message}]
        for message in messages:
            formatted_messages.append({"role": self.__get_role(message), "content": message.content})
        return formatted_messages
