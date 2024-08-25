import os
from langchain_community.llms import LlamaCpp

# Define the local Hugging Faces cache directory
cache_dir = os.getenv('TRANSFORMERS_CACHE', default=os.path.join(os.path.expanduser("~"), ".cache/huggingface/transformers"))

# Specify the model path
model_path = cache_dir + "/llama-2-7b-chat-gguf/llama-2-7b-chat.Q2_K.gguf"

llm = LlamaCpp(model_path=model_path, chat_format="llama-2")

output=llm.invoke("Who is Robinson Crusoe?")
print(output)