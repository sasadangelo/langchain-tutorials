# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage


class LLMProtocol:
    def __init__(self):
        self.create_model()

    def create_model(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def invoke(self, message: LanguageModelInput) -> AIMessage:
        raise NotImplementedError("Subclasses should implement this method.")
