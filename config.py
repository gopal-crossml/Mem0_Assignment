from langchain_google_genai import ChatGoogleGenerativeAI

MODEL_NAME = "gemini-3-flash-preview"

def get_llm():
    """
    Summary:
        This function initializes a ChatGoogleGenerativeAI object using
        a predefined model name ('gemini-3-flash-preview').

    Args:
        None

    Returns:
        ChatGoogleGenerativeAI: An instance of the Google Generative AI
        chat model ready for use.
    """
    return ChatGoogleGenerativeAI(model=MODEL_NAME)