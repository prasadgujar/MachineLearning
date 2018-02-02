from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#stop words are the words which are not usefully// removing those words not change the meaning of sentence.
example_sentence =  "This is an example showing off word filtration."

#stop_words
stop_words = set(stopwords.words("english"))

#print the available stop_words
print(stop_words)

#tokenize all words 
words = word_tokenize(example_sentence)

#list for storing all words
filtered_sentence = []

#check if word is stop word or not if not then append to list
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(filtered_sentence)

#one liner in python
#filtered_sentence =  [w for w in words if not w in stop_words]

#print(filtered_sentence)
