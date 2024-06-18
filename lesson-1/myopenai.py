from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

output=llm.invoke("Who is Robinson Crusoe?")
print(output)

