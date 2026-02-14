# Lesson 9: DataWaeve CLI and Qdrant

In this lesson we will introduce the DataWaeve command line. This tool will be used to grab data from different sources (i.e. pdf, wikipedia, etc) and store it in a QDrant vector database. This change will be useful in the next lesson to implement RAG.

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-8/src
python3 chatterpy_app.py
```

## How to run the DataWaeve CLI

To run the datawaeve cli type the following command:

```
cd lesson-8/src
python3 datawaeve_app.py [--pdf <pdf file name>] [--wikipedia <wikipedia url>]
```
