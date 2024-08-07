# Conversation - a Generic ChatBot conversation
#
# This class represents a generic chatbot conversation.
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from langchain.schema import (SystemMessage)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# This class represents a generic chatbot conversion.
# It contains the chat history of the messages and the cost of each one.
class Conversation:
    def __init__(self, config):
        self.__init(config)

    def __init(self, config):
        # Generate text using the model
        system_message = config['system_message']

        # Definition of the prompt template
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_message),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        # Inizialize the conversation memory
        self.memory = ConversationBufferMemory()

    def add_message(self, message):
        self.memory.chat_memory.add_message(message)

    def get_messages(self):
        return self.memory.chat_memory.messages

    def clear(self):
        self.__init()