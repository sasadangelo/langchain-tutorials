from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import PromptTemplate

class PlainPromptFormatter:
    def __init__(self):
      self.__chat_prompt_template = ChatPromptTemplate.from_messages(
          [
              MessagesPlaceholder(variable_name="messages"),
          ]
      )

    def get_prompt(self, context, system_message, chat_history_messages, user_message):
        # Format the chat history according to the configuration parameter chat_history_formatter
        chat_history = self.__chat_history_format(chat_history_messages)
        # Create the prompt using a PROMPT_TEMPLATE and filling it with the following information:
        # - context, if rag_enabled is True
        # - chat_history, for the first message only the system message will be present
        # - user_message, the user question
        prompt_template = self.__create_prompt_template(context, system_message, chat_history, user_message)
        return PromptTemplate(template=prompt_template, input_variables=["system_message", "context", "chat_history", "user_message"]).format(system_message=system_message.content, context=context, chat_history=chat_history, user_message=user_message.content)

    def __chat_history_format(self, chat_history_messages):
        return self.__chat_prompt_template.format(messages=chat_history_messages)

    def __create_prompt_template(self, context, system_message, chat_history, user_message):
        PROMPT_TEMPLATE = ""
        if system_message:
            PROMPT_TEMPLATE += "{system_message}\n"
        if context is not None and len(chat_history)>0:
            PROMPT_TEMPLATE += (
                "Use the following pieces of context enclosed by triple backquote and the chat history "
                "enclosed by triple dash to answer the question at the end but don't mention you're using them.\n\n"
                "Context:\n"
                "```\n"
                "{context}\n"
                "```\n\n"
                "Chat History:\n"
                "---\n"
                "{chat_history}\n"
                "---\n\n"
            )
        elif context is not None and len(chat_history)==0:
            PROMPT_TEMPLATE += (
                "Use the following pieces of context enclosed by triple backquote to answer the question at the end "
                "but don't mention you're using it.\n\n"
                "Context:\n"
                "```\n"
                "{context}\n"
                "```\n\n"
            )
        if context is None and len(chat_history)>0:
            PROMPT_TEMPLATE += (
                "Use the following pieces of chat history enclosed by triple dash to answer the question at the end but "
                "don't mention you're using them.\n\n"
                "Chat History:\n"
                "---\n"
                "{chat_history}\n"
                "---\n\n"
            )
        else:
            PROMPT_TEMPLATE += (
                "Answer to the following question.\n\n"
            )
        if user_message:
            PROMPT_TEMPLATE += (
                "Question: {user_message}\n\n"
                "Answer:"
            )
        return PROMPT_TEMPLATE

