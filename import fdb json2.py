import fdb
con = fdb.connect(host='127.0.0.1', database="d:\\22.fdb", user='sysdba', password='masterkey', charset='UTF8')
cur = con.cursor()

cur.execute("select id from JSON2")

for row in cur.itermap():
    print(str(row['id']))

#con = fdb.connect(host='127.0.0.1', database="d:\\x.fdb", user='sysdba', password='masterkey', charset='UTF8')
#con.drop_database()