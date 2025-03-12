#Prompt Template
import os
from constant import mistral_key  # Ensure this file exists with your API key
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Set Mistral API Key
os.environ["Mistral_API_KEY"] = mistral_key

llm = ChatMistralAI(model="open-mistral-7b")

template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength, Keep it to 4 lines max"

prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({
    "tone":"polite",
    "company":"cisco",
    "position":"AI Engineer",
    "skill":"AI"
})

result = llm.invoke(prompt)

print(result.content)
