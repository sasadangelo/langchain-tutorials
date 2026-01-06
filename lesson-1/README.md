# Lesson-1: Hello LLM

This tutorial show how to ask to LLM the question "Who is Robinson Crusoe?" using the following LLM providers:

* OLLama
* OpenAI
* WatsonX

Before run one of the tutorials change the directory in the `lesson-1` folder:
```
cd lesson-1
```

## How to run "Hello LLM" with Ollama

Type the following command:
```
python3 myollama.py
```

## How to run "Hello LLM" with WatsonX

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample`file in `.env` and add your IBM Cloud API Key to the `WATSONX_APIKEY` variable. Finally, type the following command:
```
python3 watsonx.py
```

## How to run "Hello LLM" with OpenAI

To run the "Hello LLM" with WatsonX you need to copy the `.env_sample`file in `.env` and add your OPENAI API Key to the `OPENAI_API_KEY` variable. If you run a local OpenAI server put a dummy key. Type the following command:
```
python3 myopenai.py
```

## How to run "Hello LLM" with LLama_cpp

Type the following command:
```
python3 myllama_cpp.py
```
