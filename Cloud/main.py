import pyodbc

# Functions
def addReminder(n, d):
    cursor.execute('INSERT INTO Reminders(isRead, name, details) VALUES(0,\'' + n + '\',\'' + d + '\')')
def getReminders():
    cursor.execute('SELECT name, details FROM Reminders WHERE isRead = 0')
    return cursor.fetchall()
def markRead(n):
    cursor.execute('UPDATE Reminders SET isRead = 1 WHERE name = \'' + n + '\'')

# Connects to Database
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=WINDELL-T2U0QEF;'
                            'Database=mydb;'
                            'Trusted_Connection=True;')

cursor = connection.cursor()
