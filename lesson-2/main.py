# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from dotenv import load_dotenv
from langchain_core.language_models.base import LanguageModelInput
from langchain_core.messages import AIMessage, HumanMessage
from protocols import LLMProtocol, LLMProtocolFactory

# Load environment variables
load_dotenv()

# Initialize model based on config
protocol: LLMProtocol = LLMProtocolFactory.get_protocol()

# Inizialize the message list
messages: LanguageModelInput = [HumanMessage("Who is Robinson Crusoe?")]

# Generate the answer using the model
result: AIMessage = protocol.invoke(messages)
print(result.content)
