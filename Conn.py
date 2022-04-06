import sqlite3 

class conn():
    def __init__(self):
        self.conn = sqlite3.connect(r'C:\SQLiteStudio\YMCA.db')
        self.cursor = self.conn.cursor()
        

