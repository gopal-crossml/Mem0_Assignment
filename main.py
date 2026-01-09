from memory import retrieve_context, save_interaction
from utils import generate_response

def chat_turn(user_input: str, user_id: str) -> str:
    context = retrieve_context(user_input, user_id)
    response = generate_response(user_input, context)
    save_interaction(user_id, user_input, response)
    return response

if __name__ == "__main__":
    print("Hi! Your personal assistant is here to help!")
    user_id = "jack"

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Personal Assistant : Thanks for reaching out! Please let me know if there’s anything else I can assist you with.")
            break

        reply = chat_turn(user_input, user_id)
        print("Personal Assistant :", reply)