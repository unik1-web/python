def poisc(x,y):
    if y in x:
        return "Word found"
    else:
        return "Word not found"
    
word=input("Vvedite stroku: ")
slovo=input()
print(poisc(word,slovo))