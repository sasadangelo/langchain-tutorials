import torch
from transformers import AutoTokenizer
from transformers import AutoModel
from dotenv import load_dotenv
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

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
        embeddings = outputs.last_hidden_state.squeeze(0)

    # Print the embeddings (with positional embedding)
    print("Token IDs:", token_ids)
    print("Embeddings Shape:", embeddings.shape)
    print("Embeddings:", embeddings)

    # Convert embeddings to numpy array
    embeddings_np = embeddings.numpy()

    # Determine a suitable perplexity value
    num_samples = embeddings_np.shape[0]
    perplexity = min(30, num_samples - 1)  # perplexity must be less than num_samples

    # Reduce dimensionality with t-SNE
    tsne = TSNE(n_components=3, perplexity=perplexity, random_state=0)
    embeddings_3d = tsne.fit_transform(embeddings_np)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each token embedding
    for i, token in enumerate(tokens):
        ax.scatter(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2], label=token)

    # Adding labels to the points
    for i, token in enumerate(tokens):
        ax.text(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2], token)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title('3D t-SNE visualization of token embeddings')
    plt.show()

if __name__ == "__main__":
    main()