# ChatBOT - the ChaatBOT main class.
#
# This class represents a generic chatbot. It is composed by:
# - a model
# - a chat history
#
# Copyright (C) 2023 Salvatore D'Angelo
# Maintainer: Salvatore D'Angelo sasadangelo@gmail.com
#
# SPDX-License-Identifier: MIT
from providers.provider_factory import LLMProviderFactory
from chatbot.conversation import Conversation
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class ChatBOT:
    def __init__(self, config):
        self.config = config
        # self.model = LlamaModel(0.0)
        self.conversation = Conversation(config)
        # Initialize the model provider according to the configuration file config.yml.
        self.provider = LLMProviderFactory.get_provider(config)
        # Generate text using the model
        system_message = config['system_message']
        # Definition of the prompt template
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_message),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

    # Once the user insert the question, this method is called to generate the answer.
    def get_answer(self, question):
        # Add the user message to the list of users
        self.conversation.add_message(HumanMessage(content=question))

        # Generate the prompt from the template
        formatted_prompt = self.prompt_template.format(messages=self.conversation.get_messages())
        if self.config['debug'] == True:
            print("****************************************************************")
            print("DEBUG.                                                          ")
            print("Chat History + Question:                                        ")
            print(formatted_prompt)
            print("****************************************************************")

        # Add the user message to the list of users
        # self.conversation.add_message(HumanMessage(content=formatted_prompt))
        # Get the answer from the model
        ai_message = self.provider.generate(formatted_prompt)
        self.conversation.add_message(AIMessage(content=ai_message))
        return ai_message