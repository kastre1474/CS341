import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import User
import Conn
import Home
import Login
import Conn
import CreateProgram
import MoreInfo

def init(root, user, conn):
    clearWin(root)
    setup(root, user)
    buttonOptions(root, user, conn)
    buildTable(root, user, conn)

def setup(root, user):
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.title("YMCA")
    for i in range(11):
        root.columnconfigure(i, weight=1, uniform = '')
    for i in range(8):
        root.rowconfigure(i, weight=1, uniform = '')
    root.configure(background = '#E6E6E6')
    header = tk.Label(root, bg='#4682B4', text = "Programs", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    header.grid(row = 0, column = 0, columnspan = 11, sticky = tk.W+tk.E+tk.S+tk.N)
    lsidebar = tk.Label(root, bg='#4682B4')
    lsidebar.grid(row = 1, column = 0, rowspan = 7, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N)
    rsidebar = tk.Label(root, bg='#4682B4')
    rsidebar.grid(row = 1, column = 9, rowspan = 7, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.userid != None):
        userlabel = tk.Label(root, bg='#4682B4', text = "Logged in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
        userlabel.grid(row = 0, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)

def buttonOptions(root, user, conn):
    color = '#999999'
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b2 = tk.Button(root, text = 'Programs', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    logintext = 'Login/SignUp' if user.userid == None else 'Log Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b1.grid(row = 1, column = 0, rowspan = 1, sticky = tk.W+tk.E+tk.S+tk.N)
    b2.grid(row = 2, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    b3.grid(row = 3, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    b4.grid(row = 4, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.type == 'S'):
        b5 = tk.Button(root, text = 'Create Program', command = lambda:createProgram(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)  
        b5.grid(row = 5, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    
def buildTable(root, user, conn):
    tree = ttk.Treeview(root)
    tree['columns'] = ('Program Name', 'Program Description', 'Program Location', 'Program ID')
    tree.column("#0", width = 0, stretch = NO)
    tree.column('Program ID', width = 0, stretch = NO)
    tree.heading('Program Name', text = 'Program Name')
    tree.heading('Program Description', text = 'Program Description')
    tree.heading('Program Location', text = 'Program Location')
    conn.cursor.execute('SELECT * FROM Program')
    rows = conn.cursor.fetchall()
    for row in rows:
        tree.insert(parent='',index='end',values=(row[1], row[2], row[3], row[0]))
    tree.grid(row = 1, column=1, rowspan = 5, columnspan = 8, sticky = tk.W+tk.E+tk.S+tk.N)
    tree.bind("<Double-1>", lambda event: indProg(event,root, tree, user, conn))

def indProg(e,root, tree, user, conn):
    row = tree.selection()[0] 
    MoreInfo.init(root, user, conn, tree.item(row,"values")[3])
    
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
