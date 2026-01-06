# Lesson 3: a simple Chatbot

In this lesson I will show you how to implement a simple Chatbot just reworking a bit the code in the lesson 2.
I assume you already know how you can switch from one provider to another, by default, the Ollama provider is set with the LLama 3 model.
It's important to understand that this chatbot will provide to the LLM only the provided question with no additional context.
If you try to send a followup question related to the first question the Chatbot could have problems to reply.

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-3
uv run python3 chatterpy.py
```
