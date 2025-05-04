from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import re

# Initialize chat components
chat_history = []
system_message = SystemMessage(content="You are a helpful AI assistant.")
model = OllamaLLM(model="gemma3:12b-it-qat", temperature=0.9, max_tokens=200, timeout=None, max_retries=1)
chat_history.append(system_message)

# Create a simple in-memory knowledge base from past interactions
knowledge_base = {}

# Function to search chat history for similar questions
def search_history(query, chat_history):
    # Clean and normalize the query
    query = query.lower().strip()
    
    # First try exact matches in knowledge base
    if query in knowledge_base:
        return knowledge_base[query]
    
    # Then check for similar questions by keywords
    query_words = set(re.findall(r'\w+', query))
    for q, a in knowledge_base.items():
        q_words = set(re.findall(r'\w+', q))
        # If there's significant word overlap (adjust threshold as needed)
        if len(query_words.intersection(q_words)) >= min(2, len(query_words) * 0.7):
            return f"Based on a similar question I answered earlier: {a}"
    
    return None

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
        
    # First check if we can answer from history
    answer_from_history = search_history(query, chat_history)
    
    if answer_from_history:
        print(f"AI (from history): {answer_from_history}")
        # Still record this interaction in chat history
        chat_history.append(HumanMessage(content=query))
        chat_history.append(AIMessage(content=answer_from_history))
    else:
        # Add user message to history
        chat_history.append(HumanMessage(content=query))
        
        # Make API call only when necessary
        result = model.invoke(chat_history)
        response = result
        chat_history.append(AIMessage(content=response))
        
        # Store in knowledge base for future reference
        knowledge_base[query.lower().strip()] = response
        
        print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)
