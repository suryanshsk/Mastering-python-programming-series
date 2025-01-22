import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

text = "Natural language processing is a fascinating field of AI"
tokens = word_tokenize(text)
tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]

print(tokens)  