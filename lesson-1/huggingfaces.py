from transformers import pipeline

# Specifica il modello e il tokenizer da utilizzare
model_name = "distilgpt2"

# Crea la pipeline per la generazione di testo
llm = pipeline("text-generation", model=model_name, tokenizer=model_name)

# Esegui la generazione di testo con il modello
result = llm("Who is Wolfgang Amadeus Mozart?", max_length=300)

# Stampare il testo generato
print(result[0]["generated_text"])