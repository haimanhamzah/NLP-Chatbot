import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

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

all_df4 = pd.read_csv("sentiment_analysis.csv")
positive = all_df4['positive'].tolist()
negative = all_df4['negative'].tolist()

all_df5 = pd.read_csv("random_joke.csv")
jokes = all_df5['jokes'].tolist()
