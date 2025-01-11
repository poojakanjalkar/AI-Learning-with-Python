# Simple AI Chatbot using keyword matching

def chatbot():
    print("Hi! I'm your friendly AI chatbot. Ask me anything or type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "weather" in user_input:
            print("Chatbot: The weather is sunny and pleasant today!")
        elif "name" in user_input:
            print("Chatbot: I'm your friendly AI chatbot. What's your name?")
        elif "time" in user_input:
            from datetime import datetime
            print(f"Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}.")
        elif "joke" in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you rephrase?")
            
chatbot()
