"""    THIS FILE IS NOT USED IN THE LATEST IMPLEMENTATION OF THE CHATBOT, AS IT WAS USED AS A PRIOR TRIAL AND ERROR FILE    """




# countries = [
#     "United States",
#     "Canada",
#     "United Kingdom",
#     "France",
#     "Germany",
#     "Italy",
#     "Spain",
#     "Japan",
#     "China",
#     "India",
# ]

# import nltk
# import re
# import random

# nltk.download("punkt")
# from nltk.tokenize import word_tokenize

# # Define patterns and responses
# travel_patterns = [
#     (r"travel to (\w+)", ["Sure, I can help you plan a trip to {}.", "Let's explore {}!"]),
#     (r"visit (\w+)", ["I can assist with travel to {}.", "Exploring {} sounds like a great idea."]),
# ]

# # Define a function to handle user input
# def handle_travel_booking(user_input):
#     for pattern, responses in travel_patterns:
#         match = re.match(pattern, user_input, re.IGNORECASE)
#         if match:
#             destination = match.group(1)
#             if destination in countries:
#                 response = random.choice(responses).format(destination)
#                 return response
#     return "I'm not sure about that destination. Can I assist you with something else? (Type: travel to / visit)"

# # Main interaction loop
# print("Hello! I'm your travel booking assistant. How can I assist you today? (Type 'quit' to exit)")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "quit":
#         print("Chatbot: Goodbye!")
#         break

#     response = handle_travel_booking(user_input)
#     print("Chatbot:", response)
    
import nltk, re, pprint, string, array
from nltk.util import ngrams
from nltk import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.util import pad_sequence
from nltk.lm import MLE, Laplace
from collections import Counter 
from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
from sklearn.dummy import DummyClassifier
from nltk.corpus import wordnet
    
countries_ex = [
    "United States",
    "Canada",
    "United Kingdom",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Japan",
    "China",
    "India",
]

def handle_checking(tokens):
     for token in tokens:
          if token in str(countries_ex):
               print(f"Chatbot: I see you'd like to go to {token}") 
          else:
               print(f"Chatbot: I'm sorry, I don't think that place is available to travel at the moment")
               break
     return f"Chatbot: Is there anything else i can help you with?" 


def rule_based_description(country):
    word = []
    for word in leove_str:
              return word.append(leove_str)          

    description = ""
    
    if country['type'] in (str(countries_ex)) or word in (str(countries_ex)):
        description += "Your budget needs to be atleast 2000$"
    elif country['type'] not in (str(countries_ex)):
        description += "You're good to go with a budget under 2000$"
        
    return description

leove = input("Welcome to Travel HaiHai, What can i help you with?: ")
leove_str = str(leove)
country_data = {'type': leove_str}
# print(handle_checking(leove))
print(rule_based_description(country_data))                                          


# def main():
#      while True:
#           user_input = input("You: ")
#           if user_input.lower() == 'exit':
#                print("Goodbye!")
#                break
           
#           print(f"ChatBot: You said {processed_input}")
          
# leove = input("Welcome to Travel HaiHai, What can i help you with?: ")
# leove_str = str(leove)

# def handle_checking(tokens):
#      tokens = nltk.word_tokenize(user_input)
#      for token in tokens:
#           if token == leove_str:
#                print(f"Chatbot: I see you'd like to go to {leove_str}")
#           else:
#                print(f"Chatbot: I'm sorry, I don't think that place is available to travel at the moment")
#      return "Is there anything i can help you with?"  
          
