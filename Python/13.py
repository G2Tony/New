



a = int(input("Количество чисел в списке: "))
b = int(input("Количество столбцов: "))
d = []
sum = 0
for i in range(a):
    c =[]
    for j in range(b):
        c.append(int(input()))
    d.append(c)
# print(d)
print("Созданная матрица:")
for row in d:
    print(row)
total_sum = 0
for sublist in d:
    for element in sublist:
        total_sum += element

print(f"Сумма всех элементов матрицы: {total_sum}")
