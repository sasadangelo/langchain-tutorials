# ChatBOT - the ChaatBOT main class.
#
# This class represents a generic chatbot. It is composed by:
# - a model
# - a chat history
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from providers.provider_factory import LLMProviderFactory
from chatbot.conversation import Conversation
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from prompts.prompt_formatter_factory import PromptFormatterFactory

class ChatBOT:
    def __init__(self, config):
        self.config = config
        self.conversation = Conversation(config)
        # Initialize the model provider according to the configuration file config.yml.
        self.provider = LLMProviderFactory.get_provider(config)
        # Generate text using the model
        system_message = config['system_message']
        self.conversation.add_message(SystemMessage(content=system_message))
        self.prompt_formatter = PromptFormatterFactory.get_prompt_formatter(self.config)

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question):
        # Add the user message to the list of users
        self.conversation.add_message(HumanMessage(content=question))
        # Create the prompt to pass to the model
        prompt = self.prompt_formatter.get_prompt(self.conversation.get_messages())
        # Get the answer from the model
        ai_message = self.provider.generate(prompt)
        self.conversation.add_message(AIMessage(content=ai_message))
        return ai_message
