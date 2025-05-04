from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage, AIMessage

#template = """Question: {question}

#Answer: Let's think step by step and you can return your answer in one sentence."""
#instructions = "You can only return one sentence"
#chat_history = []  # Use a list to store messages
system_message = SystemMessage(content="You are a helpful AI assistant.")
model = OllamaLLM(model="gemma3:12b-it-qat", temperature=0.9, max_tokens=200, timeout=None, max_retries=1)
#chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    #chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    response = model.invoke(query)
    #response = result
    #chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")


#print("---- Message History ----")
#print(chat_history)

# messages = [
#     SystemMessage("You are a Serie A football expert"),
#     HumanMessage("Give a short tip to create engaging posts on Instagram"),
#     AIMessage("Let's think step by step and return the answer in one sentence."),
# ]



