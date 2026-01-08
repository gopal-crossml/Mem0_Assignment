import os

from mem0 import MemoryClient
from cred import MEM0_API_KEY,USER_ID


memory_client = MemoryClient(
    api_key = MEM0_API_KEY
)


def search_memory(user_input: str):

    # Retrieve relevant long-term memories
    memories = memory_client.search(
        user_id=USER_ID,
        query=user_input,
        filters = {"user_id" : "USER_ID"},
        limit=5
    )
    return memories

    # Store conversation in Mem0
def add_memory(user_input: str):
    memory_client.add(
    user_id=USER_ID,
    messages=user_input
    )
    