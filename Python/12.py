

def bina(a):
    b = bin(a)
    s = b[2:]
    return s

a = int(input())
print(bina(a))