# from langchain_ollama import OllamaLLM  # Updated import

# # Connect to your local Ollama model
# llm = OllamaLLM(model="gemma3:12b-it-qat")

# # Invoke it
# response = llm.invoke("Transalate the following English sentnce I love promamming to Italian.")
# print(response)
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage, AIMessage

#template = """Question: {question}

#Answer: Let's think step by step and you can return your answer in one sentence."""
#instructions = "You can only return one sentence"
messages = [
    SystemMessage("You are a Serie A football expert"),
    HumanMessage("Give a short tip to create engaging posts on Instagram"),
    AIMessage("Let's think step by step and return the answer in one sentence."),
]



model = OllamaLLM(model="gemma3:12b-it-qat",temperature=0.9, max_tokens=200, timeout=None, max_retries=1)

ai_msg = model.invoke(messages)
print(ai_msg)