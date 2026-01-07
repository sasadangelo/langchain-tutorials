# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from typing import Any

from core import chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama
from protocols.protocol import LLMProtocol

OLLAMA_PARAM_MAP: dict[str, str] = {
    "max_tokens": "num_predict",
    "context_size": "num_ctx",
}


def translate_parameters(
    parameters: dict[str, Any],
    mapping: dict[str, str],
) -> dict[str, Any]:
    """
    Translate semantic config parameters into Ollama-specific parameters.
    Unknown parameters are passed through unchanged.
    """
    return {mapping.get(key, key): value for key, value in parameters.items() if value is not None}


class OllamaProtocol(LLMProtocol):
    def create_protocol(self):
        # Create the model using the specified paremeters
        params = translate_parameters(
            chatterpy_config.protocol.model.parameters,
            OLLAMA_PARAM_MAP,
        )
        self._protocol = ChatOllama(
            model=chatterpy_config.protocol.model.name,
            base_url=chatterpy_config.protocol.api_url,
            **params,
        )

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(messages)
