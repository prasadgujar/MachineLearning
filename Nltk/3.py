#stemming- ex- riding->rid.
#example:-
#i was taking a ride in the car
#i was riding in the car.
#algorith--Porter Stemmer

from nltk.stem import PorterStemmer
from nltk.tokenize  import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

#for w in  example_words:
#   print (ps.stem(w))


new_text = "it is very importance to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words =  word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
