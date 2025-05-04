from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser


system_message = SystemMessage(content="You are a helpful AI assistant.")
model = OllamaLLM(model="gemma3:12b-it-qat", temperature=0.9, max_tokens=200, timeout=None, max_retries=1)

# Define prompt templates (no need for separate Runnable chains)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser()
# chain = prompt_template | model

# Run the chain
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Output
print(result)
