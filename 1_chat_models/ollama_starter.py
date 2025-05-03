# from langchain_ollama import OllamaLLM  # Updated import

# # Connect to your local Ollama model
# llm = OllamaLLM(model="gemma3:12b-it-qat")

# # Invoke it
# response = llm.invoke("Transalate the following English sentnce I love promamming to Italian.")
# print(response)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

#template = """Question: {question}

#Answer: Let's think step by step and you can return your answer in one sentence."""
#instructions = "You can only return one sentence"
prompt = ChatPromptTemplate.from_messages([
    ("system", "You can only return 10 words. Be concise and direct."),
    ("human", "Question: {question}"),
    ("ai", "Let's think step by step and return the answer in one sentence.")
])


model = OllamaLLM(model="gemma3:12b-it-qat")

chain =  prompt | model

print(chain.invoke({"question": "What is Napoli?"}))