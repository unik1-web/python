y=50
def func1():
    global y
    y=100
    print(y)
    
print(y)
func1()
print(y)