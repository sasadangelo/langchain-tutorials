import random
import string
from typing import Dict, Optional
from jinja2 import Environment, FileSystemLoader
from langchain.prompts.prompt import PromptTemplate

def remove_empty_lines(value: str) -> str:
    return "\n".join([line for line in value.splitlines() if line.strip()])

def get_prompt_template_from_jinja2(
    prompt_path: str,
    prompt_name: str,
    input_variables: Dict[str, str],
    jinja2_placeholders: Dict[str, str]
) -> str:
    """
    Loads a .txt file as a Jinja2 template and converts it into a LangChain PromptTemplate.

    Parameters:
        prompt_path: Path to the prompt.
        prompt_name: Filename of the prompt, including its extension.
        jinja2_placeholders: A dictionary of placeholders to be replaced in the Jinja2 template.
    Returns:
        A formatted prompt string with placeholders replaced.
    """
    env = Environment(loader=FileSystemLoader(prompt_path))
    template = env.get_template(prompt_name)
    jinja2_placeholders = jinja2_placeholders or {}
    prompt_string = remove_empty_lines(template.render(jinja2_placeholders))
    prompt_template = PromptTemplate(input_variables=["system_message", "user_message", "ai_message"], template=prompt_string)
    return prompt_template

def generate_random_ai_message(length: int = 50) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    SYSTEM_MESSAGE = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.
If you don't know the answer to a question, please don't share false information."""

    START_TEMPLATE_PATH = "prompts"
    START_TEMPLATE_NAME = "llama2_prompt_template.j2"

    start_conversation_template = get_prompt_template_from_jinja2(
        prompt_path=START_TEMPLATE_PATH,
        prompt_name=START_TEMPLATE_NAME,
        input_variables=["system_message", "user_message", "ai_message"],
        jinja2_placeholders={"system_message": "{system_message}", "user_message": "{user_message}", "ai_message": "{ai_message}"}
    )

    conversation_template = get_prompt_template_from_jinja2(
        prompt_path=START_TEMPLATE_PATH,
        prompt_name=START_TEMPLATE_NAME,
        input_variables=["user_message", "ai_message"],
        jinja2_placeholders={"system_message": None, "user_message": "{user_message}", "ai_message": "{ai_message}"}
    )

    # First user and ai conversation
    user_message = input("User:")
    # Generate a random reply from the AI
    ai_message = generate_random_ai_message()
    formatted_conversation = start_conversation_template.format(system_message=SYSTEM_MESSAGE, user_message=user_message, ai_message=ai_message)
    print(formatted_conversation)

    # Conversation loop
    while True:
        try:
            # Prendi input dall'utente
            user_message = input("User: ")
            # Genera una risposta casuale dall'AI
            ai_message = generate_random_ai_message()
            # Stampa la conversazione formattata
            formatted_conversation = conversation_template.format(user_message=user_message, ai_message=ai_message)
            print(formatted_conversation)
        except EOFError:
            print("Ending chat. Goodbye!")
            break

if __name__ == "__main__":
    main()