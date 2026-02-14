# Lesson 7: Memory Management during the conversation

In this lesson we will improve our Chatbot allowing to use different memory strategy. Until lesson 6 the chat history grows indefinitively and this leads to a memory issue when the chat history is larger than the context size. To manage this situation we will implement 3 memory models:

- no management at all
- keep only the recent N messages (windows)
- summary of the conversation

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-7/src
uv run python3 chatterpy_app.py
```
