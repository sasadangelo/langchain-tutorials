import argparse
from dotenv import load_dotenv
import yaml
from providers.provider_factory import LLMProviderFactory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain.memory import ConversationBufferMemory

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
# Generate text using the model
system_message = config['system_message']

# Prompt template definition
prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_message),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Initialize the conversation memory
memory = ConversationBufferMemory()

try:
    while True:
        # Input from the user
        user_input = input("You: ")

        # Add the user message to the conversation
        memory.chat_memory.add_message(HumanMessage(content=user_input))

        # Get the answer from the model
        ai_response = provider.generate(prompt_template, memory.chat_memory.messages)

        # Add the AI message to the conversation
        memory.chat_memory.add_message(AIMessage(content=ai_response))

        # Print the AI reply
        print(f"Assistant: {ai_response}")
except EOFError:
    # Terminate the conversation when the user press CTRL-D
    print("\nBye.")
