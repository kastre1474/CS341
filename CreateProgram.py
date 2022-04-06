import tkinter as tk
from tkinter import *
from tkinter.font import Font
from tkinter import ttk
from tkcalendar import Calendar
import User
import Conn
import Home
import Login
import Conn
import Programs
import sqlite3

def init(root, user, conn):
    clearWin(root)
    setup(root, user)
    buttonOptions(root, user, conn)
    createEntry(root, user, conn)

def setup(root, user):
    root.attributes("-fullscreen", True)
    root.bind("<Escape>", lambda event: exitFullScreen(event, root))
    root.bind("<F1>", lambda event: enterFullScreen(event, root))
    root.title("YMCA")
    for i in range(50):
        root.columnconfigure(i, weight=1, uniform = '')
    for i in range(50):
        root.rowconfigure(i, weight=1, uniform = '')
    root.configure(background = '#E6E6E6')
    header = tk.Label(root, bg='#4682B4', text = "Create A New Program", font=Font(family = "Helvetica", size = 30, weight = "bold"))
    header.grid(row = 0, column = 0, rowspan = 5, columnspan = 50, sticky = tk.W+tk.E+tk.S+tk.N)
    lsidebar = tk.Label(root, bg='#4682B4')
    lsidebar.grid(row = 5, column = 0, rowspan = 45, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    rsidebar = tk.Label(root, bg='#4682B4')
    rsidebar.grid(row = 5, column = 45, rowspan = 45, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.userid != None):
        userlabel = tk.Label(root, bg='#4682B4', text = "Logged in as: {}".format(user.fname), font=Font(family = "Helvetica", size = 10, weight = "bold"))
        userlabel.grid(row = 0, column = 0)
    
def buttonOptions(root, user, conn):
    color = '#999999'
    b1 = tk.Button(root, text = 'Home', command = lambda: home(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b2 = tk.Button(root, text = 'Programs', command = lambda: programs(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b3 = tk.Button(root, text = 'About', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    logintext = 'Login/SignUp' if user.userid == None else 'Log Out'
    b4 = tk.Button(root, text = logintext, command = lambda:login(root, user, conn), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)
    b1.grid(row = 5, column = 0, rowspan = 2, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    b2.grid(row = 7, column = 0, rowspan = 2, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    b3.grid(row = 9, column = 0, rowspan = 2, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    b4.grid(row = 11, column = 0, rowspan = 2, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)
    if(user.type == 'S'):
        b5 = tk.Button(root, text = 'Create Program', command = None, font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = color)  
        b5.grid(row = 13, column = 0, rowspan = 2, columnspan = 5, sticky = tk.W+tk.E+tk.S+tk.N)

def createEntry(root, user, conn):
    progName = tk.Label(root, text = "Program Name:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    progName.grid(row=5,column=9,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    progName = tk.Entry(root, font = Font(family = "Helvetica", size = 20, weight = "bold"), background='white')
    progName.grid(row=5,column=12,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    progDesc = tk.Label(root, text = "Description:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    progDesc.grid(row=5,column=15,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    progDesc = tk.Entry(root, font = Font(family = "Helvetica", size = 20, weight = "bold"), background='white')
    progDesc.grid(row=5,column=18,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    locs = ["Onalaska Pool","Onalaska Gym","Onalaska Field","LaCrosse Pool","LaCrosse Gym","LaCrosse Field",]
    loc = tk.StringVar(root)
    progLoc = tk.Label(root, text = "Location:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    progLoc.grid(row=7,column=9,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    progLoc = tk.OptionMenu(root, loc, *locs)
    progLoc.grid(row=7,column=12,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    progFee = tk.Label(root, text = "Member Fee:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    progFee.grid(row=7,column=15,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    progFee = tk.Entry(root, font = Font(family = "Helvetica", size = 20, weight = "bold"), background='white')
    progFee.grid(row=7,column=18,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    hours = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    mins = ["00", "15", "30", "45"]
    ampm = ["am", "pm"]

    STime = tk.Label(root, text = "Start Time:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    STime.grid(row=9,column=9,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    sHour = tk.StringVar(root)
    sHour.set("12")
    sMin = tk.StringVar(root)
    sMin.set("00")
    sAMPM = tk.StringVar(root)
    sAMPM.set("am")
    SHour = tk.OptionMenu(root, sHour, *hours).grid(row=9,column=12,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    SMin = tk.OptionMenu(root, sMin, *mins).grid(row=9,column=13,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    SAMPM = tk.OptionMenu(root, sAMPM, *ampm).grid(row=9,column=14,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)

    ETime = tk.Label(root, text = "End Time:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    ETime.grid(row=9,column=15,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    eHour = tk.StringVar(root)
    eHour.set("12")
    eMin = tk.StringVar(root)
    eMin.set("00")
    eAMPM = tk.StringVar(root)
    eAMPM.set("am")
    EHour = tk.OptionMenu(root, eHour, *hours).grid(row=9,column=18,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    EMin = tk.OptionMenu(root, eMin, *mins).grid(row=9,column=19,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    EAMPM = tk.OptionMenu(root, eAMPM, *ampm).grid(row=9,column=20,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)

    SDate = tk.Label(root, text = "Start Date:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    SDate.grid(row=11,column=9,rowspan = 4,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    cal1 = Calendar(root, selectmode = 'day', year = 2022)
    cal1.grid(row=11,column=12,rowspan=4,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    EDate = tk.Label(root, text = "End Date:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    EDate.grid(row=11,column=15,rowspan = 4,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    cal2 = Calendar(root, selectmode = 'day', year = 2022)
    cal2.grid(row=11,column=18,rowspan=4,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    progDays = tk.Label(root, text = "Day(s) of the Week:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    progDays.grid(row=15,column=9,rowspan = 2,columnspan = 3,sticky=tk.W+tk.E+tk.S+tk.N)
    dayVar = [tk.IntVar() in range(7)]
    tk.Checkbutton(root,text = "Sunday", variable=dayVar[0]).grid(row=15,column=12,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Monday", variable=dayVar[1]).grid(row=15,column=13,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Tuesday", variable=dayVar[2]).grid(row=15,column=14,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Wednesday", variable=dayVar[3]).grid(row=15,column=15,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Thursday", variable=dayVar[4]).grid(row=15,column=16,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Friday", variable=dayVar[5]).grid(row=15,column=17,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Checkbutton(root,text = "Saturday", variable=dayVar[6]).grid(row=15,column=18,rowspan=2,sticky=tk.W+tk.E+tk.S+tk.N)
    tk.Label(root, text = "", background = 'white').grid(row=15,column=19, rowspan=2,columnspan=2,sticky=tk.W+tk.E+tk.S+tk.N)

    numSpots = tk.Label(root, text = "Number of Spots:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    numSpots.grid(row=17,column=9,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
    numSpots = tk.Entry(root, font = Font(family = "Helvetica", size = 20, weight = "bold"), background='white')
    numSpots.grid(row=17,column=12,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    prereq = tk.Label(root, text = "Prerequisite:", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    prereq.grid(row=17,column=15,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)
    selectedPrereq = tk.StringVar(root)
    selectedPrereq.set("None")
    conn.cursor.execute('SELECT NAME FROM Program GROUP BY NAME')
    courses = [row[0] for row in conn.cursor.fetchall()]
    preReqs = tk.OptionMenu(root, selectedPrereq, *courses).grid(row=17,column=18,rowspan=2,columnspan=3,sticky=tk.W+tk.E+tk.S+tk.N)

    creationMessage = tk.Label(root, text = "", font = Font(family = "Helvetica", size = 20, weight = "bold"), background = 'white')
    creationMessage.grid(row = 21, column = 9,rowspan=2, columnspan = 12, sticky=tk.W+tk.E+tk.S+tk.N)

    submit = tk.Button(root, text = 'Submit', command = lambda: verify(root,user,conn,progName.get(),progDesc.get(),loc.get(),progFee.get(),sHour.get(),sMin.get(),sAMPM.get(),eHour.get(),eMin.get(),eAMPM.get(),cal1.get_date(),cal2.get_date(),dayVar,numSpots.get(),selectedPrereq.get(),creationMessage), font = Font(family = "Helvetica", size = 20, weight = "bold"), bg = '#999999')
    submit.grid(row = 19, column = 9,rowspan=2, columnspan = 12, sticky=tk.W+tk.E+tk.S+tk.N)

def verify(root, user, conn, progName, progDesc, progLoc, progFee, sHour, sMin, sAMPM, eHour, eMin, eAMPM, sDate, eDate, days, numSpots, prereq, message):
    message.config(text="")
    if(progName==""):
        message.config(text="Program Name cannot be blank.")
        return
    if(progLoc==""):
        message.config(text="Please select a location.")
        return
    if(progFee==""):
        message.config(text="Please enter a member fee.")
        return
    try:
        progFee = int(progFee)
    except:
        message.config(text="Member fee must be of type integer.")
        return
    if(progFee<0):
        message.config(text="Member fee must be greater than 0.")
        return
    
    sHour = int(sHour)
    sMin = int(sMin)
    eHour = int(eHour)
    eMin = int(eMin)

    if(sAMPM=="am" and sHour==12):
        sHour = sHour - 12
    if(eAMPM=="am" and eHour==12):
        eHour = eHour - 12
    if(sAMPM=="pm" and sHour!=12):
        sHour = sHour + 12
    if(eAMPM=="pm" and eHour!=12):
        eHour = eHour + 12
    if(sHour<6 or sHour>20):
        message.config(text="Start time must be between 6:00am and 8:45pm.")
        return
    if((eHour<6 or (eHour==6 and eMin==0)) or eHour>21 or (eHour==21 and eMin!=0)):
        message.config(text="End time must be between 6:15am and 9:00pm.")
        return
    if(sHour > eHour):
        message.config(text="Start time must be before end time.")
        return
    if(sHour==eHour):
        if(sMin >= eMin):
            message.config(text="Start time must be before end time.")
            return
    if(eHour-sHour>3 or (eHour-sHour==3 and eMin!=sMin)):
        message.config(text="Programs cannot be over 3 hours long.")
        return

    sYear = int(sDate[6:10])
    sMonth = int(sDate[3:5])
    sDay = int(sDate[0:2])
    eYear = int(eDate[6:10])
    eMonth = int(eDate[3:5])
    eDay = int(eDate[0:2])

    if(eYear<sYear):
        message.config(text="Start date must be before end date.")
        return
    if(eYear==sYear):
        if(eMonth<sMonth):
            message.config(text="Start date must be before end date.")
            return
        if(eMonth==sMonth):
            if(eDay<=sDay):
                message.config(text="Start date must be before end date.")
                return

    if(numSpots==""):
        message.config(text="Please enter the number of spots available for registration.")
        return
    try:
        numSpots = int(numSpots)
    except:
        message.config(text="Number of spots must be of type integer.")
        return
    if(numSpots<4 or numSpots>50):
        message.config(text="Number of spots must be between 5 and 50.")
        return
    
    
    
    
def addNewProg(root, user, conn, cal1, cal2):
    entryBoxes = root.winfo_children()
    entries = []
    for entry in entryBoxes:
        if(entry.winfo_class() == 'Entry'):
            entries.append(entry.get())
            entry.delete(0, 'end')
    query1 = "INSERT INTO Program (NAME,DESCRIPTION,LOCATION,FEE,STARTTIME,ENDTIME,STARTDATE,ENDDATE,DAY,SIZE,PREQ,USERID)"
    query2 = "VALUES ('{}','{}','{}',{},'{}','{}','{}','{}','{}',{},'{}',{})"
    query2 = query2.format(entries[0],entries[1],entries[2], int(entries[3]),entries[4],entries[5], entries[6],entries[7],entries[8],int(entries[9]),entries[10],user.userid)
    try:
        conn.cursor.execute(query1 + ' ' + query2)           
        conn.conn.commit()
    except sqlite3.Error as e:
        print("Failure")

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