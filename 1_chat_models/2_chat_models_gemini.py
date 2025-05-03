import getpass
import os
import time
#print(os.environ["GOOGLE_API_KEY"])
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_core.prompts import SystemMessage, HumanMessage, AIMessage
from langchain.schema import SystemMessage, HumanMessage, AIMessage
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=200,
    timeout=None,
    max_retries=1,
    # other params...
)

messages = [
    SystemMessage("You are a Serie A football expert"),
    HumanMessage("Give a short tip to create engaging posts on Instagram"),
    AIMessage("Let's think step by step and return the answer in one sentence."),
]

time.sleep(10)
ai_msg = llm.invoke(messages)
print(ai_msg.content)
#print(ai_msg)

