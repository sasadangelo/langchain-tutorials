import argparse
from dotenv import load_dotenv
import yaml
from providers.provider_factory import LLMProviderFactory

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
prompt = "Who is Robinson Crusoe?"
result = provider.generate(prompt)
print(result)
