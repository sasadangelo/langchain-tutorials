from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Specify the WatsonX model parameters
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 100
}

# Configure the WatsonX LLM model
llm = WatsonxLLM(
    model_id="ibm/granite-13b-chat-v2",
    url="https://us-south.ml.cloud.ibm.com",
    project_id="c189bcc3-b228-4a3d-b6f9-2817c587b178",
    params=parameters
)

# Run the text generation
result = llm.invoke("Who is Robinson Crusoe?")

# Print the result
print(result)
