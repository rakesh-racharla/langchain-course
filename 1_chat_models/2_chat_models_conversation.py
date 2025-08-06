from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

messages = [
    SystemMessage("You are an expert in social media content strategy"), 
    HumanMessage("Give a short tip to create engaging posts on Instagram"), 
]

result = llm.invoke(messages)

print(result.content)