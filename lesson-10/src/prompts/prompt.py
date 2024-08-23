from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from formatters.chat_history_formatter_factory import ChatHistoryFormatterFactory

class Prompt:
    _chat_prompt_template = ChatPromptTemplate.from_messages(
        [
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    @staticmethod
    def create_prompt_template(context, chat_history, user_message):
        PROMPT_TEMPLATE = ""
        if context is not None:
            PROMPT_TEMPLATE += (
                "Use the following pieces of context enclosed by triple backquote and the chat history "
                "enclosed by triple dash to answer the question at the end but don't mention you're using them.\n"
                "Context:\n"
                "```\n"
                f"{context}\n"
                "```\n\n"
                "Chat History:\n"
                "---\n"
                f"{chat_history}\n"
                "---\n\n"
            )
        else:
            PROMPT_TEMPLATE += (
                "Use the following pieces of chat history enclosed by triple dash to answer the question at the end "
                "but don't mention you're using it.\n"
                "Chat History:\n"
                "---\n"
                f"{chat_history}\n"
                "---\n\n"
            )
        if user_message:
            PROMPT_TEMPLATE += (
                f"Question: {user_message.content}\n\n"
                "Answer:"
            )
        return PROMPT_TEMPLATE

    @classmethod
    def get_prompt(cls, config, context, system_message, chat_history_messages, user_message):
        # Format the chat history according to the configuration parameter chat_history_formatter
        chat_history_formatter = ChatHistoryFormatterFactory.get_chat_history_formatter(config)
        chat_history = chat_history_formatter.format(system_message, chat_history_messages)
        # Create the prompt using a PROMPT_TEMPLATE and filling it with the following information:
        # - context, if rag_enabled is True
        # - chat_history, for the first message only the system message will be present
        # - user_message, the user question
        prompt_template = Prompt.create_prompt_template(context, chat_history, user_message)
        return PromptTemplate(template=prompt_template, input_variables=["system_message", "context", "chat_history", "user_message"]).format(system_message=system_message.content, context=context, chat_history=chat_history, user_message=user_message.content)
