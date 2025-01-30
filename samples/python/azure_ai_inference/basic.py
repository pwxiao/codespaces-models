"""This sample demonstrates a basic call to the chat completion API.
It is leveraging your endpoint and key. The call is synchronous."""

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

# By using the Azure AI Inference SDK, you can easily experiment with different models
# by modifying the value of `model_name` in the code below. The following models are
# available in the GitHub Models service:
#
# AI21 Labs: AI21-Jamba-Instruct
# Cohere: Cohere-command-r, Cohere-command-r-plus
# Meta: Meta-Llama-3-70B-Instruct, Meta-Llama-3-8B-Instruct, Meta-Llama-3.1-405B-Instruct, Meta-Llama-3.1-70B-Instruct, Meta-Llama-3.1-8B-Instruct
# Mistral AI: Mistral-large, Mistral-large-2407, Mistral-Nemo, Mistral-small
# Azure OpenAI: gpt-4o-mini, gpt-4o
# Microsoft: Phi-3-medium-128k-instruct, Phi-3-medium-4k-instruct, Phi-3-mini-128k-instruct, Phi-3-mini-4k-instruct, Phi-3-small-128k-instruct, Phi-3-small-8k-instruct
model_name = "gpt-4o-mini"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# response = client.complete(
#     messages=[

#         UserMessage(content="中国的首都在哪"),
#     ],
#     model=model_name,

#     # Optional parameters
#     temperature=1.,
#     max_tokens=1000,
#     top_p=1.    
# )
messages = [
            SystemMessage(content="You are a helpful assistant.")
]
while True:
    s = input("问：")
    messages.append(UserMessage(content=s))
    response = client.complete(
        messages,
        model= "gpt-4o-mini",
        temperature=1.,
        max_tokens=1000,
        top_p=1.   
    )
    print(f"答：{response.choices[0].message.content}")
    
