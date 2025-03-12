import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

model = ChatMistralAI(model="open-mistral-7b")

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)