"""    THIS FILE IS NOT USED IN THE LATEST IMPLEMENTATION OF THE CHATBOT, AS IT WAS USED AS A PRIOR TRIAL AND ERROR FILE    """

# import random
# import pandas as pd
# import numpy as np
# import nltk
# from nltk.tokenize import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem.wordnet import WordNetLemmatizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances


# intent_response = {
#      'greeting' : ['Hey there! Welcome to HaiHai Movie. (Type exit to leave this conversation)', 'Hey There! (Type exit to leave this conversation)', 'Hello. (Type exit to leave this conversation)', 'Hi! How can i assist you today? (Type exit to leave this conversation)', 'Hi there, what movie would you like to watch? (Type exit to leave this conversation)'],
#      'movie_list' : ['Sure, here are the current movies available to watch..'], 
#      'showtimes' : ['These are the available showtimes for the movie', 'Sure, when do you want to watch the movie?'],           
#      'book_tickets' : ['''Great! Let's proceed with the booking. Please provide the movie name and showtime.'''],
#      'goodbye' : ['Thank you for using HaiHai Movie Bot, Enjoy your movie!', 'Goodbye!', 'See you at the movies!'],
#      'default' : ['''Sorry, I didn't quite catch that. Can you say it again please?''']       
# }

# all_df = pd.read_csv("transaction_response.csv")

# all_df_vect = TfidfVectorizer(analyzer='word', use_idf=True, smooth_idf=True, sublinear_tf=True)

# all_df_tfidf = all_df_vect.fit_transform(all_df['Input']).toarray()

# df = pd.DataFrame(all_df_tfidf, columns=all_df_vect.get_feature_names_out())


# #Pre processing the document
# lemmatiser = WordNetLemmatizer()

def process(user_input):
     input_token  = word_tokenize(user_input) #input tokenized
     stop_words = set(stopwords.words('english'))
     filtered_token = [word.lower() for word in input_token if word.isalnum() and word not in stop_words]
     lemmatised_token = [lemmatiser.lemmatize(word) for word in filtered_token]
     return lemmatised_token

# # process_response = [process(response) for response in intent_response] #process tokens


# def intent_matching(token): 
#      query = ('').join(token)
#      query_vect = all_df_vect.transform([query]).toarray()
#      query_sim = 1 - pairwise_distances(df, query_vect, metric='cosine')
#      max_sim = np.where(query_sim == np.max(query_sim, axis=0))
#      index_output = np.random.choice(max_sim[0])
     
#      print(all_df['Output'].loc[index_output])
     
#      # return False
#      # if "hello" in token or "hi" in token:
#      #      return 'greeting'
#      # elif "movie" in token and "list" in token or "movie" in token and "show" in token:
#      #      return 'movie_list'
#      # elif "showtime" in token or "showtimes" in token:
#      #      return 'showtimes'
#      # elif "book" in token or "buy" in token or "purchase" in token:
#      #      return 'book_tickets'
#      # else:
#      #      return 'default'
          
          
 
# def main(): 
#      first_greet = intent_response['greeting']
#      print("Bot: " + random.choice(list(first_greet)))
#      while True:
#           user_input = input("You: ")
#           if user_input.lower() != 'exit':
#                if user_input == "thanks" or user_input == "thank you":
#                     print("Bot: You're Welcome!")
#                     break
#                else:
#                     process_input = process(user_input)
#                     intent = intent_matching(process_input)
#                     respond = intent_response.get(intent)
#                     print("Bot: ", respond)
#           else:
#                print("Bot: Thank you for using HaiHai Movie Bot! Have a nice day")
#                break
          
          
# if __name__ == "__main__":
#      main()
