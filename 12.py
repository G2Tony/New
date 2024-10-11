def comp(a, b):
    # Создаем словарь для хранения частот элементов из a
    freq_a = {}
    for num in a:
        if num not in freq_a:
            freq_a[num] = 1
        else:
            freq_a[num] += 1

    # Проверяем каждый элемент b
    for num_b in b:
        root = int(num_b ** 0.5)

        # Если корня нет в a или его счетчик равен 0, возвращаем False
        if root not in freq_a or freq_a[root] <= 0:
            return False

        # Уменьшаем счетчик корня на 1
        freq_a[root] -= 1

    # Если мы дошли сюда, значит все проверки пройдены успешно
    return True

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 1441, 20736, 361, 25921, 361, 20736, 361]
print(comp(a,b))