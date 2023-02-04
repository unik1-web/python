#Дан произвольный список. Представить в обратном порядке
a=[1,-2,3,-4,5]
b=[1,2,3,4,5]
# a.reverse()
# #b=a[::-1]
# print(a)

#Написать функцию, принимающую список и меняющую в нем местами первый и последний элемент
# def change(lst):                          #мой вариант
#     lst0, *lst1, lstN=lst
#     lst=[lstN,*lst1,lst0]
#     return lst
# def change(lst):                          #He мой вариант
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
# print(change(a))

#функция принимает неограниченное количество аргументов и создает из них список
# def to_list(*str): return [*str]
# print(to_list(a,b))

#функция принимает список а возвращает частное от деления мксимального числа на длину списка
# def useless(s):
#     return max(s)/len(s)
# print(useless([19,8.3,-4,11,0,5]))

#сортировка списка по абсолютному значению
# def list_sort(lst):
#     return sorted(lst, key=lambda x: abs(x), reverse=True)
# print(list_sort(a))

#Найти первые три наименьшие значения в списке
# b=sorted(a)[:3]
# print(b)

#имеем список строк разной длины. Функция вернет список строк одинаковой длины, при этом за номинальную длину строк принимается максимальная строка
#остальные строки дополняются справа "_" до нужной длины
# spisok=['крот','белка','выхухоль']
# def all_eq(str):
#     # b=[]
#     L=len(max(str, key=lambda x: len(x)))
#     # for n in str:                                               #1й вариант
#     #     n+='_'*(L-len(n))
#     #     b.append(n)
#     b=[n+'_'*(L-len(n)) for n in str]                           #2й вариант
#     return b
# print(all_eq(spisok))

