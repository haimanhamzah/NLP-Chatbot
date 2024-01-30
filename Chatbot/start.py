import pandas as pd
import numpy as np
from preprocessing import *
from tokenisation import *
from movie import movie_bot
from chat import chatbot
from sentiment import sentiment_analysis
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.metrics.pairwise import pairwise_distances
from datetime import datetime

def main():
     # user_hashmap = {'name': ''}
     print("HaiHai bot: Hello! what's your name? (Press Ctrl+C to exit)")
     user_name = input("You: ")
     lemmatized_name = process(user_name)
     lemmatized_name = ''.join(lemmatized_name)
     
     #Sentiment analysis
     sentiment_analysis(lemmatized_name)
               
     print("-------------------------------------------------------------------------------------------------------------------------")
               
     print(f"HaiHai bot: Hi there, Nice to meet you {lemmatized_name}!, How can i assist you today? (Type help to see options) (Type exit to quit)")

     flag = True
     while(flag == True):
          user_input = input("You: ")
          if user_input == ("exit"):
               print("Have a nice day!")
               break
          elif user_input == ("help"):
               
               print("---------------------------------- Help ----------------------------------")
               print("Type 'moviebot' to enter booking of movie\n")
               print("--------------------------------------------------------------------------\n")
               print("Small talk with Chatbot is available")
               print("Can answer simple conversational statements")
               print("Try typing: 'Say something funny', 'Tell me something you can do' or 'Can you say something else?'\n")
               print("--------------------------------------------------------------------------\n")
               print("Question Answering with Chatbot is available")
               print("This dataset is based on the 'A small QA Dataset' in the labs\n")
               print("--------------------------------------------------------------------------\n")
               print("Type exit to quit")
          
          elif user_input == "":
               
               print(f"HaiHai bot: Hi there, Nice to meet you {lemmatized_name}!, How can i assist you today? (Type help to see options) (Type exit to quit)")
               
          elif user_input == ("moviebot"):
               print("HaiHai Moviebot: Welcome to HaiHai Cinemas, What can I do for you today? (type 'finish' to exit movie bot)")
               print("------------------------------------------------------------------------------------------------------------")
               print("HaiHai Moviebot: Searching for movie -> Searching for showtime -> Booking the movie and time (Don't separate time from AM/PM e.g. 8pm) -> Change the Time if necessary -> saying Thank you")
               print("HaiHai Moviebot: Once all is done, type 'finish' to exit")
               print("HaiHai Moviebot: DISCLAIMER: The Movies are not real and conform to Copyright/Trademark act")
               
               movie_bot()
               
          else:
               chatbot(user_input, lemmatized_name)
         
if __name__ == "__main__":
     main()
 