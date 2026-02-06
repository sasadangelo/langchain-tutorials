# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the .env file for environment variables like API keys
load_dotenv()

# Create a model instance.
# You can use various models:
# - OpenAI cloud models: "gpt-3.5-turbo", "gpt-4"
# - Local OpenAI-compatible servers:
#     * LM Studio
#     * Ollama
#     * llama.cpp server
#     * MPT-Chat local server
#     * Any other server that supports the OpenAI REST API spec
chat = ChatOpenAI(model="llama3.1:latest", base_url="http://localhost:11434/v1")
# Send a prompt to the model
response = chat.invoke("Who is Robinson Crusoe?")
# Print the model's response
print(response.content)
