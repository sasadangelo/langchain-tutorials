import wikipediaapi
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def get_wikipedia_text(page_title):
    user_agent="DataWaeve CLI"
    wiki_wiki = wikipediaapi.Wikipedia(user_agent, 'en')
    page = wiki_wiki.page(page_title)
    return page.text

def get_word_embeddings(text, model, tokenizer, max_tokens=10):
    tokens = tokenizer.tokenize(text)
    tokens = tokens[:max_tokens]  # Limita a max_tokens
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Convert token IDs to tensor
    input_ids = torch.tensor([token_ids])

    with torch.no_grad():
        outputs = model(input_ids)
        embeddings = outputs.last_hidden_state.squeeze().numpy()  # Shape: [seq_len, hidden_dim]

    return tokens, embeddings

def main():
    model_name = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Get text from Wikipedia pages
    titles = ["Despicable_Me_4"]
    texts = [get_wikipedia_text(title) for title in titles]

    all_tokens = []
    all_embeddings = []

    # Get word embeddings for each page
    for text in texts:
        tokens, embeddings = get_word_embeddings(text, model, tokenizer, max_tokens=50)
        all_tokens.extend(tokens)
        all_embeddings.append(embeddings)

    # Flatten embeddings for t-SNE
    all_embeddings_np = np.vstack(all_embeddings)

    # Reduce dimensionality with t-SNE
    tsne = TSNE(n_components=3, random_state=0)
    embeddings_3d = tsne.fit_transform(all_embeddings_np)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each token embedding
    for i, token in enumerate(all_tokens):
        ax.scatter(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2])
        ax.text(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2], token)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title('3D t-SNE visualization of word embeddings')
    plt.show()

if __name__ == "__main__":
    main()
