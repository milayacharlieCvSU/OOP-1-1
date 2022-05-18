import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                                r'DBQ=C:\Users\christian\Desktop\College Stufffs\Col1stY2ndS\CPEN 60\Project Code Draft\Demo Codes\Database1.accdb;')

    database = connection.cursor()
    database.execute("INSERT into Table1 (Fullname, Age, Course, Address, Grade)"
                     "values ('Charlie Milaya', 18, 'BSCpE', 'Cavite', 94)")
    connection.commit()
    print("Record is updated.")
except pyodbc.Error:
    print("Database is NOT connected.")
