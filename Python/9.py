def f(a):
    if a == a[::-1]:
        return True
    else:
        return False
a = input()
print(f(a))