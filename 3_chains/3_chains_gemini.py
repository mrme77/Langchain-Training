import os
import time
import sys
#print(os.environ["GOOGLE_API_KEY"])
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
time.sleep(10)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    max_tokens=200,
    timeout=None,
    max_retries=1    # other params...
)

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model #| StrOutputParser()
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result.content)
