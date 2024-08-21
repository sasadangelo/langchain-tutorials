from providers.provider import LLMProvider
from langchain_ibm import WatsonxLLM

class WatsonXProvider(LLMProvider):
    def create_model(self):
        self.url = self.config.get("api_url")
        self.project_id = self.config.get("project_id")
        self.parameters = self.config.get("parameters", {})

        self.model = WatsonxLLM(
            model_id=self.config["model"],
            url=self.url,
            project_id=self.project_id,
            params=self.parameters
        )

    def generate(self, prompt_template, messages):
        formatted_prompt = self.__format_messages(messages)

        # Generate the prompt with the template
        # formatted_prompt = prompt_template.format(messages=messages)
        print("****************************************************************")
        print("Chat History + Question:")
        print(formatted_prompt)
        print("****************************************************************")

        return self.model.invoke(formatted_prompt)

    # Convert the prompt messages list format
    def __format_messages(self, messages) -> str:
        # Construct the prompt by iterating through the messages
        prompt = []
        for message in messages:
            print(message)
            if message["role"] == "system":
                # Add the system message
                prompt.append("<|system|>")
                prompt.append(message['content'])
            elif message["role"] == "user":
                # Add user question
                prompt.append("<|user|>")
                prompt.append(message['content'])
            elif message["role"] == "assistant":
                # Add AI reply
                prompt.append("<|assistant|>")
                prompt.append(message['content'])

        return '\n'.join(prompt)