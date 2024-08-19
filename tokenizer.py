from transformers import AutoTokenizer

def main():
    # Nome del modello LLaMA (sostituisci con il modello specifico se necessario)
    model_name = "meta-llama/Meta-Llama-3-8B"  # Sostituisci con il nome corretto del modello LLaMA 3

    # Carica il tokenizer per il modello LLaMA
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Testo da tokenizzare
    text = "Hello, how are you today?"

    # Tokenizzazione del testo
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    # Stampa i risultati
    print("Original Text:", text)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)

if __name__ == "__main__":
    main()