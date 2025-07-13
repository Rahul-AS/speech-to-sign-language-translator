from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
import re

#Remove the filler words and find the root word
def TextAnalyse(text):

	#We extract only the alphabets and numbers from the given text 
	#This removes the punctuations and special characters from the text
    letnum_text =  re.sub("[^a-zA-Z0-9]+", " ",text)

    #The sentence is break down based on the space into single words
    word_tokens = word_tokenize(letnum_text)

    #This are filler words which has no meaning in the sentence
    stop_words = [ 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'a', 'an', 'the', 'and', 'as', 'of', 'at', 'by', 'for', 'so']
    
    #Removes the filler words from the sentence
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    #Initialize the Porter Stemmer Algorithm
    ps = PorterStemmer()

    #Some errors in the Porter Stemmer Algorithm is rectified
    filtered_sentence = [w if w[-2:] != 'ly' else w[:-2] for w in filtered_sentence]

    #Find the root words
    #for example words like created, creates is reduces to create
    root_words = [ps.stem(w) for w in filtered_sentence]

    #Mis assumptions done by Porter Stemmer is rectified
    for ind in range(len(root_words)):
    	if root_words[ind] == filtered_sentence[ind][:-1]:
    		root_words[ind] = filtered_sentence[ind]
    #Return the Processed sentence 
    return ' '.join(filtered_sentence).replace('your','you')

