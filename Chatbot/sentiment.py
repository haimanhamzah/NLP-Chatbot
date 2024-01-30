import pandas as pd
import numpy as np
from preprocessing import *
from tokenisation import *

#Sentiment analysis
def sentiment_analysis(lemmatized_name):
     print(f"HaiHai bot: How are you feeling today {lemmatized_name}? (Answer with one word only without spaces)")
     user_emotion = input("You: ")
               
     if user_emotion in positive:
          print("HaiHai bot: I'm glad you're feeling well!")
          return lemmatized_name
     elif user_emotion in negative:
          print("HaiHai bot: Aw I'm sorry to hear that, Would you like me to tell a joke? (Press Enter to say Yes and any other key to say no)")
          user_confirm = input()
          
          if user_confirm == "":
               print(np.random.choice(jokes))
               return lemmatized_name
          else:
               print("HaiHai bot: Aw, regardless i'm here for you.")
               return lemmatized_name