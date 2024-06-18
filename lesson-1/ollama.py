from langchain_community.llms import Ollama

# Make sure you have installed Ollama on your machine and then run the commands:
# $ ollama pull llama3
# $ ollama run llama3
llm = Ollama(model="llama3")

# You can use other models like, for example, instructlab/granite-7b-lab from IBM
# llm = Ollama(model="instructlab/granite-7b-lab")

output=llm.invoke("Who is Robinson Crusoe?")
print(output)
