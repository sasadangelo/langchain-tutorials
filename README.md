# Langchain tutorials

These tutorials will help you to build, step by step, a chatbot using Large Languages Models (LLM) and Lanch Chain. Here the list of lessons:

* [Lesson 1: Hello LLM](lesson-1/README.md)
* [Lesson 2: Hello LLM with providers configuration](lesson-2/README.md)
* [Lesson 3: a simple Chatbot](lesson-3/README.md)
* [Lesson 4: a simple Chatbot with Context](lesson-4/README.md)
* [Lesson 5: just a few improvements](lesson-5/README.md)
* [Lesson 6: an Object Oriented ChatBOT with Lang Chain](lesson-6/README.md)
* [Lesson 7: Configure generation parameters](lesson-7/README.md)
* [Lesson 8: Memory Management during the conversation](lesson-8/README.md)
* [Lesson 9: DataWaeve CLI and Qdrant](lesson-9/README.md)
* [Lesson 10: RAG implementation](lesson-10/README.md)

## Prerequisites

### How to install Python 3

To run the tutorials you need Python 3 installed on your machine. On Mac you can simply type:

```
brew install python3
```

### How to setup Ollama

To run the tutorials you need to install ollama cli:
```
brew install ollama
```

Then, you should download the LLM **llama3** model:
```
ollama pull llama3
```

This commandwill download the model in `~/.ollama`folder. You can start the ollama server with the command:
```
ollama serve
```

In another terminal you can list the downloaded model using the commands:
```
ollama list
```

### Clone the LangChain-Tutorials repository

To run the tutorials you need to clone the `langchain-tutorials` repository in a `<workspace>` folder:
```
cd <workspace>
git clone https://github.com/sasadangelo/langchain-tutorials
cd langchain-tutorials
```

## How to run the tutorials

To run the tutorials do the following steps:

1. Create and activate the Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

2. Install the dependencies
```
pip3 install -r requirements.txt
```

3. Run the tutorial following the instructions in each lesson
