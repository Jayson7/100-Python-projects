def chatbot_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm fine, thank you!",
        "bye": "Goodbye!",
    }

    return responses.get(user_input.lower(), "I don't understand that.")

if __name__ == "__main__":
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
