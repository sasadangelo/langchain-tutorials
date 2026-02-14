# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from langchain_core.messages.ai import AIMessage
from langchain_ollama import ChatOllama

# Create a ChatOllama instance.
# This connects to a local Ollama server.
# You can use any model downloaded in Ollama, e.g., "llama3.1:latest" or "deepseek-r1:8b".
chat: ChatOllama = ChatOllama(model="llama3.1:latest")

# Send the prompt to the model.
# `invoke` returns a response object with the model's output.
response: AIMessage = chat.invoke(input="Who is Robinson Crusoe?")
# Print the model's reply
print(response.content)
