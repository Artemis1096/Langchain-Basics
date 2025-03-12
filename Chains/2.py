# same working as 1.py using runnableLambdas
import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

model = ChatMistralAI(model="open-mistral-7b")

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
     [
        ("system", "You love facts and you tell facts about {animal}"),
        ("human", "Tell me {count} facts."),
    ]
)

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"animal": "cat", "count": 2})

# Output
print(response)