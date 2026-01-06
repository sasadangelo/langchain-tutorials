# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import chatterpy_config
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from protocols import LLMProtocolFactory

# Load environment variables
load_dotenv()

# Initialize model based on config
protocol = LLMProtocolFactory.get_protocol()

# Initialize the conversation
conversation = ChatMessageHistory()
conversation.add_message(SystemMessage(content=chatterpy_config.system_message))

try:
    while True:
        # Input from the user
        user_input: str = input("You: ")

        # Add the user message to the conversation
        conversation.add_message(HumanMessage(content=user_input))

        # Get the answer from the model
        ai_response: AIMessage = protocol.invoke(conversation.messages)

        conversation.add_message(ai_response)

        # Print the AI reply
        print(f"Assistant: {ai_response.content}")
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
