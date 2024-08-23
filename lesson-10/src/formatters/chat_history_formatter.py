from typing import Union
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class ChatHistoryFormatter:
    def format(self, system_message, chat_history_messages):
        raise NotImplementedError("Subclasses must implement the generate method")