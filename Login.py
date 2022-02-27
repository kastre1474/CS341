import tkinter as tk
from tkinter.font import Font
import os
import pyodbc
import User
import Conn
import Home



def init(root, user, conn):
    clearWin(root)
    if(user.userid != None):
        setuplogout(root, user, conn)
    else:
        setuplogin(root, user, conn)

def setuplogin(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda root: exitFullScreen(root))
    root.bind("<F1>", lambda root: enterFullScreen(root))
    #root.attributes("-fullscreen", True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Enter Your Email and Password", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l1 = tk.Label(root, text = "Email Address:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l2 = tk.Label(root, text = "Password:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te1 = tk.Text(root, height = 0, width = 0, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te2 = tk.Text(root, height = 0, width = 0, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b4 = tk.Button(root, text = 'Login', command = lambda: login(root, user, conn, te1, te2), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    l1.grid(row = 1, column = 3, columnspan = 1, sticky = tk.E, pady = 10)
    l2.grid(row = 2, column = 3, columnspan = 1, sticky = tk.E, pady = 10)
    te1.grid(row = 1, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
    te2.grid(row = 2, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
    b4.grid(row = 3, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)

def setuplogout(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda root: exitFullScreen(root))
    root.bind("<F1>", lambda root: enterFullScreen(root))
    #root.attributes("-fullscreen", True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Are You Sure You Want to Logout?", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = home(root), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)

def login(root, user, conn, email, pword):
    print(email.get())

def home(root, user, conn):
    Home.init(root, user, conn)

def exitFullScreen(root, event=None):
    root.attributes("-fullscreen", False)

def enterFullScreen(root, event=None):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()