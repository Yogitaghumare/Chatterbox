import nltk
from nltk.chat.util import Chat, reflections

# Download the required NLTK corpora (if you haven't already)
nltk.download('punkt')
# Define the pairs of patterns and responses
patterns = [
    (r'Hi|Hello|Hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'What is your name?', ['I am a chatbot created using NLTK.']),
    (r'How are you?', ['I am doing great, thank you!', 'I am just a bot, but I am fine.']),
    (r'What can you do?', ['I can chat with you and answer some basic questions.']),
    (r'Quit', ['Bye! Have a nice day!']),
    # Add more patterns and responses as needed
]
# Create a chatbot instance
chatbot = Chat(patterns, reflections)
def chatbot_response(user_input):
    return chatbot.respond(user_input)

def chat():
    print("Hello! I am your chatbot. Type 'Quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == 'quit':
            break
if __name__ == "__main__":
    chat()
