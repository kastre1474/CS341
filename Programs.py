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
import CreateProgram

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
    if(user.type == 'S'):
        b5 = tk.Button(root, text = 'Create Program', command = lambda:createProgram(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))  
        b5.grid(row = 5, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    setUpTree(root, conn)
    
def setUpTree(root, conn):
    columns = ('Course Name', 'Course Description', 'Day', 'Time', 'Length','Location', 'Member Fee', 'Non Member Fee')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading('Course Name', text='Course Name')
    tree.heading('Course Description', text='Course Description')
    tree.heading('Day', text='Day')
    tree.heading('Time', text='Time')
    tree.heading('Length', text='Length')
    tree.heading('Location', text='Location')
    tree.heading('Member Fee', text='Member Fee')
    tree.heading('Non Member Fee', text='Non Member Fee')
    contacts = []
    for prog in getprogs(conn):
        contacts.append((prog[2], prog[1], prog[9], prog[5], prog[8], prog[3], prog[4], prog[4] * 2))
    for contact in contacts:
        tree.insert('', tk.END, values=contact)
    tree.grid(rowspan = 4,row = 1, column = 1, padx = 10, pady = 10, sticky='nsew')
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(rowspan = 4, row = 1, column = 2, sticky='ns')
   
def getprogs(conn):
    conn.cursor.execute("SELECT * FROM dbo.[Program]")
    rows = conn.cursor.fetchall()
    return rows
    
def login(root, user, conn):
    Login.init(root, user, conn)

def home(root, user, conn):
    Home.init(root, user, conn)

def createProgram(root, user, conn):
    CreateProgram.init(root, user, conn)

def exitFullScreen(e, root):
    root.attributes("-fullscreen", False)

def enterFullScreen(e, root):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()
