import os
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Specify the WatsonX model parameters
parameters = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 100
}

# Retrieve the project ID from the environment variable
project_id = os.getenv("WATSONX_PROJECT_ID")

# Configure the WatsonX LLM model
llm = WatsonxLLM(
    model_id="ibm/granite-13b-chat-v2",
    url="https://eu-de.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters
)

# Run the text generation
result = llm.invoke("Who is Robinson Crusoe?")

# Print the result
print(result)
