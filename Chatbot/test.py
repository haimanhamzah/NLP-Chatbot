import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Download NLTK data if you haven't already
# nltk.download("punkt")
# nltk.download("wordnet")

# Define patterns and responses
travel_patterns = [
    (r"travel to (\w+)", ["Sure, I can help you plan a trip to {}.", "Let's explore {}!"]),
    (r"visit (\w+)", ["I can assist with travel to {}.", "Exploring {} sounds like a great idea."]),
]

# Define a function to handle user input
def handle_travel_booking(user_input):
    for pattern, responses in travel_patterns:
        match = nltk.regexp_tokenize(user_input, pattern)
        if match:
            destination = match[0]
            response = random.choice(responses).format(destination)
            return response
    return "I'm not sure about that destination. Can I assist you with something else?"

# Main interaction loop
print("Welcome to HaiHai Travel Agency, How can I Help? (Type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Chatbot: Goodbye!")
        break

    response = handle_travel_booking(user_input)
    print("Chatbot:", response)