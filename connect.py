import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; '
                                r'DBQ=C:\Users\christian\Desktop\College Stufffs\Col1stY2ndS\CPEN 60\Project Code Draft\Demo Codes\Database1.accdb;')
    print("Database is Connected.")

except pyodbc.Error:
    print("Database is NOT connected.")
