# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from langchain_ollama import ChatOllama

# Create a ChatOllama instance.
# This connects to a local Ollama server.
# You can use any model downloaded in Ollama, e.g., "llama3.1:latest" or "deepseek-r1:8b".
chat: ChatOllama = ChatOllama(model="llama3.1:latest")

# Send the prompt to the model with streaming.
# `stream` returns chunks of the response as they arrive.
for chunk in chat.stream(input="Who is Robinson Crusoe?"):
    print(chunk.content, end="", flush=True)
print("")
