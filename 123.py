def findNb(m):
    n = 1
    while True:
        # Вычисляем сумму кубов от n до 1
        sum_cubes = sum(i ** 3 for i in range(n, 0, -1))

        # Если сумма кубов равна m, возвращаем n
        if sum_cubes == m:
            return n

        # Если сумма меньше m, увеличиваем n и продолжаем поиск
        elif sum_cubes < m:
            n += 1
        # Если сумма больше m, уменьшаем n и продолжаем поиск
        else:
            break

    # Если не найдено подходящее значение n, возвращаем -1
    return -1


print(findNb(1071225))