def func(a):
    if a != 1 and a != 0 and a % 2 != 0:
        return True
    else:
        return False
    
b = int(input())
print(func(b))