import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MEM0_API_KEY = os.getenv("MEM0_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment")

if not MEM0_API_KEY:
    raise ValueError("MEM0_API_KEY not found in environment")