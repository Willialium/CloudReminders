import pyodbc

# Functions

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=WINDELL-T2U0QEF;'
                            'Database=mydb;'
                            'Trusted_Connection=True;')

cursor = connection.cursor()
insertFormula = 'INSERT INTO Reminders(name, details) VALUES(%s, %s)'
reminder1 = ('Do the Dishes', 'i mean just figure it out')
cursor.execute(insertFormula, reminder1)
connection.commit()
print('we made it')