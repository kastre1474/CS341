import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import os
import pyodbc
import User
import Conn
import Home
import Login
import Conn



def init(root, user, conn):
    clearWin(root)
    setupprog(root, user, conn)

def setupprog(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="YMCA Programs", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    if(user.userid != None):
        canvas.create_text(80, 10, text="Signed in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    logintext = 'Login/SignUp' if user.userid == None else 'Sign Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    wrapper1 = LabelFrame(root)
    my_canvas = Canvas(wrapper1)
    my_canvas.pack(side=LEFT, fill = "both", expand="yes")
    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=my_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")
    my_canvas.configure(yscrollcommand=yscrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    myframe = Frame(my_canvas)
    my_canvas.create_window((0,0), window=myframe, anchor="nw")
    wrapper1.grid(row = 1, column = 1, rowspan = 4, columnspan = 4, padx=10, pady= 10)
    for prog in getprogs(conn):
        tk.Label(myframe, text = prog[2] + '-' + prog[1]).pack(anchor="w")

def getprogs(conn):
    conn.cursor.execute("SELECT * FROM dbo.[Program]")
    rows = conn.cursor.fetchall()
    return rows
    
def login(root, user, conn):
    Login.init(root, user, conn)

def home(root, user, conn):
    Home.init(root, user, conn)

def exitFullScreen(e, root):
    root.attributes("-fullscreen", False)

def enterFullScreen(e, root):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()