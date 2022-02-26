import tkinter as tk
from tkinter.font import Font
import os
import pyodbc


class initwin():

    def __init__(self, root):
        self.win = root
        self.setup()
        self.buttonOptions()
    
    def setup(self):
        self.win.configure(background = 'white')
        self.win.bind("<Escape>", self.exitFullScreen)
        self.win.bind("<F1>", self.enterFullScreen)
        self.win.attributes("-fullscreen", True)
        screenWidth = self.win.winfo_screenwidth()
        screenHeight = self.win.winfo_screenheight()
        canvas = tk.Canvas(self.win, width= screenWidth, height= screenHeight / 10, bg='cyan')
        canvas.create_text(screenWidth / 2, screenHeight / 20, text="Welcome To The YMCA", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
        canvas.grid(row = 0, column = 0, columnspan = 11)
        
    def buttonOptions(self):
        b1 = tk.Button(self.win, text = 'Home', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b2 = tk.Button(self.win, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b3 = tk.Button(self.win, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b4 = tk.Button(self.win, text = 'Login/SignUp', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
        
    def exitFullScreen(self, event=None):
        self.win.attributes("-fullscreen", False)

    def enterFullScreen(self, event=None):
        self.win.attributes("-fullscreen", True)
        

 




