# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from collections.abc import Iterator

from core import chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage, AIMessageChunk
from langchain_ollama import ChatOllama
from protocols.protocol import LLMProtocol


class OllamaProtocol(LLMProtocol):
    def create_protocol(self) -> None:
        self._protocol = ChatOllama(model=chatterpy_config.protocol.model.name)

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(input=messages)

    def stream(self, messages: LanguageModelInput) -> Iterator[AIMessageChunk]:
        return self._protocol.stream(input=messages)
