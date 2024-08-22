# ChatBOT - the ChatBOT main class.
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
from langchain_core.messages import AIMessage, HumanMessage

class ChatBOT:
    def __init__(self, config):
        self.config = config
        self.conversation = Conversation(config)
        # Initialize the model provider according to the configuration file config.yml.
        self.provider = LLMProviderFactory.get_provider(config)

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question):
        # Add the user message to the list of users
        user_message = HumanMessage(content=question)
        # Get the answer from the model
        ai_message_text = self.provider.generate(self.conversation.get_chat_history_messages(), user_message)
        ai_message = AIMessage(content=ai_message_text)
        # Save the interaction in the chat history
        self.conversation.save_interaction(user_message, ai_message)
        return ai_message_text
