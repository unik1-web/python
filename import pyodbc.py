#import pyodbc
#msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
#print(f'MS-Access Drivers : {msa_drivers}')
import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\adml\Documents\Database1.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
    cursor = conn.cursor() # создается курсор для соединения
    cursor.execute('select * from tab1') # Курсор генерируется с применением критерия  поиск или запрос
    for string in cursor.fetchall():
        print(string)
    myuser = ( 
        (6, 'data', 'data@gmail.com'),
        (7, 'python', 'python@gnail.com'),
        (8, 'java', 'java@gmail.com'), 
    ) 
    cursor.executemany('INSERT INTO users VALUES (?,?,?)', myuser)
    conn.commit()
    print('Data Inserted')
except pyodbc.Error as e:
    print("Error in Connection", e)