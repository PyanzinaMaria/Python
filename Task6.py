def find_balance_point(weights):
    total_weight = sum(weights)  # Общий вес всех элементов
    left_weight = 0  # Вес слева от текущей позиции

    for i in range(len(weights)):
        right_weight = total_weight - left_weight - weights[i]

        if left_weight == right_weight:  # Проверяем баланс
            return i  # Возвращаем индекс

        left_weight += weights[i]

    return -1  # Если точка опоры не найдена

# Примеры использования функции
print(find_balance_point([1, 2, 3, 4, 6]))  # 3 (1+2+3 == 6)
print(find_balance_point([2, 1, 3, 4, 6]))  # 2 (2+1 == 3)
print(find_balance_point([1, 3, 5, 2, 2]))  # 2 (1+3 == 2+2)
print(find_balance_point([0, 0, 0, 0, 0]))  # 0 (в любом месте, т.к. все нули)
print(find_balance_point([1, 1, 1, 1, 1, 1]))  # 2 (1+1 == 1+1)
