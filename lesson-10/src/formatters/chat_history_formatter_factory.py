from formatters.chat_history_formatter import ChatHistoryFormatter
from formatters.plain_chat_history_formatter import PlainChatHistoryFormatter
from formatters.granite_chat_history_formatter import GraniteChatHistoryFormatter
from formatters.llama2_chat_history_formatter import LLama2ChatHistoryFormatter

DEFAULT_PROMPT_FORMATTER="plain"

class ChatHistoryFormatterFactory:
    @staticmethod
    def get_chat_history_formatter(config) -> ChatHistoryFormatter:
        chat_formatter_type = config.get('prompt_formatter', DEFAULT_PROMPT_FORMATTER)

        if chat_formatter_type == 'plain':
            return PlainChatHistoryFormatter()
        elif chat_formatter_type == 'granite':
            return GraniteChatHistoryFormatter()
        elif chat_formatter_type == 'llama2':
            return LLama2ChatHistoryFormatter()
        else:
            raise ValueError(f"Unknown chat formatter type: {chat_formatter_type}")
