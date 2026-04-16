# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage, SystemMessage
from protocols import LLMProtocol, LLMProtocolFactory

# Load environment variables
load_dotenv()

# Initialize model based on config
protocol: LLMProtocol = LLMProtocolFactory.get_protocol()

# Initialize the conversation
conversation: InMemoryChatMessageHistory = ChatMessageHistory()
conversation.add_message(message=SystemMessage(content=chatterpy_config.system_message))

try:
    while True:
        # Input from the user
        user_input: str = input("You: ")

        # Add the user message to the conversation
        conversation.add_message(message=HumanMessage(content=user_input))
        ai_response_chunk: AIMessageChunk | None = None

        # Generate the answer using streaming
        # The response will appear progressively, chunk by chunk
        for chunk in protocol.stream(messages=conversation.messages):
            print(chunk.text, end="", flush=True)
            ai_response_chunk = chunk if ai_response_chunk is None else ai_response_chunk + chunk
        print()  # New line at the end

        if ai_response_chunk is not None:
            ai_response: AIMessage = AIMessage(
                content=ai_response_chunk.content,
                additional_kwargs=ai_response_chunk.additional_kwargs,
                response_metadata=ai_response_chunk.response_metadata,
            )
            conversation.add_message(message=ai_response)
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
