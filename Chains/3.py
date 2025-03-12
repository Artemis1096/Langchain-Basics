# Sequential Chaining Example
import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

model = ChatMistralAI(model="open-mistral-7b")

# Define prompt templates
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You like telling facts and you tell facts about {animal}."),
        ("human", "Tell me {count} facts."),
    ]
)

# Define a prompt template for translation to French
translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

# Define additional processing steps using RunnableLambda
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "french"})


# Create the combined chain using LangChain Expression Language (LCEL)
chain = animal_facts_template | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser() 

# Run the chain
result = chain.invoke({"animal": "cat", "count": 2})

# Output
print(result)