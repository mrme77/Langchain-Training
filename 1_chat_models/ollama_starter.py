# from langchain_ollama import OllamaLLM  # Updated import

# # Connect to your local Ollama model
# llm = OllamaLLM(model="gemma3:12b-it-qat")

# # Invoke it
# response = llm.invoke("Transalate the following English sentnce I love promamming to Italian.")
# print(response)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="gemma3:12b-it-qat")

chain = prompt | model

print(chain.invoke({"question": "What is LangChain?"}))