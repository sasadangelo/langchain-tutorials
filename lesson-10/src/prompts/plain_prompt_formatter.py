from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import PromptTemplate
from prompts.prompt_formatter import PromptFormatter

class PlainPromptFormatter(PromptFormatter):
    PROMPT_TEMPLATE = (
    "{system_message}\n"
    "If available, use the following pieces of context enclosed by triple backquote to answer the question at the end."
    "Don't mention the word 'context' in the answer.\n\n"
    "Context:\n"
    "```"
    "{context}"
    "```\n\n"
    "Question: {user_message}\n"
    "Answer:")

    def __init__(self):
      self.__chat_prompt_template = ChatPromptTemplate.from_messages(
          [
              MessagesPlaceholder(variable_name="messages"),
          ]
      )

    def get_prompt(self, context, system_message, chat_history_messages, user_message):
        chat_history = self.__chat_history_format(chat_history_messages)
        combined_context = f"{context or ''}\n{chat_history or ''}"
        return PromptTemplate(template=self.PROMPT_TEMPLATE, input_variables=["system_message", "context", "chat_history", "user_message"]).format(system_message=system_message.content, context=combined_context, user_message=user_message.content)

    def __chat_history_format(self, chat_history_messages):
        return self.__chat_prompt_template.format(messages=chat_history_messages)