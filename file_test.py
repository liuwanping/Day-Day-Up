import re
import nltk
from nltk.stem.porter import PorterStemmer  

# s = nltk.stem.SnowballStemmer('english')  
porter_stemmer = PorterStemmer()
dictio = {}
file = open('1960-09-26.txt')
content = file.readlines()
sentence = " ".join(content)
for word in sentence.split():
	w = porter_stemmer.stem(word)
	print(w)
	# dictio[w] = 1
# print(dictio)

# query = "she says: I am a girls', and he was a boy!%$"
# q = re.sub('[^A-Za-z0-9 ]+', '', query)
# print(q)



print(porter_stemmer.stem('subjects'))