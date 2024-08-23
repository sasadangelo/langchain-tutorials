from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from formatters.chat_history_formatter import ChatHistoryFormatter

class PlainChatHistoryFormatter(ChatHistoryFormatter):
    def __init__(self):
        self.chat_prompt_template = ChatPromptTemplate.from_messages(
            [
               MessagesPlaceholder(variable_name="messages"),
           ]
        )

    def format(self, system_message, chat_history_messages):
        # Concatenate the user message to the chat history to create a context for the LLM
        chat_messages = [system_message] + chat_history_messages
        return self.chat_prompt_template.format(messages=chat_messages)
