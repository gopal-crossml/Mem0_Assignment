from langchain_google_genai import ChatGoogleGenerativeAI

MODEL_NAME = "gemini-2.5-flash-lite"

def get_llm():
    return ChatGoogleGenerativeAI(model=MODEL_NAME)