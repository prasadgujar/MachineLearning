import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#documents = []

#for category in movie_reviews.categories():
#    for field in movie_reviews.fileids(category):
#       documents.append(list(movie_reviews.words(field)), cateogry)

#shuffle the data
random.shuffle(documents)

#print the data
#print(documents[1])

# store the all words in the list
all_words = []

# make all words lower_case
for w in movie_reviews.words():
    all_words.append(w.lower())

#find the frequency of all words
all_words = nltk.FreqDist(all_words)
print (all_words.most_common(5)) #print the no of required

#check the frequency of specific word
print(all_words["good"])
