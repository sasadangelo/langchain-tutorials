from langchain.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryMemory
)
from langchain.memory.chat_memory import BaseChatMemory
from providers.provider_factory import LLMProviderFactory

class MemoryFactory:
    @staticmethod
    def get_memory(config) -> BaseChatMemory:
        memory_type = config.get('chat_history_memory', 'buffer')

        if memory_type == 'buffer':
            return ConversationBufferMemory(return_messages=True)
        elif memory_type == 'window':
            window_size = config.get('chat_history_memory_window', 5)
            return ConversationBufferWindowMemory(k=window_size, return_messages=True)
        elif memory_type == 'summary':
            provider = LLMProviderFactory.get_provider(config)
            return ConversationSummaryMemory(llm=provider.model, return_messages=True)
        else:
            raise ValueError(f"Unknown memory type: {memory_type}")
