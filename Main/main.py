import tkinter as tk
from tkinter import ttk
import re
from text import *
from convertToSign import *
from record import *

LARGEFONT =("Verdana", 20)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Main, Input, Text, Live, Record):

			frame = F(container, self)

			# initializing frame of that object from
			# Main, Input, Text respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(Main)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame Main
class Main(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = tk.Label(self, text ="Speech to Sign Language Translator", font = LARGEFONT)
		
		# putting the pack in its place by using
		# pack
		label.pack(padx = 20, pady = 10)

		button1 = tk.Button(self, text ="Get Started!",
		command = lambda : controller.show_frame(Input), height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button1.pack(padx = 10, pady = 10)



# second window frame Input
class Input(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text ="Speech to Sign Language Translator", font = LARGEFONT)
		label.pack( padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = tk.Button(self, text ="Text",
							command = lambda : controller.show_frame(Text), height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button2.pack( padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button3 = tk.Button(self, text ="Live Speech",
							command = lambda : controller.show_frame(Live), height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button3.pack( padx = 10, pady = 10)

		# button to show frame 4 with text
		# layout4
		button4 = tk.Button(self, text ="Recorded Audio",
							command = lambda : controller.show_frame(Record), height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button4.pack( padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="Exit",
							command = self.quit, height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place
		# by using pack
		button1.pack(padx = 10, pady = 10)

	def quit(self):
		app.destroy()



# third window frame Text
class Text(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text ="Speech to Sign Language Translator", font = LARGEFONT)
		label.pack(padx = 10, pady = 10)

		self.T = tk.Text(self, height = 5, width = 52)

		self.T.pack()

		# button to show frame 2 with text
		# layout2
		button1 = tk.Button(self, text ="Translate the text",
							command = self.getTextInput, height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button1.pack( padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = tk.Button(self, text ="Back",
							command = lambda : controller.show_frame(Input), height = 3, width = 30, bg='#b5b5f2')
	
		# putting the button in its place by
		# using pack
		button2.pack( padx = 10, pady = 10)

	def getTextInput(self):
		text = self.T.get("1.0","end")
		convertToSign(text)

#Fourth window frame Live
class Live(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = tk.Label(self, text ="Speech to Sign Language Translator", font = LARGEFONT)
         
        # putting the pack in its place by using
        # pack
        label.pack( padx = 10, pady = 10)
  
        button1 = tk.Button(self, text ="Record",
        command = self.SpeechToSign, height = 3, width = 30, bg='#b5b5f2')
     
        # putting the button in its place by
        # using pack
        button1.pack( padx = 10, pady = 10)

         ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Back",
        command = lambda : controller.show_frame(Input), height = 3, width = 30, bg='#b5b5f2')
     
        # putting the button in its place by
        # using pack
        button2.pack( padx = 10, pady = 10)

    def SpeechToSign(self):
    	rec()

#Fifth Window frame record
class Record(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = tk.Label(self, text ="Speech to Sign Language Translator", font = LARGEFONT)
         
        # putting the pack in its place by using
        # pack
        label.pack( padx = 10, pady = 10)

        self.T = tk.Text(self, height = 5, width = 52)

        self.T.pack()

        button1 = tk.Button(self, text ="Translate the Audio",
        command = self.getTextInput , height = 3, width = 30, bg='#b5b5f2')
     
        # putting the button in its place by
        # using pack
        button1.pack( padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Back",
        command = lambda : controller.show_frame(Input), height = 3, width = 30, bg='#b5b5f2')
     
        # putting the button in its place by
        # using pack
        button2.pack( padx = 10, pady = 10)

    def getTextInput(self):
    	text = self.T.get("1.0","end").strip()
    	text = re.sub(r'[\n\r\t]', '', text)
    	recorded(text)


# Driver Code
app = tkinterApp()
app.mainloop()
