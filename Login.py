import tkinter as tk
from tkinter.font import Font
import User
import Conn
import Home
import Programs
import CreateProgram

def init(root, user, conn):
    clearWin(root)
    setup(root, user)
    buttonOptions(root, user, conn)
    if(user.userid != None):
        setuplogout(root, user, conn)
    else:
        setuplogin(root, user, conn)

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
    if(user.userid == None):
        header = tk.Label(root, bg='#4682B4', text = "Please Login or Create an Account", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    else:
        header = tk.Label(root, bg='#4682B4', text = "Log Out", font=Font(family = "Helvetica", size = 30, weight = "bold")) 
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
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
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

def setuplogin(root, user, conn):
    l1 = tk.Label(root, text = "Email Address:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l2 = tk.Label(root, text = "Password:", bg = "White", font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te1 = tk.Entry(root, font = Font(family = "Helvetica", size = 20, weight = "bold"))
    te2 = tk.Entry(root,  font = Font(family = "Helvetica", size = 20, weight = "bold"))
    incorrectlabel = tk.Label(root, text = "", bg = '#E6E6E6', font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b4 = tk.Button(root, text = 'Login', command = lambda: login(root, user, conn, te1, te2, incorrectlabel), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l1.grid(row = 1, column = 3, sticky = tk.W+tk.E+tk.S+tk.N)
    l2.grid(row = 2, column = 3, sticky = tk.W+tk.E+tk.S+tk.N)
    te1.grid(row = 1, column = 4, columnspan = 3, sticky = tk.W+tk.E+tk.S+tk.N)
    te2.grid(row = 2, column = 4, columnspan = 3, sticky = tk.W+tk.E+tk.S+tk.N)
    b4.grid(row = 3, column = 3, columnspan = 4, sticky = tk.W+tk.E+tk.S+tk.N)
    incorrectlabel.grid(row = 4, column = 3, columnspan = 4, sticky = tk.W+tk.E+tk.S+tk.N)
    root.bind("<Return>", lambda event: login(root, user, conn, te1, te2, incorrectlabel, event))

def setuplogout(root, user, conn):
    l1 = tk.Label(root, text = "Are You Sure You Want To Log Out?", bg = '#E6E6E6', font = Font(family = "Helvetica", size = 20, weight = "bold"))
    l1.grid(row = 2, column = 4, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    b6 = tk.Button(root, text = 'Log Out', command = lambda: logout(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"))
    b6.grid(row = 3, column = 4, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)

def login(root, user, conn, email, pword, inclabel, e=None):
    conn.cursor.execute("SELECT * FROM User WHERE EMAIL='{}' AND PASSWORD='{}'".format(email.get(), pword.get()))
    if(conn.cursor.rowcount == 0):
        inclabel.config(text="Email or Password Incorrect")
        email.delete(0, 'end')
        pword.delete(0, 'end')
    else:
        userinfo = conn.cursor.fetchone()
        user.signin(userinfo[0], userinfo[1],userinfo[2],userinfo[3],userinfo[4],userinfo[5],userinfo[6])
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

def createProgram(root, user, conn):
    CreateProgram.init(root, user, conn)

def exitFullScreen(e, root):
    root.attributes("-fullscreen", False)

def enterFullScreen(e, root):
    root.attributes("-fullscreen", True)

def clearWin(root):
    for widgets in root.winfo_children():
        widgets.destroy()