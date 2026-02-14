# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from protocols import LLMProtocol, LLMProtocolFactory

# Load environment variables
load_dotenv()

# Initialize model based on config
protocol: LLMProtocol = LLMProtocolFactory.get_protocol()

try:
    while True:
        # Input from the user
        user_input: str = input("You: ")

        # Get the answer from the model
        ai_response: AIMessage = protocol.invoke(messages=[HumanMessage(content=user_input)])

        # Print the AI reply
        print(f"Assistant: {ai_response.content}")
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
