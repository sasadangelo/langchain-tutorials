# Lesson 2: "Hello LLM" with providers configuration

In this lesson, we will configure the LLM provider using the new `config.yaml`configuration file.

Before run one of the tutorials change the directory in the `lesson-1` folder:
```
cd lesson-2
```

## How to run "Hello LLM" with Ollama

Make sure in the `config.yml` only the following rows are uncommented:

```
provider: "ollama"
model: "llama3"
```

Type the following command:
```
python3 main.py
```

## How to run "Hello LLM" with WatsonX

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample` file in `.env` and add your IBM Cloud API Key to the `WATSONX_APIKEY` variable. 

Make sure in the `config.yml` only the following rows are uncommented (enter the project id):
```
provider: "watsonx"
model: "ibm/granite-13b-chat-v2"
project_id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
api_url: "https://us-south.ml.cloud.ibm.com"
parameters:
 decoding_method: greedy
 min_new_tokens: 1
 max_new_tokens: 500
```

Type the following command:
```
python3 main.py
```

## How to run "Hello LLM" with OpenAI

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample`file in `.env` and add your IBM Cloud API Key to the `OPENAI_API_KEY` variable. 

Make sure in the `config.yml` only the following rows are uncommented (enter the project id):
```
provider: "openai"
model: "gpt-3.5-turbo"
```

Type the following command:
```
python3 main.py
```

## How to run "Hello LLM" with LLama_cpp

Make sure in the `config.yml` only the following rows are uncommented (enter the project id):
```
provider: "llamacpp"
model: "llama-2-7b-chat-gguf"
transformers_path: "~/.cache/huggingface/transformers"
model_path: "llama-2-7b-chat-gguf/llama-2-7b-chat.Q2_K.gguf"
chat_format: "llama-2"
```

Type the following command:
```
python3 main.py
```
