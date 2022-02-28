import tkinter as tk
from tkinter.font import Font
import os
import pyodbc
import User
import Conn
import Home
import Programs

def init(root, user, conn):
    clearWin(root)
    if(user.userid != None):
        setuplogout(root, user, conn)
    else:
        setuplogin(root, user, conn)

def setuplogin(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.attributes("-fullscreen", True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Enter Your Email and Password", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    if(user.userid != None):
        canvas.create_text(80, 10, text="Signed in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l1 = tk.Label(root, text = "Email Address:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l2 = tk.Label(root, text = "Password:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te1 = tk.Entry(root, width = 0, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te2 = tk.Entry(root,  width = 0, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    inclabel = tk.Label(root, text = "", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b4 = tk.Button(root, text = 'Login', command = lambda: login(root, user, conn, te1, te2, inclabel), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    l1.grid(row = 1, column = 3, columnspan = 1, sticky = tk.E, pady = 10)
    l2.grid(row = 2, column = 3, columnspan = 1, sticky = tk.E, pady = 10)
    te1.grid(row = 1, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
    te2.grid(row = 2, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
    b4.grid(row = 3, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
    inclabel.grid(row = 3, column = 3, columnspan = 1, sticky = tk.E, pady = 10)

def setuplogout(root, user, conn):
    root.configure(background = 'white')
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.attributes("-fullscreen", True)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="Are You Sure You Want to Logout?", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    if(user.userid != None):
        canvas.create_text(80, 10, text="Signed in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
    canvas.grid(row = 0, column = 0, columnspan = 11)
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b4 = tk.Button(root, text = 'Log Out', command = lambda: logout(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    b4.grid(row = 2, column = 4, columnspan = 3, sticky = tk.W+tk.E, pady = 10)
 
def login(root, user, conn, email, pword, inclabel):
    conn.cursor.execute("SELECT * FROM dbo.[User] WHERE EMAIL='{}' AND PASSWORD='{}'".format(email.get(), pword.get()))
    if(conn.cursor.rowcount == 0):
        inclabel.config(text="Email or Password Incorrect")
        email.delete(0, 'end')
        pword.delete(0, 'end')
    else:
        userinfo = conn.cursor.fetchone()
        user.signin(userinfo[0],userinfo[1],userinfo[2],userinfo[3],userinfo[4],userinfo[5],userinfo[6])
        inclabel.config(text="")
        email.delete(0, 'end')
        pword.delete(0, 'end')
        Home.init(root, user, conn)

def logout(root, user, conn):
    user.signout()
    Home.init(root, user, conn)
    
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