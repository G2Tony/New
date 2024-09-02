# a = input().split()
# a.sort()

def f(a):
    b = []
    for i in a:
        
        # if i in a:
        #     a.remove(a[i])
        # else:
        #     b.append()
        if i not in b:
            b.append(i)
    return b

a = []
n = int(input("Kol-vo el: "))
for i in range(0,n):
    el = input()
    a.append(el)
print(f(a))