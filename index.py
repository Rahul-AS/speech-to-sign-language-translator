# Python program to translate 
# speech to text and text to speech 

import speech_recognition as sr 
import pyttsx3 
from text import *
from sign import *
from webscrap import *
import time

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to 
# speech 
def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait()


#Function to Analyse the text and convert the text to Sign Language
def convertToSign(MyText):
	#start = time.time()
	MyText = MyText.lower() 

	#Analyse the text
	MyText = TextAnalyse(MyText)
	#end = time.time()

	#print('Text Analysis:',end - start)

	#Iterate every word in the Processed text and play the Sign Language video
	for w in MyText.split():

		#playVideo Function returns a value 1 if the word is found in the local system otherwise None
		val = playVideo(w)

		if val == 1:
			findInDictionary(w)

	#end = time.time()
	#print('Text to Sign Time taken:', end - start)


#Ask for the choice to the user to choose the type of input
while(1):	
	print('Enter the choice')
	print('1 for text to sign language conversion')
	print('2 for audio to sign language conversion')
	print('3 for exit')

	choice = int(input())

	#if input of choice is 1, then the type of input is text
	#So we directly convert the text to Sign Language
	if choice == 1:
		MyText = input().strip()
		convertToSign(MyText)

	#if the input of choice is 2, then the type of input is Speech
	#Here the Speech is converted to text and then converted to Sign Language
	elif choice == 2:

		try: 	
			# use the microphone as source for input. 
			with sr.Microphone() as source2: 
				
				#start = time.time()

				# wait for a second to let the recognizer 
				# adjust the energy threshold based on 
				# the surrounding noise level 
				r.adjust_for_ambient_noise(source2, duration=0.2)

				print()
				print()
				print('Speak now')

				#listens for the user's input 
				audio2 = r.listen(source2, phrase_time_limit = 10) 
				print('Listened')


				# Using google to recognize audio 
				MyText = r.recognize_google(audio2, language = 'en-IN') 

				print('Recognized')

				print('Did you say ' + MyText)
				print()
				print()
				
				#Here the Function process and convert the recognized text to Sign Language
				convertToSign(MyText)

				
				print("Tell 'exit' to end")
				if MyText == 'exit':
					break
		except sr.RequestError as e: 
			print("Could not request results; {0}".format(e)) 
			
		except sr.UnknownValueError: 
			print("Could not understand audio") 

	#if the choice is other than 1 or 2, we exit the program
	else:
		exit()

