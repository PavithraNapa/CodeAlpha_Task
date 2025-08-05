# filepath: c:\Users\user\OneDrive\Desktop\CodeAlpha_Hangman\basic_chatbot.py
print("Starting chatbot...")  # Add this line

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["hello", "hi"]:
            print("Chatbot: Hi!")
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks!")
        elif user_input in ["bye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

if __name__ == "__main__":
    chatbot()