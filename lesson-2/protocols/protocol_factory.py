# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import ProtocolName, chatterpy_config
from protocols.ollama_protocol import OllamaProtocol
from protocols.openai_protocol import OpenAIProtocol
from protocols.protocol import LLMProtocol
from protocols.watsonx_protocol import WatsonXProtocol


class LLMProtocolFactory:
    protocols = {
        ProtocolName.OLLAMA: OllamaProtocol,
        ProtocolName.OPENAI: OpenAIProtocol,
        ProtocolName.WATSONX: WatsonXProtocol,
    }

    @classmethod
    def get_protocol(cls) -> LLMProtocol:
        provider_name = chatterpy_config.protocol.name
        provider_class = cls.protocols.get(provider_name)
        if not provider_class:
            raise ValueError(f"Unsupported provider: {provider_name}")
        return provider_class()
