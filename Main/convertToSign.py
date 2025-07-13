import speech_recognition as sr
from text import *
from sign import *
from database import *
import time

#Activate the microphone and records the voice and converts the speech to text
def rec():
    #initialize the Speech recognizer
    r = sr.Recognizer()
    
    try:
        #Activate the microphone
        with sr.Microphone() as source:
            #Adjust the background noise
            r.adjust_for_ambient_noise(source)

            #Records the speech
            audio = r.listen(source, phrase_time_limit = 10)
            print('Listened')

            # Using google to recognize audio 
            MyText = r.recognize_google(audio, language = 'en-IN') 

            print('Recognized')

            print('Did you say ' + MyText)

            convertToSign(MyText)


    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
            
    except sr.UnknownValueError: 
        print("Could not understand audio")


#Function to Analyse the text and convert the text to Sign Language
def convertToSign(MyText):
    #start = time.time()
    MyText = MyText.lower() 

    #Analyse the text
    MyText = TextAnalyse(MyText)

    #Iterate every word in the Processed text and play the Sign Language video
    for w in MyText.split():

        #playVideo Function returns a value 1 if the word is found in the local system otherwise None
        val = playVideo(w)
        
        if val == 1:
            if findInDictionary(w) == 1:
                for char in w:
                    playVideo(char.upper())