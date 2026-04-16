# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from collections.abc import Iterator

from core import LoggerManager, chatterpy_config
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage, SystemMessage
from protocols import LLMProtocol, LLMProtocolFactory


class ChatBOT:
    def __init__(self) -> None:
        self._logger = LoggerManager.get_logger(name=self.__class__.__name__)
        self._conversation = ChatMessageHistory()
        # Initialize the model provider according to the configuration file config.yml.
        self._protocol: LLMProtocol = LLMProtocolFactory.get_protocol()
        # Generate text using the model
        system_message: str = chatterpy_config.system_message
        self._logger.info(f"System Message: {system_message}")
        self._conversation.add_message(message=SystemMessage(content=chatterpy_config.system_message))

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question: str) -> Iterator[AIMessageChunk]:
        # Add the user message to the list of users
        self._conversation.add_message(message=HumanMessage(content=question))
        self._logger.debug("********************************************************************************")
        self._logger.debug("Chat History:")
        self._logger.debug(self._conversation)
        self._logger.debug("********************************************************************************")

        ai_response_chunk: AIMessageChunk | None = None

        # Stream the answer from the model while accumulating the final AIMessage
        for chunk in self._protocol.stream(messages=self._conversation.messages):
            yield chunk
            ai_response_chunk = chunk if ai_response_chunk is None else ai_response_chunk + chunk

        if ai_response_chunk is not None:
            ai_message: AIMessage = AIMessage(
                content=ai_response_chunk.content,
                additional_kwargs=ai_response_chunk.additional_kwargs,
                response_metadata=ai_response_chunk.response_metadata,
            )
            self._conversation.add_message(message=ai_message)
