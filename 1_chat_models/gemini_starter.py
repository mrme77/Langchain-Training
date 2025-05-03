import getpass
import os
import time
#print(os.environ["GOOGLE_API_KEY"])
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=200,
    timeout=None,
    max_retries=1,
    # other params...
)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to Italian. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
time.sleep(10)
ai_msg = llm.invoke(messages)
#print(ai_msg.content)
print(ai_msg)

