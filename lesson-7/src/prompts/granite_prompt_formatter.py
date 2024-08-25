from typing import Union
from langchain.prompts import PromptTemplate
from prompts.prompt_formatter import PromptFormatter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class GranitePromptFormatter(PromptFormatter):
    PROMPT_TEMPLATE = (
    "If available, use the following pieces of context enclosed by triple backquote to answer the question at the end\n"
    "Don't mention the word 'context' in the answer.\n\n"
    "Context:\n"
    "```\n"
    "{context}\n"
    "```\n\n"
    "Question: {user_message}\n"
    "Answer:")

    def get_prompt(self, chat_messages):
        # Split the messages in two parts:
        # - chat_history_message, all the messages but last
        # - user_message, the last message
        chat_history_message = chat_messages[:-1]  # Take all the messages but last
        user_message = chat_messages[-1]           # Take the last message
        chat_history = self.__granite_v2_prompt(chat_history_message)
        return PromptTemplate(template=self.PROMPT_TEMPLATE, input_variables=["context", "chat_history", "user_message"]).format(context=chat_history, user_message=user_message.content)

    # This method creates the Granite v2 prompt for the model starting from a message list like this:
    #
    # [
    #   {"role": "system", "content": system_message},
    #   {"role": "user", "content": user_message},
    #   {"role": "assistant", "content": assistant_message},
    #   {"role": "user", "content": user_message},
    #   {"role": "assistant", "content": assistant_message},
    #   {"role": "user", "content": user_message},
    #   ...
    # ]
    #
    # It returns a string like this:
    #
    # <|system|>
    # {system_message}
    # <|user|>
    # {user_message_1}
    # <|assistant|>
    # {assistant_message_1}
    # <|user|>
    # {user_message_2}
    # <|assistant|>
    # {assistant_message_1}
    # <|user|>
    # {user_message_3}
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
