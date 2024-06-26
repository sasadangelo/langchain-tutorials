from providers.provider import LLMProvider
from langchain_ibm import WatsonxLLM

class WatsonXProvider(LLMProvider):
    def create_model(self):
        self.url = self.config.get("api_url")
        self.project_id = self.config.get("project_id")
        parameters = self.config.get("parameters", {})
        
        self.model = WatsonxLLM(
            model_id=self.config["model"],
            url=self.url,
            project_id=self.project_id,
            params=parameters
        )

    def generate(self, prompt):
        return self.model.invoke(prompt)