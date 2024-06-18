import os
from llama_cpp import Llama

# Define the local Hugging Faces cache directory
cache_dir = os.getenv('TRANSFORMERS_CACHE', default=os.path.join(os.path.expanduser("~"), ".cache/huggingface/transformers"))

# Specify the model path
model_path = cache_dir + "/llama-2-7b-chat-gguf/llama-2-7b-chat.Q2_K.gguf"

llm = Llama(model_path=model_path)

# Execute the text generation
result = llm("Who is Robinson Crusoe?", max_tokens=100)

# Print the result
print(result['choices'][0]['text'])