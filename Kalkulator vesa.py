from tkinter import *
from tkinter import messagebox

def calculate_bmi():            #Объявляем функцию.
    kgs = weight_tf.get() #С помощью метода .get получаем из поля ввода с именем weight_tf значение веса, которое ввёл пользователь и конвертируем в целое число с помощью int().
    ms = height_tf.get() #С помощью метода .get получаем из поля ввода с именем height_tf значение роста и конвертируем в целое число с помощью int(). Обязательно делим его на 100, так как пользователь вводит рост в сантиметрах, а в формуле для расчёта ИМТ используются метры.
    if not kgs.isdigit()  or not ms.isdigit(): return
    kg=int(kgs)
    m=int(ms)/100
    bmi = kg/(m*m)              #Рассчитываем значение индекса массы тела.
    bmi = round(bmi, 1)         #Округляем результат до одного знака после запятой.
    
        
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
    else:
        messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')  

window = Tk()               #Создаём окно приложения.
window.title("Калькулятор индекса массы тела (ИМТ)") #Добавляем название приложения.
window.geometry('400x200')  #Размер окна



frame = Frame(
    window,                 #Обязательный параметр, который указывает окно для размещения Frame.
    padx = 10,              #Задаём отступ по горизонтали.
    pady = 10               #Задаём отступ по вертикали.
)
frame.pack(expand=True)     # Не забываем позиционировать виджет в окне. Здесь используется метод pack. 
                            # С помощью свойства expand=True указываем, что Frame заполняет весь контейнер, 
                            # созданный для него.

height_lb = Label(
    frame,
    text="Введите свой рост (в см)  "
)
height_lb.grid(row=2, column=1)

weight_lb = Label(
    frame,
    text="Введите свой вес (в кг)  ",
)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=2, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

cal_btn = Button(
    frame,                      #Заготовка с настроенными отступами.
    text='Рассчитать ИМТ',      #Надпись на кнопке.
    command=calculate_bmi       #Позволяет запустить событие с функцией при нажатии на кнопку
)
cal_btn.grid(row=5, column=2)   # Размещаем кнопку в ячейке, расположенной ниже, чем наши надписи, 
                                # но во втором столбце, то есть под ячейками для ввода информации.


window.mainloop()