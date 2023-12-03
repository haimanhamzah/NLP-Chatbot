import random
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances

#Pre processing the document
lemmatiser = WordNetLemmatizer()

def process(user_input):   
     #Tokenizes the sentence 
     post_tokens = nltk.word_tokenize(user_input) 
     
     #does pos tag on it for named entity recognition
     post_word = nltk.pos_tag(post_tokens)
     
     #detects the name in the sentence
     detected_names_nltk = [name.title() for name, pos in post_word if pos == 'NNP' or pos == 'JJ' or pos == 'ADJ']
     print(post_word)
     
     return detected_names_nltk


def qa_lemma(user):
     posmap = {
          'ADJ' : 'a',
          'ADV' : 'r',
          'NOUN' : 'n',
          'VERB' : 'v'
     }
     
     post = nltk.pos_tag(word_tokenize(user), tagset='universal')

     for token in post:
          word = token[0]
          tag = token[1]
          if tag in posmap.keys():
               lemma1 = lemmatiser.lemmatize(word, posmap[tag])
               return(lemma1)
          else:
               lemma2 = lemmatiser.lemmatize(word)
               return(lemma2)
          

          
# test(sentence)
# def tokenise(user_input):
#      text_token  = word_tokenize(user_input) #input tokenized
#      print(text_token)
#      tokens_without_sw = [word.lower() for word in text_token if not word in stopwords.words('english') and word.isalpha()]
#      print(tokens_without_sw)
#      filtered_sentence = (" ").join(tokens_without_sw)
#      print(filtered_sentence)
#      return filtered_sentence

# user_input = "what can you do?"
# tokenise(user_input)

#----------------------------------------------------------------------------------------------------------------

#Read the csv files
all_df = pd.read_csv("transaction_response.csv")
all_df_vect = TfidfVectorizer(analyzer='word', use_idf=True, smooth_idf=True, sublinear_tf=True)
all_df_tfidf = all_df_vect.fit_transform(all_df['Input']).toarray()
df = pd.DataFrame(all_df_tfidf, columns=all_df_vect.get_feature_names_out())

all_df1 = pd.read_csv("qa.csv")
all_df_vect1 = TfidfVectorizer(analyzer='word', use_idf=True, smooth_idf=True, sublinear_tf=True)
all_df_tfidf1 = all_df_vect1.fit_transform(all_df1['Question']).toarray()
df1 = pd.DataFrame(all_df_tfidf1, columns=all_df_vect1.get_feature_names_out())

all_df2 = pd.read_csv("small_talk.csv")
all_df_vect2 = TfidfVectorizer(analyzer='word', use_idf=True, smooth_idf=True, sublinear_tf=True)
all_df_tfidf2 = all_df_vect2.fit_transform(all_df2['Smallq']).toarray()
df2 = pd.DataFrame(all_df_tfidf2, columns=all_df_vect2.get_feature_names_out())

all_df3 = pd.read_csv("name.csv")
all_df_vect3 = TfidfVectorizer(analyzer='word', use_idf=True, smooth_idf=True, sublinear_tf=True)
all_df_tfidf3 = all_df_vect3.fit_transform(all_df3['Question']).toarray()
df3 = pd.DataFrame(all_df_tfidf3, columns=all_df_vect3.get_feature_names_out())

# #--------------------------------------------------------------------------------------------------------------

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
                   
 
def main():
     # user_hashmap = {'name': ''}
     user_name = input("HaiHai bot: Hello! what's your name? (Press Ctrl+C to exit)")
     lemmatized_name = process(user_name)
     lemmatized_name = ''.join(lemmatized_name)
     print(f"HaiHai bot: Hi there, Nice to meet you, {lemmatized_name}!, How can i assist you today? (Type exit to quit)")
     
     flag = True
     while(flag == True):
          user_input = input("You: ")
          if user_input == ("exit"):
               print("Have a nice day!")
               break
          else:
               query = user_input
               query1 = qa_lemma(user_input)
               
     
               query_vect = all_df_vect.transform([query]).toarray()
               query_sim = 1 - pairwise_distances(df, query_vect, metric='cosine')
               max_sim = np.where(query_sim == np.max(query_sim, axis=0))
               index_output = np.random.choice(max_sim[0])
               
               query_vect1 = all_df_vect1.transform([query1]).toarray()
               query_sim1 = 1 - pairwise_distances(df1, query_vect1, metric='cosine')
               max_sim1 = np.where(query_sim1 == np.max(query_sim1, axis=0))
               index_output1 = np.random.choice(max_sim1[0])
               
               query_vect2 = all_df_vect2.transform([query]).toarray()
               query_sim2 = 1 - pairwise_distances(df2, query_vect2, metric='cosine')
               max_sim2 = np.where(query_sim2 == np.max(query_sim2, axis=0))
               index_output2 = np.random.choice(max_sim2[0])
               
               query_vect3 = all_df_vect3.transform([query]).toarray()
               query_sim3 = 1 - pairwise_distances(df3, query_vect3, metric='cosine')
               max_sim3 = np.where(query_sim3 == np.max(query_sim3, axis=0))
               index_output3 = np.random.choice(max_sim3[0])
               
               
               if 0.7 < query_sim.max():
                    print(all_df['Output'].loc[index_output])
                    
               elif 0.7 < query_sim2.max():
                    print(all_df2['Smalla'].loc[index_output2])
                    
               elif 0.7 < query_sim3.max():
                    print(f"Your name is {lemmatized_name}")
               
               elif 0.2 < query_sim1.max():
                    print(all_df1['Answer'].loc[index_output1])
                    
               else:
                    print("I'm sorry, i didn't quite catch that.")
               
#                # final_output = intent_matching(user_input,
#                #                               [df, df1, df2],
#                #                               [all_df, all_df1, all_df2],
#                #                               ['Output', 'Answer', 'Smalla'],
#                #                               threshold=0.75)
               
#                # if final_output is None:
#                #      print("Haihai Bot: I'm sorry, i couldn't quite catch that. Can you please say it again?")
#                # else:
#               #      print(f"Haihai Bot: {final_output}")
     
     
          
          
if __name__ == "__main__":
     main()
 