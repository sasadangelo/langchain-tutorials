# Lesson 9: RAG implementation

In this lesson we will introduce the RAG implementation. Using the configuration parameter rag_enabled, we can activate the RAG so that a context relative to the
user question is retrieved from QDrant and added to the prompt.

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-9/src
python3 chatterpy_app.py
```

## How to run the DataWaeve CLI

To run the datawaeve cli type the following command:

```
cd lesson-9/src
python3 datawaeve_app.py [--pdf <pdf file name>] [--wikipedia <wikipedia url>]
```
