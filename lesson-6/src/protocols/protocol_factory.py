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
        protocol_name = chatterpy_config.protocol.name
        protocol_class = cls.protocols.get(protocol_name)
        if not protocol_class:
            raise ValueError(f"Unsupported provider: {protocol_name}")
        return protocol_class()
