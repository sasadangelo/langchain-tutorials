# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from protocols.protocol import LLMProtocol


# To use ChatGPT 3.5 set model_name="gpt-3.5-turbo" and omit the parameter openai_api_base
# To use ChatGPT 4 set model_name="gpt-4" and omit the parameter openai_api_base
class OpenAIProtocol(LLMProtocol):
    def create_protocol(self):
        self._protocol = ChatOpenAI(
            model_name=chatterpy_config.protocol.model.name, openai_api_base=chatterpy_config.protocol.api_url
        )

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(messages)
