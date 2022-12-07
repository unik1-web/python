import fdb
#, fb_library_name='drive:\path\fbclient.dll'
con = fdb.create_database("create database '127.0.0.1:d:\\x.fdb' user 'sysdba' password 'masterkey'") 
con = fdb.connect(host='127.0.0.1', database="d:\\x.fdb", user='sysdba', password='masterkey', charset='UTF8')
cur = con.cursor()
cur.execute("recreate table COUNTRY (ID_COUNTRY int, CNT_NAME varchar(50))")
con.commit()
cur.execute("create unique index COUNTRY_ID on COUNTRY(ID_COUNTRY)")
con.commit()
cur = con.cursor()
cur.execute("insert into COUNTRY (ID_COUNTRY,CNT_NAME) values (?,?)",(1,"Afghanistan"))
con.commit()
cur = con.cursor()
data = [
    (2,'Albania'),
    (3,'Algeria'),
    (4,'Andorra')
]
cur.executemany("insert into COUNTRY (ID_COUNTRY,CNT_NAME) values (?,?)",data)
con.commit()
cur = con.cursor()
cur.execute("select ID_COUNTRY,CNT_NAME from COUNTRY")

for row in cur.itermap():
    print(str(row['ID_COUNTRY']).ljust(5),row['CNT_NAME'])