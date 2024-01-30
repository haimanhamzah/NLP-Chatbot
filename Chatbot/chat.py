import pandas as pd
import numpy as np
from preprocessing import *
from tokenisation import *
from sklearn.metrics.pairwise import pairwise_distances

def chatbot(user_input, lemmatized_name):
     query = user_input
     query1 = tokenise_word(user_input)

     #Question Answering Dataset
     query_vect1 = all_df_vect1.transform([query1]).toarray()
     query_sim1 = 1 - pairwise_distances(df1, query_vect1, metric='cosine')
     max_sim1 = np.where(query_sim1 == np.max(query_sim1, axis=0))
     index_output1 = np.random.choice(max_sim1[0])

     #Small Talk dataset
     query_vect2 = all_df_vect2.transform([query]).toarray()
     query_sim2 = 1 - pairwise_distances(df2, query_vect2, metric='cosine')
     max_sim2 = np.where(query_sim2 == np.max(query_sim2, axis=0))
     index_output2 = np.random.choice(max_sim2[0])

     #name context dataset
     query_vect3 = all_df_vect3.transform([query]).toarray()
     query_sim3 = 1 - pairwise_distances(df3, query_vect3, metric='cosine')
     max_sim3 = np.where(query_sim3 == np.max(query_sim3, axis=0))
     index_output3 = np.random.choice(max_sim3[0])
                    
     if 0.75 < query_sim2.max(): #small talk
          print("HaiHai bot: " + all_df2['Smalla'].loc[index_output2])
          return user_input
                    
     elif 0.88 < query_sim3.max(): #name context
          print(f"HaiHai bot: Your name is {lemmatized_name}")
          return user_input

     elif 0.2 < query_sim1.max(): #question answering
          print("HaiHai bot: " + all_df1['Answer'].loc[index_output1])
          return user_input
            
     #Reprompting -> Error handling        
     else:
          print("HaiHai bot: I'm sorry, i didn't quite catch that.")
          return user_input