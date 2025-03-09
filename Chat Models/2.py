#Basic Chat Model and Types of Messages used in LangChain
import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

llm = ChatMistralAI(model="open-mistral-7b")

messages = [
    SystemMessage("You are an expert in Affliate Marketing Strategy"),
    HumanMessage("Givea short tip on how to start with affliate marketing")
]
result = llm.invoke(messages)
print(result.content)