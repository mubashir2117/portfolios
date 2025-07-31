# simple_chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing fine! What about you?"
    elif "your name" in user_input:
        return "I'm your simple Python chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

# Chat loop
print("Chatbot: Hello! (type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot:", chatbot_response(user_input))
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
