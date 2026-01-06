# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from core import settings
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from protocols import LLMProtocolFactory

# Load environment variables
load_dotenv()

# Initialize model based on config
protocol = LLMProtocolFactory.get_protocol()

# Initialize the conversation
conversation = [SystemMessage(content=settings.system_message)]

try:
    while True:
        # Input from the user
        user_input: str = input("You: ")

        # Add the user message to the conversation
        conversation.append(HumanMessage(content=user_input))

        # Get the answer from the model
        ai_response: AIMessage = protocol.invoke(conversation)

        conversation.append(ai_response)

        # Print the AI reply
        print(f"Assistant: {ai_response.content}")
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
