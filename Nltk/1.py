#import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
#nltk.download()


#tokenizing - word tokenizing and sentence tokenizing
#corpora - body of text: ex: medical journals, prersidental speech
#lexicon - word and their means

#invester-speak .. regular english-speak

#investor speak 'bull' =  someone who is positive about market

#english-speak 'bull' = scary animal you don't want running

example_text = "Hello Mr.Berde, there, how are you  doing today?  The weather is great and python is awesome. The sky is pinkish-blue. you should not eat cardboard"

#print sentence that will separted by space using sent_tokenize
print(sent_tokenize(example_text))

#print word without space using word_tokenize
print(word_tokenize(example_text))

#print word to newline using for-loop
for i in word_tokenize(example_text):
    print (i)
