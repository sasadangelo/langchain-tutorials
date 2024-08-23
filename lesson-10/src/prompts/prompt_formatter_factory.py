from prompts.prompt_formatter import PromptFormatter
from prompts.plain_prompt_formatter import PlainPromptFormatter

DEFAULT_PROMPT_FORMATTER="plain"

class PromptFormatterFactory:
    _instance = None

    @staticmethod
    def get_prompt_formatter(config) -> PromptFormatter:
        if PromptFormatterFactory._instance is None:
            prompt_formatter = config.get('prompt_formatter', DEFAULT_PROMPT_FORMATTER)

            if prompt_formatter == 'plain':
                PromptFormatterFactory._instance = PlainPromptFormatter()
            else:
                PromptFormatterFactory._instance = PlainPromptFormatter()
        return PromptFormatterFactory._instance
