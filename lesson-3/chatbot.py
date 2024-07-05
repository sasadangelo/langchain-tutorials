import argparse
from dotenv import load_dotenv
import yaml
from providers.provider_factory import LLMProviderFactory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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

# Inizializzazione della lista dei messaggi
# Aggiunta del messaggio di sistema
messages = []
messages.append({"role": "system", "content": system_message})

try:
    while True:
        # Input dell'utente
        user_input = input("You: ")

        # Aggiunta del messaggio dell'utente alla lista dei messaggi
        user_message = {"role": "user", "content": user_input}
        messages.append(user_message)

        # Ottenimento della risposta dal modello
        ai_response = provider.generate(user_input)

        # Aggiunta del messaggio dell'AI alla lista dei messaggi
        ai_message = {"role": "assistant", "content": ai_response}
        messages.append(ai_message)

        # Stampa della risposta dell'AI
        print(f"Assistant: {ai_response}")
except EOFError:
    # Termina la conversazione quando viene premuto CTRL-D
    print("\nBye.")