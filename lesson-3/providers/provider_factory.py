import yaml
from providers.watsonx_provider import WatsonXProvider
from providers.ollama_provider import OllamaProvider
from providers.llamacpp_provider import LLamaCppProvider
from providers.openai_provider import OpenAIProvider
from providers.huggingfaces_provider import HuggingFacesProvider

class LLMProviderFactory:
    providers = {
        "huggingfaces": HuggingFacesProvider,
        "llamacpp": LLamaCppProvider,
        "ollama": OllamaProvider,
        "openai": OpenAIProvider,
        "watsonx": WatsonXProvider
    }

    @classmethod
    def __load_config(cls, config_file):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        return config

    @classmethod
    def get_provider(cls, config_path):
        config = cls.__load_config(config_path)
        provider_name = config['provider']
        provider_class = cls.providers.get(provider_name)
        if not provider_class:
            raise ValueError(f"Unsupported provider: {provider_name}")
        return provider_class(config)