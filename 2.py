def summ_kub(n):
    summ = 0
    for i in range(1,n+1):
        summ += i**3
    return summ
"""
Функция для суммирования кубов в диапозоне числе от 1 до n
Условия: все числа положительные
"""
a = summ_kub(2)
print(a)