def poisc(x,y):
    z=x.split()
    if z.count(y)>0:
        return "Word found"
    else:
        return "Word not found"
    
word=input()
slovo=input()
print(poisc(word,slovo))