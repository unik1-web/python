from tkinter import *  
def clicked():  
    lbl.configure(text="Запустили!")   
window = Tk()  
window.title("Highload")  
lbl = Label(window, text="Первая программа", font=("Roboto Bold", 20))  
lbl.grid(column=0, row=0)  
btn = Button(window, text="Запустить", command=clicked)  
btn.grid(column=1, row=0)  
window.mainloop()