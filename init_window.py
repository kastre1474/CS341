import tkinter as tk
from tkinter.font import Font
import os
import pyodbc

conn = None
window = None
mode = None
user = -1

def exitFullScreen(event=None):
    global window
    window.attributes("-fullscreen", False)

def enterFullScreen(event=None):
    global window
    window.attributes("-fullscreen", True)
    
def clearWindow():
    global window
    for widget in window.winfo_children():
        widget.destroy()

def setupWindow():
    global window
    window.configure(background = 'white')
    window.bind("<Escape>", exitFullScreen)
    window.bind("<F1>", enterFullScreen)
    window.attributes("-fullscreen", True)
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    canvas = tk.Canvas(window, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Welcome To The YMCA", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    buttonOptions()

def buttonOptions(i = -1):
    if i == -1:
        b1 = tk.Button(window, text = 'Home', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b2 = tk.Button(window, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b3 = tk.Button(window, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b4 = tk.Button(window, text = 'Login/SignUp', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    elif i == 0:
        pass
    elif i == 1:
        pass
    else:
        pass
    

def createPage():

    global window
    window = tk.Tk()
    setupWindow()
    window.mainloop()
 




