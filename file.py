# f=open('data.txt', 'w')
# try:
# 	f.write('#Name Email Phone\n')
# 	f.write('Rostya kostya@mail.ru 111-1111\n')
# 	f.write('Admin admin@test.ru 212-2323\n')
# 	f.write('Support support@test.ru 333-3333\n')
# finally:
# 	f.close()
# with open('data.txt', 'w') as f:
# 	f.write('#Name Email Phone\n')
# 	f.write('Rostya kostya@mail.ru 111-1111\n')
# 	f.write('Admin admin@test.ru 212-2323\n')
# 	f.write('Support support@test.ru 333-3333\n')
# data=['#Name Email Phone\n','Kostya kostya@mail.ru 111-1111\n','Admin admin@test.ru 212-2323\n','Support support@test.ru 333-3333\n']
# f=open('data.txt', 'w')
# try:
# 	f.writelines(data)
# finally:
# 	f.close()
# f=open('data.txt')
# f.seek(48)
# print(f.read())
# print(f.readlines())
# f=open('data.txt')                          #Это предпочтителльный способ чтения 
# for line in open('data.txt'):				  #файлов	
f=open('data.txt')							  # Извлечение						
buf=f.readlines()							  # данных из data.txt
f.close()									  # Сортировка 
buf.sort()									  # данных по имени
foot=open('data1.txt','w')					  # и передача
for line in buf:							  # данных
	foot.write(line)						  # в другой файл data1.txt
	print(line, end='')  					  # с выводом данных data1.txt
	pass
foot.close()