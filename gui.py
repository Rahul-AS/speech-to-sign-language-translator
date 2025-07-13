import speech_recognition as sr
import tkinter as tk
from tkinter.ttk import Label
from text import *
from sign import *

#create a 400X400 frame and name the title as 'Speech to Sign Language'
obj = tk.Tk()
obj.title("Speech To Sign Language")
obj.geometry('400x400')
obj.resizable(0,0)

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
            audio = r.listen(source)
            print('Listened')

            # Using google to recognize audio 
            MyText = r.recognize_google(audio, language = 'en-IN') 

            print('Recognized')

            print('Did you say ' + MyText)

            MyText = MyText.lower() 

            #Analysing the text
            MyText = TextAnalyse(MyText)

            #Print the text in the gui frame
            msg.configure(text=MyText)

            #Iterate through every word and play the according Sign Language
            for w in MyText.split():
                playVideo(w)


    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
            
    except sr.UnknownValueError: 
        print("Could not understand audio") 



msg = tk.Label()
msg.grid(row=0,column=0)

#Print the text in the Front End
Label(msg, text="Speech To Sign Language",font=("Arial", 25),justify = 'center').pack(pady=20)

#Create the Button in the GUI with onClick action to call the rec function
btn = tk.Button(text="Record",command=rec,height = 5, width = 20, bg='#b5b5f2')
btn.place(relx=0.3, rely=0.5)

#Starts the GUI
obj.mainloop()