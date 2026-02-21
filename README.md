# LangChain Tutorials

These tutorials guide you step by step in building a **RAG Chatbot** using **Large Language Models (LLMs)** and **LangChain**.

## Lessons

- [Lesson 1: Hello LLM](lesson-1/README.md)
- [Lesson 2: Hello LLM with Protocols Configuration](lesson-2/README.md)
- [Lesson 3: A Simple Chatbot](lesson-3/README.md)
- [Lesson 4: A Simple Chatbot with Context](lesson-4/README.md)
- [Lesson 5: An Object-Oriented Chatbot with LangChain](lesson-5/README.md)
- [Lesson 6: Configure Generation Parameters](lesson-6/README.md)
- [Lesson 7: Memory Management During the Conversation](lesson-7/README.md)
- [Lesson 8: DataWeave CLI and Qdrant](lesson-8/README.md)
- [Lesson 9: RAG Implementation](lesson-9/README.md)
- [Lesson 10: Add UI Interface with Streamlit](lesson-10/README.md)

---

## Prerequisites

### Python 3 (version 3.12)

To run the tutorials, you need **Python 3** installed on your machine. On Mac:

```bash
brew install python3
```

## uv Package Manager

You also need the uv package manager installed. On Mac:

```bash
brew install uv
```

## Setup Ollama

To run the tutorials with the Ollama provider, install the Ollama CLI:

```bash
brew install ollama
```

## Start the Ollama server:

```bash
ollama serve
```

In another terminal, download the LLM llama3.1 model:

```bash
ollama pull llama3.1
```

List the downloaded models:

```bash
ollama list
```

## Clone the Repository

Clone this repository in your <workspace> folder:

```bash
cd <workspace>
git clone https://github.com/sasadangelo/langchain-tutorials
cd langchain-tutorials
```

## Running the Tutorials

Install dependencies:

```bash
uv sync
```

Follow the instructions in each lesson to run the tutorials.
