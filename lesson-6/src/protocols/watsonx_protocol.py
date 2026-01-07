# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_ibm import ChatWatsonx
from protocols.protocol import LLMProtocol


class WatsonXProtocol(LLMProtocol):
    def create_protocol(self):
        self._protocol = ChatWatsonx(
            model_id=chatterpy_config.protocol.model.name,
            url=chatterpy_config.protocol.api_url,
            space_id=chatterpy_config.protocol.space_id,
            params=chatterpy_config.protocol.model.parameters,
        )

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(messages)
