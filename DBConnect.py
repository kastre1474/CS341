import pyodbc 
 #changing code
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ymca.database.windows.net;'
                      'Database=ymca;'
                      'Trusted_Connection=yes;PWD=AdminUser2022!;UID=ymca;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.[User]')

for i in cursor:
    print(i)
