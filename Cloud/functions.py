import pyodbc

# Functions
def addReminder(n, d):
    cursor.execute('INSERT INTO Reminders(isRead, name, description) VALUES(0,\'' + n + '\',\'' + d + '\')')
    connection.commit()
def getNames():
    cursor.execute('SELECT DISTINCT CONVERT(VARCHAR, firstName) FROM names')
    return cursor.fetchall()
def getReminders(name):
    cursor.execute('SELECT firstName, description FROM reminders A INNER JOIN names B ON A.id=B.reminderID WHERE CONVERT(VARCHAR, B.firstName)= \'' + name + '\'')
    return cursor.fetchall()
def markRead(n):
    cursor.execute('UPDATE Reminders SET isRead = 0 WHERE CONVERT(VARCHAR, name) = \'' + n + '\'')
    connection.commit()

# Connects to Database
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=10.230.146.53,1433;'
                            'Database=master;'
                            'Trusted_Connection=True;')
cursor = connection.cursor()



