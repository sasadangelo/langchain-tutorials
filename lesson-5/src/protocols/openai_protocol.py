# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import LoggerManager, chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from protocols.protocol import LLMProtocol


# To use ChatGPT 3.5 set protocol.name="gpt-3.5-turbo" and protocol.api_url="https://api.openai.com/v1" in the
# config.yml. To use ChatGPT 4 set protocol.name="gpt-4" and protocol.api_url="https://api.openai.com/v1" in the
# config.yml
class OpenAIProtocol(LLMProtocol):
    _logger = LoggerManager.get_logger(name=__name__)

    def create_protocol(self):
        model: str = chatterpy_config.protocol.model.name
        base_url: str = chatterpy_config.protocol.api_url
        self._logger.info(f"OpenAI protocol: model={model} - url={base_url}")
        self._protocol = ChatOpenAI(model=model, base_url=base_url)

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(input=messages)
