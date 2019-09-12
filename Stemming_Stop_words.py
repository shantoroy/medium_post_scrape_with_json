import nltk
from nltk import PorterStemmer
from nltk import SnowballStemmer
from nltk import LancasterStemmer
import pandas as pd
import re

nltk.download('stopwords')
from nltk.corpus import stopwords

port = PorterStemmer()
# snowball = SnowballStemmer("english")
# lancaster = LancasterStemmer()
df = pd.read_csv('../Dataset/Joined_Question_Title_Answers_Tags_Comment_from_ETHEREUM.csv')
# print(df.head())
# exit(0)

sw_set = set(stopwords.words('english'))

#print("stop words:\n {}")
#print(sw_set)

# df = pd.read_csv('../../DataSheets/WithoutBlockchain/Dataset/CleanedDataset_Question.csv')
#
# text_col = df['Cleaned_TitleTextBody']
#
# text_tokenize = text_col.apply(nltk.word_tokenize)
# print(text_tokenize[4])


def clean_tokenized(col_name, new_col_name, stemming_method):
    df[new_col_name] = df[col_name].apply(nltk.word_tokenize)

    df[new_col_name] = df[new_col_name].apply(lambda x: [w.lower() for w in x if w.isalpha()])

    df[new_col_name] = df[new_col_name].apply(lambda x: [w for w in x if not w in sw_set])

    df[new_col_name] = df[new_col_name].apply(lambda x: [stemming_method(w) for w in x])


clean_tokenized('Question_Title_Answers_Tags_Comment', 'CleanStopWords_PorterStemming_TextBody', port.stem)
# clean_tokenized('Cleaned_TitleTextBody', 'CleanStopWords_SnowballStemming_TextBody', snowball.stem)
# clean_tokenized('Cleaned_TitleTextBody', 'CleanStopWords_LancasterStemming_TextBody', lancaster.stem)




print( df['CleanStopWords_PorterStemming_TextBody'][1])
# print(df['CleanStopWords_SnowballStemming_TextBody'][1])
# print(df['CleanStopWords_LancasterStemming_TextBody'][1])

df.to_csv('../Dataset/AfterStemming_Joined_Question_Title_Answers_Tags_Comment_from_ETHEREUM.csv')