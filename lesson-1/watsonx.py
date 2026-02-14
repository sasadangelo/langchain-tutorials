# -----------------------------------------------------------------------------
# Copyright (c) 2026 Salvatore D'Angelo, Code4Projects
# Licensed under the MIT License. See LICENSE.md for details.
# -----------------------------------------------------------------------------
import os
from typing import Any

from dotenv import load_dotenv
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_core.messages.ai import AIMessage
from langchain_ibm import ChatWatsonx

# Load the .env file
load_dotenv()

# Specify the WatsonX model parameters
parameters: dict[str, Any] = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.MAX_NEW_TOKENS: 200,
    GenParams.TEMPERATURE: 0.7,
}

# Retrieve the project ID from the environment variable
space_id: str | None = os.getenv("WATSONX_SPACE_ID")

chat: ChatWatsonx = ChatWatsonx(
    model_id="ibm/granite-4-h-small",
    url="https://eu-de.ml.cloud.ibm.com",  # type: ignore[arg-type]  # ChatWatsonx expects SecretStr but accepts str at
    # runtime. The problem is ignored because an URL is not a secret in our opinion.
    space_id=space_id,
    params=parameters,
)
# Send a prompt to the model
response: AIMessage = chat.invoke(input="Who is Robinson Crusoe?")
# Print the model's response
print(response.content)
