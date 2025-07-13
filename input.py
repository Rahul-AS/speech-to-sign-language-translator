import tkinter as tk
from tkinter.ttk import Label
import tkinter.font as font

#Create a Frame
obj = tk.Tk()
obj.title("Speech To Sign Language")
obj.geometry('500x500')
obj.resizable(0,0)


msg = tk.Label()
msg.grid(row=0,column=0)
myFont = font.Font(size=10)
Label(msg, text="Speech To Sign Language",font=("Arial", 25)).pack(pady=20)
btn = tk.Button(text="Text",height = 3, width = 30, bg='#b5b5f2')
btn.place(relx=0.2, rely=0.3)
btn['font'] = myFont
btn = tk.Button(text="Live Speech",height = 3, width = 30, bg='#b5b5f2')
btn.place(relx=0.2, rely=0.5)
btn['font'] = myFont
btn = tk.Button(text="Recorded Audio",height = 3, width = 30, bg='#b5b5f2')
btn.place(relx=0.2, rely=0.7)
btn['font'] = myFont
obj.mainloop()