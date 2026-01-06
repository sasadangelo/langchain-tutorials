# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from protocols.protocol import LLMProtocol
from langchain_ollama import ChatOllama
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from core import settings


class OllamaProtocol(LLMProtocol):
    def create_model(self):
        model_name = settings.protocol.model
        self._model = ChatOllama(model=model_name)

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._model.invoke(messages)
