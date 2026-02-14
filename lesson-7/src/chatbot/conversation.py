# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from memory import BaseChatMemoryStrategy, MemoryFactory


# This class represents a generic chatbot conversion.
# It contains the chat history of the messages and the cost of each one.
class Conversation:
    def __init__(self, config):
        self.__init(config)

    def __init(self, config):
        # Inizialize the conversation
        self.conversation: BaseChatMemoryStrategy = MemoryFactory.get_memory()

    def save_interaction(self, user_message, ai_message):
        self.conversation.save_context({"input": user_message.content}, {"output": ai_message.content})

    def get_chat_history_messages(self):
        return self.conversation.load_memory_variables({}).get("history", "")
