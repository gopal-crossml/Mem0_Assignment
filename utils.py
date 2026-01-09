from config import get_llm
from prompts import get_prompt

llm = get_llm()
prompt = get_prompt()

def generate_response(user_input: str, context):
    chain = prompt | llm
    response = chain.invoke({
        "input": user_input,
        "context": context
    })
    return response.content[0]['text']