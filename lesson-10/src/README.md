# Lesson 10: Add UI interface with Streamlit

In this lesson we will introduce a UI interface for our chatbot. We will use Streamlit to create easily a UI for prototype purposes.

Streamlit is an open-source Python framework that makes it easy to create and share beautiful, custom web apps for machine learning and data science. With just a few lines of code, you can turn data scripts into interactive web applications.

## Key Features of the GUI

The GUI implementation includes:

- **Interactive Chat Interface**: A clean, user-friendly chat interface built with Streamlit
- **Real-time Responses**: The chatbot responds to user queries in real-time with a typing indicator
- **Conversation History**: All messages are displayed in the chat window, maintaining the conversation context
- **Clear Conversation**: A sidebar button allows users to clear the conversation and start fresh
- **Session Management**: The chatbot state is maintained across interactions using Streamlit's session state

## How to run the Chatbot

To run the chatbot in UI mode, type the following command:

```
cd lesson-10/src
streamlit run chatterpy_gui.py
```

To run the chatbot in text mode (CLI), type the following command:

```
cd lesson-10/src
uv run python3 chatterpy_app.py
```

## How to run the DataWaeve CLI

To run the datawaeve cli type the following command:

```
cd lesson-10/src
python3 datawaeve_app.py -c config.yml [--pdf <pdf file name>] [--wikipedia <wikipedia url>]
```

## Architecture

The GUI is implemented using a modular architecture:

- **chatterpy_gui.py**: Main entry point for the Streamlit application
- **gui/page.py**: Abstract base class for pages
- **gui/chatbot_page.py**: Implementation of the chatbot page with chat interface
- **ChatBotApp**: Singleton class that manages the application and page navigation

This architecture allows for easy extension with additional pages in the future.
