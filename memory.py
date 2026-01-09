from typing import List, Dict
from mem0 import MemoryClient
from cred import MEM0_API_KEY

mem0 = MemoryClient()

def retrieve_context(query: str, user_id: str) -> List[Dict]:
    try:
        memories = mem0.search(
            query = query, 
            filters = {"user_id" : user_id},

            )
        
        memory_list = memories.get("results", [])

        serialized = " ".join(mem["memory"] for mem in memory_list)

        if not serialized:
            return[]

        return [{
            "role": "system",
            "content": f"Relevant information: {serialized}"
        }]
    except Exception as e:
        print("Memory retrieval error:", e)
        return []

def save_interaction(user_id: str, user_input: str, assistant_response: str):
    try:
        mem0.add(
            [
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": assistant_response}
            ],
            user_id=user_id
        )
    except Exception as e:
        print("Memory save error:", e)  