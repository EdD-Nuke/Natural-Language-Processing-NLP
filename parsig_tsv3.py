
import pandas as pd


filename = 'nlmaps.tsv'
file = open(filename, 'rt')
text = file.read()
file.close()
# split into words
from re import split
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to upper case
tokens = [w.upper() for w in tokens]
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print(words[:])

# df = pd.read_csv(filename)
# saved_column = df.column_name #you can also use df['column_name']


# for k in range(len(words)):
#     if len(words[k]) <= 2:
#         for j in range(k):
#             words.append(words[j]) #This line is storing as letters.

