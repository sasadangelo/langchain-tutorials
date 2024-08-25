import argparse
from dotenv import load_dotenv
import yaml
from providers.provider_factory import LLMProviderFactory
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from prompts.prompt_formatter_factory import PromptFormatterFactory

def load_environment(env_file):
    load_dotenv(env_file)

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

# Parse command-line arguments
parser = argparse.ArgumentParser(description='LLM Provider Factory')
parser.add_argument('--config', '-c', type=str, required=True, help='Path to the config file')
parser.add_argument('--env', '-e', type=str, required=False, default=".env", help='Path to the environment file')
args = parser.parse_args()

# Load environment variables
load_environment(args.env)
# Load the configuration file
config = load_config(args.config)

# Initialize model based on config
provider = LLMProviderFactory.get_provider(config)
prompt_formatter = PromptFormatterFactory.get_prompt_formatter(config)
# Generate text using the model
system_message = config['system_message']

# Initialize the conversation
conversation = ChatMessageHistory()
conversation.add_message(SystemMessage(content=system_message))

try:
    while True:
        # Input from the user
        user_input = input("You: ")

        # Add the user message to the conversation
        conversation.add_message(HumanMessage(content=user_input))
        prompt = prompt_formatter.get_prompt(conversation.messages)
        # Get the answer from the model
        ai_response = provider.generate(prompt)

        # Add the AI message to the conversation
        conversation.add_message(AIMessage(content=ai_response))

        # Print the AI reply
        print(f"Assistant: {ai_response}")
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
