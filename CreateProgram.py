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
import Programs

def init(root, user, conn):
    clearWin(root)
    setup(root, user, conn)

def setup(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Create New Program", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    if(user.userid != None):
        canvas.create_text(80, 10, text="Signed in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    logintext = 'Login/SignUp' if user.userid == None else 'Sign Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N, pady = 10)
    entryFields = ['Class Name:', 'Class Description:', 'Location:','Member Fee:', 'Time:', 'Start Date:', 'End Date:', 'Day of the Week:', 'Length in Minutes:', 'Number of Spots:']
    bgFrame = tk.Frame(root, width=screenWidth)
    bgFrame.grid(row = 1, column = 3, rowspan = 4, sticky = tk.W)
    for i in range(len(entryFields)):
        label = tk.Label(bgFrame, text = entryFields[i], bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
        te = tk.Entry(bgFrame, font = Font(family = "Helvetica", size = 20, weight = "bold"))
        label.grid(row = i, column = 0, sticky = tk.E, pady = 10)
        te.grid(row = i, column = 1, sticky = tk.W, pady = 10, padx = 10)
    b5 = tk.Button(bgFrame, text = 'Submit', command = lambda:addNewProg(bgFrame, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b5.grid(row = i, column = 3, columnspan = 2)

def addNewProg(bgFrame, user, conn):
    entryBoxes = bgFrame.winfo_children()
    entries = []
    for entry in entryBoxes:
        if(entry.winfo_class() == 'Entry'):
            entries.append(entry.get())
            entry.delete(0, 'end')
    print(entries)
    query1 = "INSERT INTO dbo.Program ([DESCRIPTION], [NAME], LOCATION, FEE, [TIME], STARTDATE, ENDDATE, [LENGTH], [DAY], SIZE, USERID)"
    query2 = "VALUES ('{}','{}','{}',{},'{}','{}','{}',{},{},{},{})"
    query2 = query2.format(entries[1], entries[0], entries[2], int(entries[3]), entries[4], entries[5], entries[6],int(entries[8]), int(entries[7]), int(entries[9]), user.userid)
    conn.cursor.execute(query1 + ' ' + query2)           
    conn.conn.commit()

def login(root, user, conn):
    Login.init(root, user, conn)

def home(root, user, conn):
    Home.init(root, user, conn)

def programs(root, user, conn):
    Programs.init(root, user, conn)

def exitFullScreen(e, root):
    root.attributes("-fullscreen", False)

def enterFullScreen(e, root):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()