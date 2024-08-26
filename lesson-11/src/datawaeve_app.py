import argparse
import yaml
from dotenv import load_dotenv
from datasources.pdf_source import PDFSource
from datawaeve.datawaeve_cli import DataWeaveCLI

def load_environment(env_file):
    load_dotenv(env_file)

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config

# This is the main entry point of the DataWeave command-line interface.
def main():
    parser = argparse.ArgumentParser(description="DataWeave CLI: Populate a vector database with data coming from different sources.")
    parser.add_argument('--config', '-c', type=str, required=True, help='Path to the config file')
    parser.add_argument('--env', '-e', type=str, required=False, default=".env", help='Path to the environment file')
    parser.add_argument('--pdf', type=str, action='append', required=False, help='Specify the path of a PDF file or a folder containing multiple PDF files.')
    parser.add_argument('--wikipedia', type=str, action='append', required=False, help='Specify the URL of a Wikipedia page.')

    args = parser.parse_args()

    # Load environment variables
    load_environment(args.env)
    # Load the configuration file
    config = load_config(args.config)

    # Load data from all the supported data sources
    datawaeve_cli = DataWeaveCLI(config)
    datawaeve_cli.load_pdf_sources(args.pdf) if args.pdf else []
    datawaeve_cli.load_wikipedia_sources(args.wikipedia) if args.wikipedia else []
    datawaeve_cli.process_sources()

if __name__ == "__main__":
    main()