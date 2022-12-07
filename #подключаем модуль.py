#подключаем модуль
import kinterbasdb
ibhostname='127.0.0.1'
ibdatabasename="d:\\x.fdb"
ibusername='sysdba'
ibpassword='masterkey'
#Подключаемся к базе
myconnection = kinterbasdb.connect(ibhostname,ibdatabasename, ibusername, ibpassword)
 
 #Cоздаем курсор
mycursor = myconnection.cursor()

# выполяем sql-запрос
mycursor.execute('select  tt.field1, tt.field2, tt.filed3 from mytable tt')
 
# парсим полученный результат в список кортежей
result = mycursor.fetchall()
 
# бежим по записям и выполняем любые действия
for  (myfield1, myfield2, myfield3) in result:
        #выводим на экран значения полей
        print field1+'|'+ field2 + '|' + field3

# после выполнения всех нужных нам действий закрываем соединение с базой
myconnection.close