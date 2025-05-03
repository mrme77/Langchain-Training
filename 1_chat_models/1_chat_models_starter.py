from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

result = llm.invoke("What is the current time in India?")

print(result)

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Initialize the chat model
model = ChatOllama(model="gemma3:12b-it-qat")

# Create a prompt template
template = """Question: {question}
Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

# Create a chain
chain = prompt | model

# Invoke the chain
response = chain.invoke({"question": "What is LangChain?"})
print(response)
