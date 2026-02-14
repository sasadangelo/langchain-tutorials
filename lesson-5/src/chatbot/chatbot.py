# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import LoggerManager, chatterpy_config
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from protocols import LLMProtocolFactory


class ChatBOT:
    def __init__(self) -> None:
        self._logger = LoggerManager.get_logger(name=self.__class__.__name__)
        self._conversation = ChatMessageHistory()
        # Initialize the model provider according to the configuration file config.yml.
        self._protocol = LLMProtocolFactory.get_protocol()
        # Generate text using the model
        system_message: str = chatterpy_config.system_message
        self._logger.info(f"System Message: {system_message}")
        self._conversation.add_message(message=SystemMessage(content=chatterpy_config.system_message))

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question: str) -> str:
        # Add the user message to the list of users
        self._conversation.add_message(message=HumanMessage(content=question))
        self._logger.debug("********************************************************************************")
        self._logger.debug("Chat History:")
        self._logger.debug(self._conversation)
        self._logger.debug("********************************************************************************")
        # Get the answer from the model
        ai_message: AIMessage = self._protocol.invoke(messages=self._conversation.messages)
        self._conversation.add_message(message=ai_message)
        if isinstance(ai_message.content, list):
            return "\n".join(str(c) for c in ai_message.content)
        return ai_message.content
