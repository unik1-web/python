##########
# Задача 1
###########
# Имеется список целых чисел, необходимо вернуть True,
# если в каком-нибудь списке обнаружится последовательность чисел 1, 2, 3:
# Пример:
# listCheck([1,2,3,1,3]) -> True
# listCheck([1,1,2,4,1]) -> False

nums=[1,2,13,11,2,13,1,2,13,1,2,13,11,2,13,1,2,3]
# def listCheck(nums):                                          #1й вариант
    # for i in range(len(nums)-2):                              #функция при собпадении 3х последовательных чисел с 1,2,3 возвращает True
    #     if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:      #иначе False
    #         return True
    # return False
#     return any([                                              #2й вариант
#         nums[i]==1 and
#         nums[i+1]==2 and
#         nums[i+2]==3
#         for i in range(len(nums)-2)
#     ])
# print(listCheck(nums))

# s=lambda x: [                                                 #3й вариант
#     x[i]==1 and                                               #функция создает список возможных собпадений 3х последовательных чисел с 1,2,3
#     x[i+1]==2 and                                             #при суммировании элементов списка True=1,False=0 получим 1 если есть хоть одно
#     x[i+2]==3                                                 #совпадение и 0 при отсутствии совпадений.
#     for i in range(len(x)-2) ]
# print(bool(sum(s(nums))))                                     #bool() преобразуют 0 или 1 в логику True or False

# def fn(str):                                                  #4й вариант: перебор списка до нужной комбинации 1,2,3
#     while len(str)!=2:
#         str1,str2,str3,*ost=str
#         if str1==1 and str2==2 and str3==3:
#             return True
#         else:
#             str.pop(0)
#     return False
# print(fn(nums))
        
###########
# Задача 2
########### 
# Дана строка, надо вернуть новую строку из другого символа, начиная с первого:
# Пример:
# stringBits('Hello') -> Hlo
# stringBits('Hi') -> H
# stringBits('Heeololeo') -> Hello

# print('Heeololeo'[::2])               #просто срез выводим на экран

###########
# Задача 3
###########
# Имеется две строки, учитывая их верните True,
# если одна из строк появляется в самом конце другой строки.
# Игнорируйте верхний и нижний регистр:
# Пример:
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

# s=['HiAbc', 'abc']
# def stringVh(str):
#     a, b = str[0].lower(), str[1].lower()
#     # return b == a[-len(b)::] or a == b[-len(a)::]                                             #1й вариант: сравниваем срез одной строки с другой строкой
#     return a.endswith(b) or b.endswith(a)                                                     #2й вариант: есть ли в конце одной строки другая?
# print(stringVh(s))

# stringVh = lambda x=s[0].lower(), y=s[1].lower(): x.endswith(y) or y.endswith(x)              #3й вариант: как 2й в-т только короче через лямбду
# print(stringVh())

# from functools import reduce                                                                  #4й вариант: через функцию лямбды reduce - удобно если список большой!
# stringVh = reduce(lambda x=s[0].lower(), y=s[1].lower(): x.endswith(y) or y.endswith(x), s)   #выполняется повторяющаяся операция над парами итерируемых объектов
# print(stringVh)

###########
# Задача 4
########### 
# Дана строка. Надо вернуть строку,
# где будет дублироваться каждый символ в первоначальной строке:
# Пример:
# doubleChar('The') -> 'TThhee'
# doubleChar('AAbb') -> 'AAAAbbbb'
# doubleChar('Hi-There') -> 'HHii--TThheerree'


# s='He-There'
# z=''                                          #1й вариант: собираем строку из удвоенных символов
# for table in [lambda x=x: x*2 for x in s]:
#     z+=table()
# z=''.join(list(map(lambda x: x*2, s)))        #2й вариант: удваиваем каждый символ последовательности и объединяем
# from functools import reduce                  #3й вариант: лямбду иначе используем c reduce
# z=s[0]+reduce(lambda x,y: x+y*2, s)
# z=''.join([n*2 for n in s])                   #4й вариант: почти как 2й но без лямбды
# print(z)

###########
# Задача 5
########### 
# Вернуть количество четных чисел находящихся в данных списках: 
# count_evens([2,1,2,3,4]) -> 3
# count_evens([2,2,0]) -> 3
# count_evens([1,3,5]) -> 0

# l=[0,1,3,4,6]
# def q(a):                                 #1й вариант: перебор списка в цикле
#     s=0
#     for i in a:
#         if i%2 == 0:
#             s+=1
#     return s
# print(q(l))
# q=len([n for n in l if n%2 == 0])         #2й вариант: то же, но короче
# q=len(list(filter(lambda x: x%2==0, l)))  #3й вариант: с лямбдой
# print(q)