import random
print("*" * 10, "Угадай число", "*" * 10) 
print("Компьютер выберет случайным образом число от 1 до 10. Попробуй угадать это число. Для выхода введите 0")
answer = 1 
score = 0
i = 0 
while answer: 
    rand = random.randint(1, 10) 
    answer = int(input("Bвeдитe число: ")) 
    if answer == 0: break
    if answer == rand: 
        score = score +1 
        print("Правильно! Ваш счет: ", score, " из ", i) 
    else: 
        print("Попробуйте еще раз!") 
    i = i + 1 
print("Общий счет ", score, " из ", i)    
print("Дo встречи!")
