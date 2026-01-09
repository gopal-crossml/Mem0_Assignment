from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def get_prompt():
    return ChatPromptTemplate.from_messages([
        SystemMessage(content="""
You are a helpful Personal Assistant AI.
Use stored memories to personalize responses, including remembering the user’s name, preferences, and prior interactions when explicitly shared.
If the user provides their name, store it and use it naturally in future responses when appropriate.
Always maintain a friendly, respectful, and helpful tone.
"""),
        MessagesPlaceholder(variable_name="context"),
        HumanMessage(content="{input}")
    ])