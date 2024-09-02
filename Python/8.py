def f(a):
    res = 0
    for i in str(a):
        res += int(i)
    return res


b = input()
print(f(b))