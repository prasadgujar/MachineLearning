import nltk
import pickle
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB,GaussianNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

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

word_features = list(all_words.keys())[:3000]

def find_features(document):
    words  = set(document) 
    features = {}
    for w in word_features:
        features[w] = (w in words) 
    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev, category) in documents]
        
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

##uncomment this for randomness and naive_bayes
#classifier = nltk.NaiveBayesClassifier.train(training_set)

## for differen/random dataset comment classifiers
#it is used to store the dataset/training/testing
classifier_f = open("naivebayes.pickle","rb") #rb= read byte
classifier = pickle.load(classifier_f)
classifier_f.close()
#posterior  = prior occurence x likilhood / evidence

#classifier = nltk.NaiveBayesClassifier.train(training_set)
print(' Original Naive Bayes Algo accuracy:', (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)


# save the dataset using pickle package
#save_classifier = open("naivebayes.pickle","wb") #wb=write_bayes
#pickle.dump(classifier,save_classifier)
#save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print(' MNB Naive Bayes Algo accuracy:', (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

#GaussianNB , BernoulliNB

#GaussianNB_classifier = SklearnClassifier(GaussianNB())
#GaussianNB_classifier.train(training_set)
#print(' Gaussian Naive Bayes Algo accuracy:', (nltk.classify.accuracy(GaussianNB_classifier, testing_set))*100)


BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print(' Bernoulli Naive Bayes Algo accuracy:', (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)


#from sklearn.linear_model import LogisticRegression, SGDClassifier
#from sklearn.svm import SVC, linearSVC, NuSVC

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print(' LogisticRegression Algo accuracy:', (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)


SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print(' SVC Classifier accuracy:', (nltk.classify.accuracy(SVC_classifier, testing_set))*100)


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print(' linearSVC classifier accuracy:', (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print(' NuSVC Classifier accuracy:', (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)



