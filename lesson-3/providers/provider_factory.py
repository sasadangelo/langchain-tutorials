from providers.watsonx_provider import WatsonXProvider
from providers.ollama_provider import OllamaProvider
from providers.llamacpp_provider import LLamaCppProvider
from providers.openai_provider import OpenAIProvider

class LLMProviderFactory:
    providers = {
        "llamacpp": LLamaCppProvider,
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
        "watsonx": WatsonXProvider
    }

    @classmethod
    def get_provider(cls, config):
        provider_name = config['provider']
        provider_class = cls.providers.get(provider_name)
        if not provider_class:
            raise ValueError(f"Unsupported provider: {provider_name}")
        return provider_class(config)