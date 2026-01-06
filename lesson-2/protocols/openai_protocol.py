# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from protocols.protocol import LLMProtocol
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
from langchain_core.language_models.base import LanguageModelInput
from core import settings


# To use ChatGPT 3.5 set model_name="gpt-3.5-turbo" and omit the parameter openai_api_base
# To use ChatGPT 4 set model_name="gpt-4" and omit the parameter openai_api_base
class OpenAIProtocol(LLMProtocol):
    def create_model(self):
        model_name = settings.protocol.model
        api_url = settings.protocol.api_url
        self._model = ChatOpenAI(model_name=model_name, openai_api_base=api_url)

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._model.invoke(messages)
