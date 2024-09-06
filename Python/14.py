def f(d):
    rez = 1 
    for i in d:
        rez = rez * i 
    return rez




a = []
b = int(input('Кол-во чисел: '))
for i in range(b):
    c = int(input())
    a.append(c)
print(f(a))