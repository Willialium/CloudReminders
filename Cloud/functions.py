import pyodbc

# Functions
def getNames():
    cursor.execute('SELECT DISTINCT CONVERT(VARCHAR, firstName) FROM names')
    return cursor.fetchall()
def getReminders(name):
    cursor.execute('SELECT name, description FROM reminders A INNER JOIN names B ON A.id=B.reminderID WHERE isRead = 0 AND CONVERT(VARCHAR, B.firstName)= \'' + name + '\'')
    return cursor.fetchall()
def markRead(n):
    cursor.execute('UPDATE Reminders SET isRead = 1 WHERE CONVERT(VARCHAR, name) = \'' + n + '\'')
    connection.commit()
def addReminder(name, title, description):

    cursor.execute("INSERT INTO reminders (name, description) VALUES (\'" + title + "\',\'" + description +"\')")
    cursor.execute("SELECT ID FROM reminders where convert(VARCHAR,name)= \'" + title + "\'")
    id = cursor.fetchone()[0]
    print(id)
    cursor.execute("INSERT INTO names VALUES (\'" + name + "\',\'" + str(id) + "\')")
    connection.commit()


# Connects to Database
connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=10.230.146.53,1433;'
                            'Database=master;'
                            'UID=root;'
                            'PWD=password;')
cursor = connection.cursor()



