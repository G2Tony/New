a = [] 
b = []
d = int(input("Количетсво в первом спискеЁ элеметов: "))
c = int(input("Количетсво в втором спискеЁ элеметов: "))
for i in range(d):
    el = int(input())
    a.append(el)
for j in range(c):
    el2=int(input())
    b.append(el2)

g = set(a)
print(g,a)
print(a in b)