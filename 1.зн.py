def bits(n):
    binnary = bin(n)[2:]
    result = []
    for i in binnary:
        if i == '1':
            result.append(i)
    return result
"""
В данную функцию поступает целое число 
Данное число переводится в двоичную запись
Идет перебор значений и в список помещаются только еденицы
Для дальнейшего их подсчета
"""

numbers = int(input())
result = bits(numbers).count('1')
print(f"Количество единиц в двоичном представлении {numbers}: {result}")