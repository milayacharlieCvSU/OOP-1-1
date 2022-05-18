import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\christian\Desktop\College Stufffs\Col1stY2ndS\CPEN 60\Project Code Draft\Demo Codes\Database1.accdb')

    user_id = 3
    Address = 'Cavite'

    database = connection.cursor()
    database.execute('UPDATE Table1 set Address=? where id=?', (Address, user_id))
    connection.commit()
    print('Database is updated.')
except pyodbc.Error:
    print('Database is NOT connected.')
