# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import settings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from protocols import LLMProtocolFactory


class ChatBOT:
    def __init__(self):
        self._conversation = ChatMessageHistory()
        # Initialize the model provider according to the configuration file config.yml.
        self._protocol = LLMProtocolFactory.get_protocol()
        # Generate text using the model
        self._conversation.add_message(SystemMessage(content=settings.system_message))

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question: str) -> str:
        # Add the user message to the list of users
        self._conversation.add_message(HumanMessage(content=question))
        # Get the answer from the model
        ai_message: AIMessage = self._protocol.invoke(self._conversation.messages)
        self._conversation.add_message(ai_message)
        return ai_message.content
