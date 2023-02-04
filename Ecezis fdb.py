import fdb
#, fb_library_name='drive:\path\fbclient.dll'
#con = fdb.create_database("create database '127.0.0.1:d:\\x.fdb' user 'sysdba' password 'masterkey'") 
con = fdb.connect(host='127.0.0.1', database="d:\\STATICTRUCKSCALE.fdb", user='sysdba', password='masterkey', charset='UTF8')
ind=(11,12,3,23,13,8,9,10,17)
cur = con.cursor()
cur.execute("select * from WEIGHINGS")

# печатаем шапку таблицы
i=0
for fieldDesc in cur.description:
    i+=1
    if i in ind:
        if i == 11 or i == 12:
            print (fieldDesc[fdb.DESCRIPTION_NAME].ljust(26), end="|")   #fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]
        else:
            print (fieldDesc[fdb.DESCRIPTION_NAME].ljust(15), end="|")
    #if i==10:
    #     break
print("")
print("="*200)
# вывод данных таблицы
fieldIndices = range(len(cur.description))
i=0

for row in cur:
    i+=1
    j=0
    for fieldIndex in fieldIndices:
        j+=1
        fieldValue = str(row[fieldIndex])
        fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]
        if j in ind:
            if j == 8 or j == 9 or j == 10:
                print(str((row[fieldIndex]*10000)//10.00).ljust(15), end="|")
            elif j == 11 or j == 12:
                print(fieldValue.ljust(26), end="|")  #fieldMaxWidth
            else:
                print(fieldValue.ljust(15), end="|")
        #if j==10:
        #     break  
    print("") 
    if i==100:
         break
#print(con.version)
#print(con.ods)
#con.database_info(fdb.isc_info_user_names, 's')
#con = fdb.connect(host='127.0.0.1', database="d:\\x.fdb", user='sysdba', password='masterkey', charset='UTF8')
#con.drop_database()