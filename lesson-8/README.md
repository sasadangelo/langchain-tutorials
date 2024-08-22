# Lesson 8: Memory Management during the conversation

In this lesson we will improve our Chatbot allowing to use different memory strategy. Until lesson 7 the chat history grows indefinitively and this leads to a memory issue when the chat history is larger than the context size. To manage this situation Lang Chai supports different strategy:
- no management at all with ConversationBufferMemory
- keep only the recent N messages (windows) with ConversationBufferWindowMemory

## How to run the Chatbot

To run the chatbot type the following command:

```
cd lesson-8/src
python3 app.py -c config.yml
```
