import pyodbc

# Functions
def addReminder(n, d):
    reminder = 'INSERT INTO Reminders(isRead, name, details) VALUES(0,\'' + n + '\',\'' + d + '\')'
    print(reminder)
    cursor.execute(reminder)
#def getReminder():

#def markRead(n):

print('begin')
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=WINDELL-T2U0QEF;'
                            'Database=mydb;'
                            'Trusted_Connection=True;')

cursor = connection.cursor()
addReminder('Do the Dishes', 'i mean just figure it out')
connection.commit()
print('we made it')