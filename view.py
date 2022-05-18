import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\christian\Desktop\College Stufffs\Col1stY2ndS\CPEN 60\Project Code Draft\Demo Codes\Database1.accdb')

    database = connection.cursor()
    database.execute('select * from Table1')
    for x in database.fetchall():
        print(x)
    print('Database is viewed.')
except pyodbc.Error:
    print('Database is NOT connected.')
