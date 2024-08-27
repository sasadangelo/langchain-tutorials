import torch
from transformers import AutoTokenizer
from transformers import AutoModel
from dotenv import load_dotenv

ENV_FILE=".env"

def main():
    load_dotenv(ENV_FILE)

    # Name of the model used from HuggingFaces
    # model_name = "meta-llama/Meta-Llama-3-8B"
    model_name = "distilbert/distilbert-base-uncased"

    # Download the tokenizer:
    # - tokenizer.json
    # - tokenizer_config.json
    # - vocab.txt
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Input question
    text = "Who is bigger a dog or a cat?"

    # Convert the question in token and token IDs
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Print the results
    print("Original Text:", text)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)

    # Convert the token ids vector in PyTorch tensor using the model
    input_ids = torch.tensor([token_ids])
    # Ottieni gli embeddings direttamente dai token IDs
    with torch.no_grad():  # Disable the calculation of the efficiency gradient
        outputs = model(input_ids)
        embeddings = outputs.last_hidden_state

    # Print the embeddings (with positional embedding)
    print("Token IDs:", token_ids)
    print("Embeddings Shape:", embeddings.shape)
    print("Embeddings:", embeddings)

if __name__ == "__main__":
    main()