from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Make sure you have a Python 3 virtual environment active:
# $ source venv/bin/activate
#
# Make sure you installed the following dependencies:
# $ (venv) pip3 install llama_cpp_python
# $ (venv) pip3 install sse_starlette
# $ (venv) pip3 install starlette_context
# $ (venv) pip3 install pydantic_settings
# $ (venv) pip3 install fastapi
#
# Then run the llama.cpp server with the input mode:
# $ (venv) python3 -m llama_cpp.server --model <GGUF model path>

# To use ChatGPT 3.5 set model_name="gpt-3.5-turbo" and omit the parameter openai_api_base
# To use ChatGPT 4 set model_name="gpt-4" and omit the parameter openai_api_base
llm = ChatOpenAI(model_name="llama-2-7b-chat",
                openai_api_base="http://localhost:8000/v1")
response=llm.invoke("Who is Robinson Crusoe?")
print(response.content)

