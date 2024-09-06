import random
a = '1234567890'
b = 'qwertyuiopasdfghjklzxcvbnm'
s = b.upper()
n = int(input("Количество символов в пароле: "))
psw = ''
# Словарь
su = a + b + s
ls = list(su)
for i in range(n):
    psw += random.choice(su)
print(psw)