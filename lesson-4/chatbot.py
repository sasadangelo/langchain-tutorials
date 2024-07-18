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

# Definition of the prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=system_message),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

# Inizialize the conversation memory
memory = ConversationBufferMemory()

try:
    while True:
        # Ask input from the user
        user_message = input("You: ")

        # Add the user message to the list of users
        memory.chat_memory.add_message(HumanMessage(content=user_message))

        # Generate the prompt from the template
        formatted_prompt = prompt_template.format(messages=memory.chat_memory.messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")

        # Get the answer from the model
        ai_message = provider.generate(formatted_prompt)

        # Add the AI message to the chat history
        memory.chat_memory.add_message(AIMessage(content=ai_message))

        # Print the AI answer
        print(f"Assistant: {ai_message}")
except EOFError:
    # Terminate the conversation
    print("\nBye.")
