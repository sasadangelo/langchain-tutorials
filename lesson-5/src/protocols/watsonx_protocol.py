# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import settings
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_ibm import ChatWatsonx
from protocols.protocol import LLMProtocol


class WatsonXProtocol(LLMProtocol):
    def create_model(self):
        parameters = {
            GenParams.DECODING_METHOD: settings.protocol.parameters.decoding_method,
            GenParams.MIN_NEW_TOKENS: settings.protocol.parameters.min_new_tokens,
            GenParams.MAX_NEW_TOKENS: settings.protocol.parameters.max_new_tokens,
            GenParams.TEMPERATURE: settings.protocol.parameters.temperature,
        }

        self._model = ChatWatsonx(
            model_id=settings.protocol.model,
            url=settings.protocol.api_url,
            space_id=settings.protocol.space_id,
            params=parameters,
        )

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._model.invoke(messages)
