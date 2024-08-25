# Lesson 4: a simple Chatbot with context

In this lesson I will show you how to implement a simple Chatbot with context just reworking a bit the code in the lesson 3.
I assume you already know how you can switch from one provider to another, by default, the Ollama provider is set with the LLama 3 model.
In this tutorial, the chatbot will always submit to the LLM the user question with the chat history so that the LLM has knowledge of the whole conversation.

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-4
python3 chatterpy.py -c config.yml
```
