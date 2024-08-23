from typing import List, Union
from formatters.chat_history_formatter import ChatHistoryFormatter
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# The LLama 2 chat history format is the following:
#
# <s>[INST] <<SYS>>
# {your_system_message}
# <</SYS>>
# {user_message_1}
# [/INST]
# {model_reply_1}
# </s>
# <s>[INST]
# {user_message_2}
# [/INST]
# {model_reply_1}
# </s>
# <s>[INST]
# {user_message_3}
# [/INST]
# </s>
B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
BOS, EOS = "<s>", "</s>"

class LLama2ChatHistoryFormatter(ChatHistoryFormatter):
    def format(self, system_message, chat_history_messages):
        # Concatenate the user message to the chat history to create a context for the LLM
        chat_messages = [system_message] + chat_history_messages
        return self.__llama_v2_prompt(self.__convert_langchainschema_to_dict(chat_messages))

    # This method creates the LLama 2 prompt for the model starting from a message list like this:
    #
    # [
    #   {"role": "system", "content": "<system content>"},
    #   {"role": "user", "content": "<user message>"},
    #   {"role": "assistant", "content": "<assistant message>"},
    #   {"role": "user", "content": "<user message>"},
    #   {"role": "assistant", "content": "<assistant message>"},
    #   {"role": "user", "content": "<user message>"},
    #   ...
    # ]
    def __llama_v2_prompt(self, chat_messages: List[dict]) -> str:
        chat_messages = [
            {
                "role": chat_messages[1]["role"],
                "content": B_SYS + chat_messages[0]["content"] + E_SYS + chat_messages[1]["content"],
            }
        ] + chat_messages[2:]

        messages_list = [
            f"{BOS}{B_INST} {(prompt['content']).strip()} {E_INST} {(answer['content']).strip()} {EOS}"
            for prompt, answer in zip(chat_messages[::2], chat_messages[1::2])
        ]
        messages_list.append(
            f"{BOS}{B_INST} {(chat_messages[-1]['content']).strip()} {E_INST}")
        return "".join(messages_list)

    # This method converts the list:
    # [
    #   SystemMessage,
    #   HumanMessage,
    #   AIMessage,
    #   HumanMessage,
    #   AIMessage,
    #   HumanMessage,
    #   ...
    # ]
    #
    # in a list of dictionary like this:
    #
    # [
    #   {"role": "system", "content": "<system content>"},
    #   {"role": "user", "content": "<user message>"},
    #   {"role": "assistant", "content": "<assistant message>"},
    #   {"role": "user", "content": "<user message>"},
    #   {"role": "assistant", "content": "<assistant message>"},
    #   {"role": "user", "content": "<user message>"},
    #   ...
    # ]
    def __convert_langchainschema_to_dict(self, messages: List[Union[SystemMessage, HumanMessage, AIMessage]]) -> List[dict]:
        return [{"role": self.__get_role(message), "content": message.content} for message in messages]

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
