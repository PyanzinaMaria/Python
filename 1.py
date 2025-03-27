#1
def iosif(n: int, k: int) -> list:
    # Создаем список участников от 1 до n
    people = list(range(1, n + 1))
    result = []
    index = 0

    # Пока список не пуст
    while people:
        # Находим индекс следующего выбывающего участника
        index = (index + k - 1) % len(people)
        # Удаляем участника и добавляем его в результат
        result.append(people.pop(index))

    return result

print("n=6, k=2", iosif(6, 2))
print("n=5, k=2", iosif(5, 2))
print("n=8, k=8", iosif(8, 8))
print("n=3, k=9", iosif(3, 9))
print("n=4, k=3", iosif(4, 3))

#2
def count_paths(x: int, y: int, tabu: list) -> int:
    tabu_set = set(tabu)

    # таблица для хранения количества путей
    paths = [[0] * (y + 1) for _ in range(x + 1)]

    # Начальная точка (0, 0) всегда имеет один путь
    if (0, 0) not in tabu_set:
        paths[0][0] = 1

    # первый столбец
    for i in range(1, x + 1):
        if (i, 0) not in tabu_set:
            paths[i][0] = paths[i - 1][0]

    # первая строка
    for j in range(1, y + 1):
        if (0, j) not in tabu_set:
            paths[0][j] = paths[0][j - 1]

    # оставшаяся таблица
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if (i, j) not in tabu_set:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    return paths[x][y]

print("x=3, y=2, tabu=[]", count_paths(3, 2, []))
print("x=1, y=6, tabu=[(7,1), (4,4)]", count_paths(1, 6, [(7, 1), (4, 4)]))
print("x=8, y=8, tabu=[(9,10), (1,4)]", count_paths(8, 8, [(9, 10), (1, 4)]))
print("x=7, y=5, tabu=[(6,8)]", count_paths(7, 5, [(6, 8)]))

#3
def generate_transformed_numbers(n: int, mink: int, maxk: int) -> list:
    result = []
    digits = [int(d) for d in str(n)]

    for k in range(mink, maxk + 1):
        for i in range(len(digits) - k + 1):
            digit_slice = digits[i:i + k]
            digit_num = int(''.join(map(str, digit_slice)))

            if digit_num % 2 == 0:  # Четное
                half_digit = digit_num // 2
                # Создаем новое число
                new_digits = digits[:i] + [int(d) for d in str(half_digit)] + digits[i + k:]
                new_num = int(''.join(map(str, new_digits)))
                result.append(new_num)

            double_digit = digit_num * 2
            new_digits = digits[:i] + [int(d) for d in str(double_digit)] + digits[i + k:]
            new_num = int(''.join(map(str, new_digits)))
            result.append(new_num)

    return sorted(set(result))

print("n=10, mink=2, maxk=5", generate_transformed_numbers(10, 2, 5))  # [5, 20]
print("n=9, mink=1, maxk=4", generate_transformed_numbers(9, 1, 4))  # [18]
print("n=47, mink=1, maxk=1", generate_transformed_numbers(47, 1, 1))  #  [27, 87, 414]
print("n=100, mink=84, maxk=99", generate_transformed_numbers(100, 84, 99))  #  []

#5
def s_polygonal(s, i):
    return (i * ((s - 2) * i - (s - 4))) // 2

def find_nearest_polygonal(s, n):
    closest_number = None
    min_diff = float('inf')

    i = 1
    while True:
        pn = s_polygonal(s, i)

        if pn > n + min_diff:
            break

        diff = abs(pn - n)
        if diff < min_diff or (diff == min_diff and pn < closest_number):
            closest_number = pn
            min_diff = diff

        i += 1

    return closest_number

print(find_nearest_polygonal(8, 7))  # Ожидаемый результат: 8
print(find_nearest_polygonal(19, 1))  # Ожидаемый результат: 1
print(find_nearest_polygonal(18, 15))  # Ожидаемый результат: 15
print(find_nearest_polygonal(36, 87))  # Ожидаемый результат: 105

#6
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