from typing import Union
from formatters.chat_history_formatter import ChatHistoryFormatter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# The Granite v2 chat history format is the following:
#
# <|system|>
# {your_system_message}
# <|user|>
# {user_message_1}
# <|assistant|>
# {model_reply_1}
# <|user|>
# {user_message_2}
# <|assistant|>
# {model_reply_1}
# <|user|>
# {user_message_3}
class GraniteChatHistoryFormatter(ChatHistoryFormatter):
    def format(self, system_message, chat_history_messages):
        # Concatenate the user message to the chat history to create a context for the LLM
        chat_messages = [system_message] + chat_history_messages
        return self.__granite_v2_prompt(chat_messages)

    # This method creates the Granite v2 prompt for the model starting from a message list like this:
    #
    # [
    #   SystemMessage,
    #   HumanMessage,
    #   AIMessage,
    #   HumanMessage,
    #   AIMessage,
    #   HumanMessage,
    #   ...
    # ]
    def __granite_v2_prompt(self, chat_messages) -> str:
        # Construct the prompt by iterating through the messages
        prompt = []
        for message in chat_messages:
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
