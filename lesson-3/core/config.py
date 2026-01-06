# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from enum import Enum
from typing import ClassVar
from pydantic import BaseModel
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict
from pydantic_settings.sources import YamlConfigSettingsSource


class OllamaParameters(BaseModel):
    temperature: float | None = 0.7


class DecodingMethod(str, Enum):
    SAMPLE = "sample"
    GREEDY = "greedy"


class WatsonxParameters(BaseModel):
    decoding_method: str = DecodingMethod.SAMPLE.value
    min_new_tokens: int = 1
    max_new_tokens: int = 500
    temperature: float | None = 0.7


class OpenAIParameters(BaseModel):
    temperature: float | None = 0.7
    max_tokens: int | None = 512


class ProtocolName(str, Enum):
    OLLAMA = "ollama"
    WATSONX = "watsonx"
    OPENAI = "openai"


class OllamaProtocol(BaseModel):
    name: ProtocolName = ProtocolName.OLLAMA
    model: str
    api_url: str = "http://localhost:11434"
    parameters: OllamaParameters = OllamaParameters()


class WatsonxProtocol(BaseModel):
    name: ProtocolName = ProtocolName.WATSONX
    model: str
    api_url: str = "https://eu-de.ml.cloud.ibm.com"
    space_id: str
    parameters: WatsonxParameters


class OpenAIProtocol(BaseModel):
    name: ProtocolName = ProtocolName.OPENAI
    model: str
    api_url: str = "https://api.openai.com/v1"
    parameters: OpenAIParameters = OpenAIParameters()


ProtocolConfig = OllamaProtocol | WatsonxProtocol | OpenAIProtocol


class AppSettings(BaseSettings):
    protocol: ProtocolConfig

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        yaml_file="config.yaml",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Customize settings sources: YAML file only."""
        return (
            YamlConfigSettingsSource(settings_cls),
            init_settings,
        )


# Load settings at module import
settings: AppSettings = AppSettings()  # type: ignore[call-arg]
