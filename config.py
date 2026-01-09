from langchain_google_genai import ChatGoogleGenerativeAI

MODEL_NAME = "gemini-3-flash-preview"

def get_llm():
    return ChatGoogleGenerativeAI(model=MODEL_NAME)