"""
Run all examples from one file.
"""

from agents.multi_agents import multi_agent
from agents.memory import add_memory,search_memory



MEMORY_TRIGGERS = [
    "remember",
    "from now on",
    "i prefer",
    "my location",
    "use this format",
    "always"
]

def should_store_memory(text: str) -> bool:
    text = text.lower()
    return any(trigger in text for trigger in MEMORY_TRIGGERS)

def main():
    print("Agent is ready. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # Store memory if needed
        if should_store_memory(user_input):
            add_memory(user_input)
            print(" Memory saved.\n")

        # Retrieve past memory
        memory_context = search_memory(user_input)

        # Send to agent
        response = multi_agent.invoke({
            "messages": [
                {
                    "role": "system",
                    "content": f"User memory:\n{memory_context}"
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })

        print("Agent:", response["messages"][-1].content)
        print()
if __name__ =="__main__":
    main()

    # add_memory("User prefers to solve the equation step by step with proper breakdown")
    # add_memory("Users prefers DD-MM-YY date format")
    # add_memory("Users locality is in banglore.")
    # add_memory("User prefer text sentiment answer in one line with small reasons.")

    
    # math_result = agent.invoke({"messages": [{"role": "user", "content": "What is (234 * 12) + 98?"}]})
    # print("\n--- Example 1 ---")
    # print(math_result["messages"][-1].content)    

    # analyzer_result = agent.invoke({"messages": [{"role": "user", "content":"Analyze this paragraph: I love this product. It is excellent!"}]})
    # print("\n--- Example 2 ---")
    # print(analyzer_result["messages"][-1].content)
    
    # date_result = agent.invoke({"messages": [{"role": "user", "content":"What will be the date 45 days from today?"}]})
    # print("\n--- Example 3 ---")
    # print(date_result["messages"][-1].content)
   

    # shipping_result = multi_agent.invoke({"messages": [{"role": "user", "content": "Calculate the total cost if I buy 3 items priced at 499 each,and tell me the delivery date if shipping takes 7 days."}]})
    # print("\n--- Multi Tool Example ---")
    # print(shipping_result["messages"][-1].content)

    # api_result = api_agent.invoke({"messages": [{"role": "user", "content": "How is the weather in Chandigar?"}]})
    # print("\n--API example--")
    # print(api_result["messages"][-1].content)

                                    

