import os
from providers.provider import LLMProvider
from langchain_ibm import WatsonxLLM

class WatsonXProvider(LLMProvider):
    def create_model(self):
        self.url = self.config["api_url"]
        self.parameters = self.config.get("parameters", {})
        # Retrieve the project ID from the environment variable
        self.project_id = os.getenv("WATSONX_PROJECT_ID")

        self.model = WatsonxLLM(
            model_id=self.config["model"],
            url=self.url,
            project_id=self.project_id,
            params=self.parameters
        )

    def generate(self, prompt):
        print("****************************************************************")
        print("Prompt:")
        print(prompt)
        print("****************************************************************")

        return self.model.invoke(prompt)
