"""
Multi-tool agent using ReAct reasoning.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


from cred import gemini_api_key
from tools.math import math_calculator
from tools.date import future_date

#chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0
)
#Tools 
tools = [math_calculator, future_date]

#created an agent for multiple tools 
multi_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt='You are helpful assistance.'
)
