import tkinter as tk
from tkinter.font import Font
import MoreInfo
import Login

def register(root, user, conn, progid):
    if checkAv(user, conn, progid): 
        tk.Label(root, bg='white', text = "Class is Full. Sorry!" , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 5, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    elif user.userid == None: Login.init(root,user,conn)
    elif checkPre(user, conn, progid):
        tk.Label(root, bg='white', text = "You do not meet the class prerequisite. Sorry!" , font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 5, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    elif (checkCal(user, conn, progid)):
        tk.Label(root, bg='white', text = "You have a schedule conflict. Sorry!", font=Font(family = "Helvetica", size = 15, weight = "bold"), anchor = "w", relief="ridge").grid(row = 5, column = 2, rowspan = 1, columnspan = 2, sticky = tk.W+tk.E+tk.S+tk.N)
    else:
        rows = None
        conn.cursor.execute("SELECT NAME FROM Program WHERE PROGRAMID = '{}'".format(progid))
        rows = conn.cursor.fetchall()[0][0]
        conn.cursor.execute("INSERT INTO History (PROGRAMID,USERID,NAME,STATUS)" + " " + "VALUES ('{}','{}','{}','{}')".format(progid,user.userid,rows,"e"))
        conn.conn.commit()
        MoreInfo.init(root, user, conn, progid)
              
def checkAv(user, conn, progid):
    rows = None
    conn.cursor.execute("SELECT SIZE, ENROLLED FROM Program WHERE PROGRAMID = '{}'".format(progid))
    rows = conn.cursor.fetchall()[0]
    if rows[0] <= rows[1]: return True
    return False

def checkPre(user, conn, progid):
    rows = None
    conn.cursor.execute("SELECT PREQ FROM Program WHERE PROGRAMID = '{}'".format(progid))
    rows = conn.cursor.fetchall()[0][0]
    if rows == "None": return False
    conn.cursor.execute("SELECT* FROM History WHERE USERID = '{}' AND STATUS = '{}' AND NAME = '{}'".format(user.userid,"p",rows))
    rows = conn.cursor.fetchall()
    if rows == [] or rows == None:
        return True
    return False

def checkCal(conn, progid):
    rows = None
    rows2 = None
    rows3 = None
    
    conn.cursor.execute("SELECT STARTTIME, ENDTIME, DAY FROM Program WHERE PROGRAMID = '{}'".format(progid))
    rows = conn.cursor.fetchall()[0]
    
    conn.cursor.execute("SELECT PROGRAMID FROM History WHERE STATUS = '{}' AND USERID = '{}'".format("e", "1"))
    rows2 = conn.cursor.fetchall()
    if rows2 == []: return False
    rows2 = rows2[0]
    days = rows[2]
    time1 = int(rows[0].replace(":", ""))
    time2 = int(rows[1].replace(":", ""))
    
    for i in rows2:
        conn.cursor.execute("SELECT STARTTIME, ENDTIME, DAY, NAME FROM Program WHERE PROGRAMID = '{}'".format(i))
        rows3 = conn.cursor.fetchall()[0]  
        days2 = rows3[2]
        for i in range(7):
            if days[i] == '1' and days[i] == days2[i]:
                time3 = int(rows3[0].replace(":", ""))
                time4 = int(rows3[1].replace(":", ""))
                if time1 <= time3 or time3 <= time2:
                    return True
                elif time1 <= time4 or time4 <= time2:
                    return True
                elif time3 <= time1 or time1 <= time4:
                    return True
                elif time3 <= time2 or time2 <= time4:
                    return True     
    return False