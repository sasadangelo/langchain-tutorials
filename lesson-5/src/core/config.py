# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from enum import Enum
from typing import ClassVar

from pydantic import BaseModel
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict
from pydantic_settings.sources import YamlConfigSettingsSource


class ProtocolName(str, Enum):
    OLLAMA = "ollama"
    OPENAI = "openai"
    WATSONX = "watsonx"


class ModelConfig(BaseModel):
    name: str
    parameters: dict[str, object] = {}


class ProtocolConfig(BaseModel):
    name: ProtocolName
    api_url: str
    model: ModelConfig
    space_id: str | None = None  # only watsonx


class AppSettings(BaseSettings):
    protocol: ProtocolConfig
    system_message: str

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
            env_settings,
            init_settings,
        )


# Load settings at module import
chatterpy_config: AppSettings = AppSettings()  # type: ignore[call-arg]
