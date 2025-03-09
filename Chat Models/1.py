import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

llm = ChatMistralAI(model="open-mistral-7b")

result = llm.invoke("What is 2+2")
print(result)