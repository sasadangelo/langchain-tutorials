# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import LoggerManager, chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama
from protocols.protocol import LLMProtocol


class OllamaProtocol(LLMProtocol):
    _logger = LoggerManager.get_logger(name=__name__)

    def create_protocol(self) -> None:
        model: str = chatterpy_config.protocol.model.name
        base_url: str = chatterpy_config.protocol.api_url
        self._logger.info(f"Ollama protocol: model={model} - url={base_url}")
        self._protocol = ChatOllama(model=model, base_url=base_url)

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(input=messages)
