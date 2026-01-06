# Lesson 2: "Hello LLM" with protocols configuration

In this lesson, we will configure the LLM protocols using the new `config.yaml` configuration file.

Before run one of the tutorials change the directory in the `lesson-1` folder:
```
cd lesson-2
```

## How to run "Hello LLM" with Ollama

Make sure in the `config.yaml` only the following rows are uncommented:

```
protocol:
  name: "ollama"
  model: "llama3.1:latest"
  api_url: http://localhost:11434
```

Type the following command:
```
uv run python3 main.py
```

## How to run "Hello LLM" with WatsonX

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample` file in `.env` and add your IBM Cloud API Key to the `WATSONX_APIKEY` variable.

Make sure in the `config.yaml` only the following rows are uncommented (enter the project id):

```
protocol:
  name: "watsonx"
  model: "ibm/granite-4-h-small"
  api_url: "https://eu-de.ml.cloud.ibm.com"
  space_id: "dd2dd8ef-a711-4919-a61b-b6115becd96a"
  parameters:
    decoding_method: sample
    min_new_tokens: 1
    max_new_tokens: 500
```

Type the following command:

```
uv run python3 main.py
```

## How to run "Hello LLM" with OpenAI

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample` file in `.env` and add your IBM Cloud API Key to the `OPENAI_API_KEY` variable.
You can use also ollama server locally to test the Open AI protocol and, in this case, you don't need the `.env` file.

Make sure in the `config.yaml` only the following rows are uncommented (enter the project id):

```
protocol:
  name: "openai"
  # You can use:
  # - "gpt-3.5-turbo" for ChatGPT 3.5
  # - "gpt-4" for ChatGPT 4
  # - "instructlab/merlinite-7b-lab" for InstructLab and Merlinite model
  model: "llama3.1:latest"
  # You can use:
  # - https://api.openai.com/v1 for ChatGPT
  api_url: "http://localhost:11434/v1"
```

Type the following command:
```
uv run python3 main.py
```
