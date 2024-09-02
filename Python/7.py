znak = str(input("Znak "))
a = float(input("a = "))
b = float(input("b = "))
if znak == '+':
    res = a + b
elif znak == '-':
    res = a - b
elif znak == '*':
    res = a * b
elif znak == '/':
    res = a / b
else:
     res = "Error"
print(res)