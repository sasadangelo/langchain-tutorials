from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from formatters.chat_history_formatter_factory import ChatHistoryFormatterFactory

class PromptFormatter:
    def get_prompt(self, context, system_message, chat_history_messages, user_message):
        raise NotImplementedError("Subclasses must implement the generate method")