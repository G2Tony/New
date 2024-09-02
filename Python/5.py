def feb(g):
    if g == 0:
        return 0
    elif g == 1:
        return 1
    else:
        return feb(g-1) + feb(g-2) 

b = int(input())
for i in range(0,b):
    print(feb(i), end =" ")