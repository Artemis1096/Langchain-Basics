#Making a chatbot which also remembers the conversation history
import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

model = ChatMistralAI(model="open-mistral-7b")

chat_history = [] #using a list to store messages

# Set an initial system message
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message) #added system message to chat history

#Chat Loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))
    
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI: {response}")
    
print("Message History")
print(chat_history)