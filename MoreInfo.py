import tkinter as tk
from tkinter.font import Font
import User
import Conn
import Login
import Programs
import CreateProgram
import Home
import Register

def init(root, user, conn, progid):
    clearWin(root)
    setup(root, user, conn, progid)
    buttonOptions(root, user, conn)
   
def setup(root, user, conn, progid):
    info = getprogs(conn, progid)
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.title("YMCA")
    for i in range(11):
        root.columnconfigure(i, weight=1, uniform = '')
    for i in range(8):
        root.rowconfigure(i, weight=1, uniform = '')
    root.configure(background = '#E6E6E6')
    header = tk.Label(root, bg='#4682B4', text = info[1], font=Font(family = "Helvetica", size = 30, weight = "bold"))
    header.grid(row = 0, column = 0, columnspan = 11, sticky = tk.W+tk.E+tk.S+tk.N)
    lsidebar = tk.Label(root, bg='#4682B4')
    lsidebar.grid(row = 1, column = 0, rowspan = 7, columnspan = 1, sticky = tk.W+tk.E+tk.S+tk.N)
    rsidebar = tk.Label(root, bg='#4682B4')
    rsidebar.grid(row = 1, column = 9, rowspan = 7, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.userid != None):
        userlabel = tk.Label(root, bg='#4682B4', text = "Logged in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
        userlabel.grid(row = 0, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    information(root, user, conn, info, progid)

def information(root, user, conn, info, progid):    
    tk.Label(root, bg='white', text = "Description: {}".format(info[2]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 1, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, bg='white', text = "Location: {}".format(info[3]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 2, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, bg='white', text = "Day of Week: {}      Time: {} - {}".format(info[9], info[5], info[6]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 3, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, bg='white', text = "Start Date: {}      End Date: {}".format(info[7], info[8]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 4, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, bg='white', text = "Class Size: {}".format(info[10]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 1, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, bg='white', text = "Prerequisite: {}".format(info[11]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 2, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    if user.type == "M" or user.type == "S": tk.Label(root,  bg='white', text = " Member Fee: {}".format(info[4]) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 3, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    else: tk.Label(root,  bg='white', text = "Non Member Fee: {}".format(info[4]*2) , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 3, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    if(enrollStat(user, conn, progid) == False):
        b6 = tk.Button(root, text = 'Register', bg='#999999', command = lambda: Register.register(root,user,conn,progid), font = Font(family = "Helvetica", size = 20, weight = "bold")).grid(row = 4, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    else:
        b6 = tk.Button(root, text = 'Unenroll', bg='#999999', command = lambda: None, font = Font(family = "Helvetica", size = 20, weight = "bold")).grid(row = 4, column = 4, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
        tk.Label(root, bg='white', text = "You are enrolled!" , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 5, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
     
def buttonOptions(root, user, conn):
    color = '#999999'
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    logintext = 'Login/SignUp' if user.userid == None else 'Log Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b1.grid(row = 1, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    b2.grid(row = 2, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    b3.grid(row = 3, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    b4.grid(row = 4, column = 0, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.type == 'S'):
        b5 = tk.Button(root, text = 'Create Program', command = lambda:createProgram(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)  
        b5.grid(row = 5, column = 0, rowspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
        
def enrollStat(user, conn, progid):
    rows = None
    if user.userid != None:
        conn.cursor.execute("SELECT * FROM History WHERE PROGRAMID = {}".format(progid))
        rows = conn.cursor.fetchall()
    if rows == None or rows == []:
        return False
    return True

def getprogs(conn, progid):
    conn.cursor.execute("SELECT * FROM Program WHERE PROGRAMID = {}".format(progid))
    rows = conn.cursor.fetchall()
    return rows[0]

def home(root, user, conn):
    Home.init(root, user, conn)

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

        