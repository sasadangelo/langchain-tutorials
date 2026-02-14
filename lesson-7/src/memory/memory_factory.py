# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from memory import (
    BaseChatMemoryStrategy,
    BufferMemoryStrategy,
    SummaryMemoryStrategy,
    WindowMemoryStrategy,
)
from protocols import LLMProtocolFactory


class MemoryFactory:
    """
    Factory to decide which memory strategy to use based on configuration.
    It returns an instance of a BaseChatMemoryStrategy.
    """

    @staticmethod
    def get_memory() -> BaseChatMemoryStrategy:
        if chatterpy_config.chat_history_memory == "buffer":
            return BufferMemoryStrategy()
        if chatterpy_config.chat_history_memory == "window":
            # Default window size of 10 if not specified
            window_size = (
                chatterpy_config.chat_history_memory_window
                if chatterpy_config.chat_history_memory_window is not None
                else 10
            )
            return WindowMemoryStrategy(window=window_size)
        if chatterpy_config.chat_history_memory == "summary":
            # The summary strategy needs an LLM protocol to perform the summarization
            protocol = LLMProtocolFactory.get_protocol()
            # Assuming provider.model (or the provider itself) follows your LLMProtocol
            return SummaryMemoryStrategy(protocol=protocol)

        raise ValueError(f"Unknown memory strategy type: {chatterpy_config.chat_history_memory}")
