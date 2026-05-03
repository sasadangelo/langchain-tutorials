# Lesson 11: Introduction to Session Management

In this lesson we introduce the concept of **Session** to manage conversations. Each conversation is now associated with a unique session ID, preparing the architecture for future multi-conversation support.

## What's New in Lesson 11

### Session Class

A new `Session` class has been introduced that:

- Generates a unique session ID (UUID) for each conversation
- Encapsulates the `Conversation` object
- Provides a foundation for future multi-conversation management

### Key Changes

1. **New Session Class** (`chatbot/session.py`):

   - Manages a conversation with a unique identifier
   - Automatically generates a UUID if no session ID is provided
   - Logs session creation for tracking purposes

2. **Updated ChatBOT Class**:

   - Now uses `Session` instead of directly managing `Conversation`
   - Provides `get_session_id()` method to retrieve the current session ID
   - All conversation operations are now accessed through the session

3. **UI Updates**:
   - CLI mode displays the session ID at startup
   - GUI mode shows the session ID in the sidebar
   - Session ID is logged for debugging and tracking

## Architecture

```
ChatBOT
  └── Session (with unique ID)
        └── Conversation
              └── Memory Strategy
```

This architecture prepares the codebase for Lesson 12, where we will implement support for multiple conversations per user.

## Key Features

- **Interactive Chat Interface**: A clean, user-friendly chat interface built with Streamlit
- **Real-time Responses**: The chatbot responds to user queries in real-time with a typing indicator
- **Conversation History**: All messages are displayed in the chat window, maintaining the conversation context
- **Clear Conversation**: A sidebar button allows users to clear the conversation and start fresh
- **Session Management**: Each conversation has a unique session ID displayed in both CLI and GUI modes
- **Session State**: The chatbot state is maintained across interactions using Streamlit's session state

## How to run the Chatbot

To run the chatbot in UI mode, type the following command:

```
cd lesson-11/src
uv run streamlit run chatterpy_gui.py
```

To run the chatbot in text mode (CLI), type the following command:

```
cd lesson-11/src
uv run python3 chatterpy_app.py
```

## How to run the DataWaeve CLI

To run the datawaeve cli type the following command:

```
cd lesson-11/src
python3 datawaeve_app.py [--pdf <pdf file name>] [--wikipedia <wikipedia url>]
```

## Session ID Usage

The session ID is:

- Automatically generated when a ChatBOT instance is created
- Displayed at startup in CLI mode
- Shown in the sidebar in GUI mode
- Logged for debugging and tracking purposes
- Unique for each conversation instance

In future lessons, this session ID will be used to:

- Support multiple concurrent conversations
- Persist conversation history
- Enable conversation switching and management
