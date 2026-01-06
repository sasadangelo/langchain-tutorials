# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
from chatbot.chatbot import ChatBOT
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create a ChatBOT object
chatbot = ChatBOT()

# Print a welcome message for the ChatterPy command-line interface.
print("Welcome to the ChatterPy command-line interface!")
print("Start the conversation (Type 'quit' or press 'CTRL-D' to exit)")


# This is the main entry point of the ChatterPy command-line interface.
# It handles command-line arguments, initializes the ChatBOT, and
# facilitates a conversation with the ChatBOT until the user chooses to exit.
def main():
    try:
        while True:
            # Ask input from the user
            user_message = input("you> ")
            if user_message.lower() == "quit":
                print("\nBye.")
                break

            # Generate the chatbot's response
            response = chatbot.get_answer(user_message)

            # Print the chatbot's response
            print("")
            print("assistant>", response)

    except EOFError:
        # Terminate the conversation
        print("\nBye.")


if __name__ == "__main__":
    # Call the main function when the script is executed.
    main()
