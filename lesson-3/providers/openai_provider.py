from providers.provider import LLMProvider
from langchain_openai import ChatOpenAI

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
class OpenAIProvider(LLMProvider):
    def create_model(self):
        model_name = self.config['model']
        base_url = self.config['base_url']
        self.model = ChatOpenAI(model_name=model_name, openai_api_base=base_url)

    def generate(self, prompt):
        result = self.model.invoke(prompt)
        return result.content
