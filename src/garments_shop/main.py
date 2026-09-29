from garments_shop.agent import run_agent

from garments_shop.memory import load_memory

def main():

    messages = []

    memory = load_memory()

    while True:

        user_message = input("You: ")

        if user_message.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        if not user_message.strip():
            continue

        answer = run_agent(user_message, messages,  memory)
        print(f"Agent: {answer}")

if __name__ == "__main__":
    main()