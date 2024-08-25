# Conversation - a Generic ChatBot conversation
#
# This class represents a generic chatbot conversation.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from langchain_community.chat_message_histories import ChatMessageHistory

# This class represents a generic chatbot conversion.
# It contains the chat history of the messages and the cost of each one.
class Conversation:
    def __init__(self, config):
        self.__init(config)

    def __init(self, config):
        # Inizialize the conversation
        self.conversation = ChatMessageHistory()

    def add_message(self, message):
        self.conversation.add_message(message)

    def get_messages(self):
        return self.conversation.messages

    def clear(self):
        self.__init()
