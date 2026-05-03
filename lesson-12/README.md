# Lesson 12: Multiple Sessions Management

In this lesson we introduce multiple sessions management. Users can now create, switch between, and delete multiple chat sessions, each maintaining its own conversation history.

## New Features

### SessionManager Class

A new `SessionManager` class has been added to manage multiple chat sessions:

- Create new sessions with unique IDs
- Switch between sessions
- Delete sessions (with protection against deleting the last session)
- List all available sessions
- Track the current active session

### CLI Commands

The text-based interface now supports the following commands:

- `/new` - Create a new session and switch to it
- `/list` - List all available sessions (current session marked with →)
- `/switch` - Switch to a different session (interactive selection)
- `/delete` - Delete a session (interactive selection with confirmation)
- `/clear` - Clear the current conversation history
- `quit` - Exit the application

### GUI Features

The Streamlit interface now includes:

- **Session sidebar**: Shows all sessions with the current one highlighted
- **New Session button**: Create a new session instantly
- **Session switching**: Click on any session to switch to it
- **Delete session**: Delete any session (except if it's the only one)
- **Clear Conversation**: Clears only the current session's history

## How to run the Chatbot

To run the chatbot in UI mode, type the following command:

```bash
cd lesson-12/src
streamlit run chatterpy_gui.py
```

To run the chatbot in text mode, type the following command:

```bash
cd lesson-12/src
python3 chatterpy_app.py
```

### CLI Usage Examples

```
you> /new
✓ Created and switched to new session: 12345678-1234-5678-1234-567812345678

you> /list
Sessions (2):
  → 12345678-1234-5678-1234-567812345678
    87654321-4321-8765-4321-876543218765

you> /switch
Available sessions:
  1. → 12345678-1234-5678-1234-567812345678
  2.   87654321-4321-8765-4321-876543218765
Enter session number to switch to (or press Enter to cancel): 2
✓ Switched to session: 87654321-4321-8765-4321-876543218765

you> /clear
✓ Conversation cleared

you> /delete
Available sessions:
  1.   12345678-1234-5678-1234-567812345678
  2. → 87654321-4321-8765-4321-876543218765
Enter session number to delete (or press Enter to cancel): 1
Delete session 12345678-1234-5678-1234-567812345678? (y/N): y
✓ Deleted session: 12345678-1234-5678-1234-567812345678
```

## How to run the DataWaeve CLI

To run the datawaeve cli type the following command:

```bash
cd lesson-12/src
python3 datawaeve_app.py [--pdf <pdf file name>] [--wikipedia <wikipedia url>]
```

## Architecture Changes

### ChatBOT Class

- Now uses `SessionManager` instead of managing a single `Session`
- Added methods: `create_session()`, `delete_session()`, `switch_session()`, `list_sessions()`, `get_session_count()`
- All conversation operations now work on the current active session

### Session Management

- Each session maintains its own conversation history
- Sessions are identified by UUID
- The system always maintains at least one session
- Deleting the current session automatically switches to another available session
