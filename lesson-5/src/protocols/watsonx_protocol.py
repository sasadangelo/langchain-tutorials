# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import LoggerManager, chatterpy_config
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage
from langchain_ibm import ChatWatsonx
from protocols.protocol import LLMProtocol


class WatsonXProtocol(LLMProtocol):
    _logger = LoggerManager.get_logger(name=__name__)

    def create_protocol(self) -> None:
        model: str = chatterpy_config.protocol.model.name
        base_url: str = chatterpy_config.protocol.api_url
        self._logger.info(f"WatsonX protocol: model={model} - url={base_url}")
        self._protocol = ChatWatsonx(
            model_id=model,
            url=base_url,  # type: ignore[arg-type]  # ChatWatsonx expects SecretStr but
            # accepts str at runtime. The problem is ignored because an URL is not a secret in our opinion.
            space_id=chatterpy_config.protocol.space_id,
            params=chatterpy_config.protocol.model.parameters,
        )

    def invoke(self, messages: LanguageModelInput) -> AIMessage:
        return self._protocol.invoke(input=messages)
