# import nltk
# import random
# from nltk.tokenize import word_tokenize
# from nltk.corpus import wordnet

# # Download NLTK data if you haven't already
# # nltk.download("punkt")
# # nltk.download("wordnet")

# # Define patterns and responses
# travel_patterns = [
#     (r"travel to (\w+)", ["Sure, I can help you plan a trip to {}.", "Let's explore {}!"]),
#     (r"visit (\w+)", ["I can assist with travel to {}.", "Exploring {} sounds like a great idea."]),
# ]

# # Define a function to handle user input
# def handle_travel_booking(user_input):
#     for pattern, responses in travel_patterns:
#         match = nltk.regexp_tokenize(user_input, pattern)
#         if match:
#             destination = match[0]
#             response = random.choice(responses).format(destination)
#             return response
#     return "I'm not sure about that destination. Can I assist you with something else?"

# # Main interaction loop
# print("Welcome to HaiHai Travel Agency, How can I Help? (Type 'quit' to exit)")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "quit":
#         print("Chatbot: Goodbye!")
#         break

#     response = handle_travel_booking(user_input)
#     print("Chatbot:", response)

# intent_response = {
#      'greeting' : ['Hey there! Welcome to HaiHai Movie. (Type exit to leave this conversation)', 'Hey There! (Type exit to leave this conversation)', 'Hello. (Type exit to leave this conversation)', 'Hi! How can i assist you today? (Type exit to leave this conversation)', 'Hi there, what movie would you like to watch? (Type exit to leave this conversation)'],
#      'movie_list' : ['Sure, here are the current movies available to watch..'], H
#      'showtimes' : ['These are the available showtimes for the movie', 'Sure, when do you want to watch the movie?'],           
#      'book_tickets' : ['''Great! Let's proceed with the booking. Please provide the movie name and showtime.'''],
#      'goodbye' : ['Thank you for using HaiHai Movie Bot, Enjoy your movie!', 'Goodbye!', 'See you at the movies!'],
#      'default' : ['''Sorry, I didn't quite catch that. Can you say it again please?''']       
# }


    #  query = ('').join(token)
     
    #  query_vect = all_df_vect.transform([query]).toarray()
    #  query_sim = 1 - pairwise_distances(df, query_vect, metric='cosine')
    #  max_sim = np.where(query_sim == np.max(query_sim, axis=0))
    #  index_output = np.random.choice(max_sim[0])
     
    #  query_vect1 = all_df_vect1.transform([query]).toarray()
    #  query_sim1 = 1 - pairwise_distances(df1, query_vect1, metric='cosine')
    #  max_sim1 = np.where(query_sim1 == np.max(query_sim1, axis=0))
    #  index_output1 = np.random.choice(max_sim1[0])
     
    #  query_vect2 = all_df_vect2.transform([query]).toarray()
    #  query_sim2 = 1 - pairwise_distances(df2, query_vect2, metric='cosine')
    #  max_sim2 = np.where(query_sim2 == np.max(query_sim2, axis=0))
    #  index_output2 = np.random.choice(max_sim2[0])
     
    #  similirity_threshold = 0.75
     
     
     
    #  if max_sim > similirity_threshold and max_sim > max_sim1 and max_sim > max_sim2:
    #       return(all_df['Output'].loc[index_output])
          
    #  elif max_sim1 > similirity_threshold and max_sim1 > max_sim and max_sim1 > max_sim2:
    #       return(all_df1['Answer'].loc[index_output1])
          
    #  elif max_sim2 > similirity_threshold and max_sim2 > max_sim and max_sim2 > max_sim1:
    #       return(all_df2['Smalla'].loc[index_output2])
          
    #  else:
    #       return("I'm sorry, i didn't quite catch that.")

     
     # return False
     # if "hello" in token or "hi" in token:
     #      return 'greeting'
     # elif "movie" in token and "list" in token or "movie" in token and "show" in token:
     #      return 'movie_list'
     # elif "showtime" in token or "showtimes" in token:
     #      return 'showtimes'
     # elif "book" in token or "buy" in token or "purchase" in token:
     #      return 'book_tickets'
     # else:
     #      return 'default'
          
          
# def qa_lemma(user):
#      posmap = {
#           'ADJ' : 'a',
#           'ADV' : 'r',
#           'NOUN' : 'n',
#           'VERB' : 'v'
#      }
     
#      post = nltk.pos_tag(word_tokenize(user), tagset='universal')

#      for token in post:
#           word = token[0]
#           tag = token[1]
#           if tag in posmap.keys():
#                lemma1 = lemmatiser.lemmatize(word, posmap[tag])
#                return(lemma1)
#           else:
#                lemma2 = lemmatiser.lemmatize(word)
#                return(lemma2)

# # process_response = [process(response) for response in intent_response] #process tokens


# # def intent_matching(user_input, all_df_total_tfidf, all_datasets, column_output_names, threshold=0.75):
# #      similarities = []
     
# #      for i in range(len(all_df_total_tfidf)):
# #           all_df_total = all_df_total_tfidf[i]
# #           datasets = all_datasets[i]
# #           column_output_name = column_output_names[i]
          
# #           query = ''.join(user_input)
          
# #           query_vect = all_df_total.transform(query).toarray()
# #           query_sim = 1 - pairwise_distances(query_vect, all_df_total, metric='cosine')
# #           if np.max(query_sim) >= threshold:
# #                max_sim = np.where(query_sim == np.max(query_sim, axis=0))
# #                max_sim_random = np.random.choice(max_sim)
# #                intent = datasets.iloc[max_sim_random][column_output_name]
# #                similarities.append(intent)
               
# #      if not similarities:
# #           return None
# #      else:
# #           return np.random.choice(similarities)

#                # final_output = intent_matching(user_input,
#                #                               [df, df1, df2],
#                #                               [all_df, all_df1, all_df2],
#                #                               ['Output', 'Answer', 'Smalla'],
#                #                               threshold=0.75)
               
#                # if final_output is None:
#                #      print("Haihai Bot: I'm sorry, i couldn't quite catch that. Can you please say it again?")
#                # else:
#               #      print(f"Haihai Bot: {final_output}")

# countries = [
# #     "United States",
# #     "Canada",
# #     "United Kingdom",
# #     "France",
# #     "Germany",
# #     "Italy",
# #     "Spain",
# #     "Japan",
# #     "China",
# #     "India",
# # ]

# # import nltk
# # import re
# # import random

# # nltk.download("punkt")
# # from nltk.tokenize import word_tokenize

# # # Define patterns and responses
# # travel_patterns = [
# #     (r"travel to (\w+)", ["Sure, I can help you plan a trip to {}.", "Let's explore {}!"]),
# #     (r"visit (\w+)", ["I can assist with travel to {}.", "Exploring {} sounds like a great idea."]),
# # ]

# # # Define a function to handle user input
# # def handle_travel_booking(user_input):
# #     for pattern, responses in travel_patterns:
# #         match = re.match(pattern, user_input, re.IGNORECASE)
# #         if match:
# #             destination = match.group(1)
# #             if destination in countries:
# #                 response = random.choice(responses).format(destination)
# #                 return response
# #     return "I'm not sure about that destination. Can I assist you with something else? (Type: travel to / visit)"

# # # Main interaction loop
# # print("Hello! I'm your travel booking assistant. How can I assist you today? (Type 'quit' to exit)")

# # while True:
# #     user_input = input("You: ")
# #     if user_input.lower() == "quit":
# #         print("Chatbot: Goodbye!")
# #         break

# #     response = handle_travel_booking(user_input)
# #     print("Chatbot:", response)
    
# import nltk, re, pprint, string, array
# from nltk.util import ngrams
# from nltk import word_tokenize, sent_tokenize
# from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.util import pad_sequence
# from nltk.lm import MLE, Laplace
# from collections import Counter 
# from nltk.lm.preprocessing import pad_both_ends, padded_everygram_pipeline
# from sklearn.dummy import DummyClassifier
# from nltk.corpus import wordnet
    
# countries_ex = [
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

# def handle_checking(tokens):
#      for token in tokens:
#           if token in str(countries_ex):
#                print(f"Chatbot: I see you'd like to go to {token}") 
#           else:
#                print(f"Chatbot: I'm sorry, I don't think that place is available to travel at the moment")
#                break
#      return f"Chatbot: Is there anything else i can help you with?" 


# def rule_based_description(country):
#     word = []
#     for word in leove_str:
#               return word.append(leove_str)          

#     description = ""
    
#     if country['type'] in (str(countries_ex)) or word in (str(countries_ex)):
#         description += "Your budget needs to be atleast 2000$"
#     elif country['type'] not in (str(countries_ex)):
#         description += "You're good to go with a budget under 2000$"
        
#     return description

# leove = input("Welcome to Travel HaiHai, What can i help you with?: ")
# leove_str = str(leove)
# country_data = {'type': leove_str}
# # print(handle_checking(leove))
# print(rule_based_description(country_data))                                          


# # def main():
# #      while True:
# #           user_input = input("You: ")
# #           if user_input.lower() == 'exit':
# #                print("Goodbye!")
# #                break
           
# #           print(f"ChatBot: You said {processed_input}")
          
# # leove = input("Welcome to Travel HaiHai, What can i help you with?: ")
# # leove_str = str(leove)

# # def handle_checking(tokens):
# #      tokens = nltk.word_tokenize(user_input)
# #      for token in tokens:
# #           if token == leove_str:
# #                print(f"Chatbot: I see you'd like to go to {leove_str}")
# #           else:
# #                print(f"Chatbot: I'm sorry, I don't think that place is available to travel at the moment")
# #      return "Is there anything i can help you with?"  
          
