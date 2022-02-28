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
    # root.configure(background = 'white')
    # root.bind("<Escape>", lambda root: exitFullScreen(root))
    # root.bind("<F1>", lambda root: enterFullScreen(root))
    # #root.attributes("-fullscreen", True)
    # screenWidth = root.winfo_screenwidth()
    # screenHeight = root.winfo_screenheight()
    # canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    # canvas.create_text(screenWidth / 2, screenHeight / 20, text="YMCA Programs", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    # canvas.grid(row = 0, column = 0, columnspan = 11)
    # b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    # b2 = tk.Button(root, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    # b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    # logintext = 'Login/SignUp' if user.userid == None else 'Sign Out'
    # b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    # b1.grid(row = 1, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    # b2.grid(row = 2, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    # b3.grid(row = 3, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    # b4.grid(row = 4, column = 0, columnspan = 1, sticky = tk.W+tk.E, pady = 10)
    # getprogs(conn)

    root.configure(background = 'white')
    root.bind("<Escape>", lambda root: exitFullScreen(root))
    root.bind("<F1>", lambda root: enterFullScreen(root))
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    canvas = tk.Canvas(root, width= screenWidth, height= screenHeight / 10, bg='cyan')
    canvas.pack()
    canvas.create_text(screenWidth / 2, screenHeight / 20, text="YMCA Programs", fill="Black", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    canvas.pack()

    wrapper1 = LabelFrame(root)
    wrapper2 = LabelFrame(root)

    my_canvas = Canvas(wrapper1)
    my_canvas.pack(side=LEFT, fill = "both", expand="yes")

    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=my_canvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    my_canvas.configure(yscrollcommand=yscrollbar.set)
    
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    myframe = Frame(my_canvas)
    my_canvas.create_window((0,0), window=myframe, anchor="nw")


    wrapper1.pack(fill="both", expand="yes", padx=10, pady= 10)
    wrapper1.pack(fill="both", expand="yes", padx=10, pady= 10)


    for thing in range(100):
        tk.Label(myframe, text = f'Button {thing} Yo!').pack()

    

    

    # main_frame = tk.Frame(root)
    # main_frame.pack(fill = BOTH, expand = 1)

    # my_canvas = tk.Canvas(main_frame)
    # my_canvas.pack(side = LEFT,fill= BOTH, expand = 1)

    # my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT,fill=Y)

    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # second_frame = tk.Frame(my_canvas)

    # my_canvas.create_window((0,0), window=second_frame, anchor = "nw")

    # for thing in range(100):
    #     tk.Label(second_frame, text = f'Button {thing} Yo!').grid(row = thing, column=4)



    
def getprogs(conn):
    conn.cursor.execute("SELECT * FROM dbo.[Program]")
    rows = conn.cursor.fetchall()
    for row in rows:
        print(row)

def login(root, user, conn):
    Login.init(root, user, conn)

def home(root, user, conn):
    Home.init(root, user, conn)

def exitFullScreen(root, event=None):
    root.attributes("-fullscreen", False)

def enterFullScreen(root, event=None):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()