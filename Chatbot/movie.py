import numpy as np
from preprocessing import *
from sklearn.metrics.pairwise import pairwise_distances
from datetime import datetime

#Movie transaction Bot

def movie_bot():
     movie_flag = True
     while(movie_flag == True):
          movie_input = input("You: ")
          movie_query = movie_input
          
          query_vect = all_df_vect.transform([movie_query]).toarray()
          query_sim = 1 - pairwise_distances(df, query_vect, metric='cosine')
          max_sim = np.where(query_sim == np.max(query_sim, axis=0))
          index_output = np.random.choice(max_sim[0])
          
          if 0.75 < query_sim.max():
               print("HaiHai Moviebot: " + all_df['Output'].loc[index_output])
          elif movie_input == "finish":
               print("HaiHai Moviebot: Thank you for using MovieBot, Have a nice day")
               movie_flag == False
               break
          else: 
               print("Sorry I didn't quite catch that, can you repeat it again please? (Remember to follow the pointers given by Moviebot above)")       