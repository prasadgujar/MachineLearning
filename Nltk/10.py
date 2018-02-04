from nltk.corpus import wordnet

syns = wordnet.synsets("program")


#print the all word from list - synset
print (syns)
#print the nth word from list
print (syns[0])

#lemmas
print(syns[0].lemmas())

#just the word
print(syns[0].lemmas()[0].name())

#definition

print(syns[0].definition())

#example

print(syns[0].examples())


synonyms = [] # similar or close to particular word meaning
antonyms = [] # opposite word

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        #print("l:",l)   #uncomment this line if you want to print the list format or all synonyms of given word.
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

#print the set of synonyms
#print (set(synonyms))

#print the set of anonyms
#print (set(antonyms))

# find whether two words are similar or not and their %.
w1  =  wordnet.synset("ship.n.01") #word1 
w2  =  wordnet.synset("boat.n.01") #word2

#print the accuracy between two words
print (w1.wup_similarity(w2))


# find whether two words are similar or not and their %.
w1  =  wordnet.synset("ship.n.01") #word1 
w2  =  wordnet.synset("cat.n.01") #word2

#print the accuracy between two words
print (w1.wup_similarity(w2))


# find whether two words are similar or not and their %.
w1  =  wordnet.synset("nerd.n.01") #word1 
w2  =  wordnet.synset("crush.n.01") #word2

#print the accuracy between two words
print (w1.wup_similarity(w2))
