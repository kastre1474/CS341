import tkinter as tk
from tkinter.font import Font
import os
import pyodbc
import User
import Conn
import Login
import Programs
import CreateProgram

def init(root, user, conn):
    clearWin(root)
    setup(root, user)
    buttonOptions(root, user, conn)
    
def setup(root, user):
    root.title("YMCA")
    for i in range(11):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)
    root.configure(background = 'white')
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.attributes("-fullscreen", True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')  
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Welcome To The YMCA", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    if(user.userid != None):
        canvas.create_text(80, 10, text="Signed in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
        
def buttonOptions(root, user, conn):
    b1 = tk.Button(root, text = 'Home', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    logintext = 'Login/SignUp' if user.userid == None else 'Sign Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    if(user.type == 'S'):
        b5 = tk.Button(root, text = 'Create Program', command = lambda:createProgram(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))  
        b5.grid(row = 5, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)

def login(root, user, conn):
    Login.init(root, user, conn)

def programs(root, user, conn):
    Programs.init(root, user, conn)

def createProgram(root, user, conn):
    CreateProgram.init(root, user, conn)
    
def exitFullScreen(e, root):
    root.attributes("-fullscreen", False)

def enterFullScreen(e, root):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()
        

 




