import pyodbc 

class conn():
    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};Server=ymca.database.windows.net;Database=ymca;Trusted_Connection=no;PWD=AdminUser2022!;UID=ymca;')
        self.cursor = self.conn.cursor()
        

