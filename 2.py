#Функции
#1
import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    try:
        a = float(input("Введите длину первого катета: "))
        b = float(input("Введите длину второго катета: "))
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"Длина гипотенузы: {hypotenuse:.2f}")
    except ValueError:
        print("Ошибка! Введите числовые значения.")

#2
def taxi_fare(distance_km):
    BASE_FARE = 4.00
    COST_PER_140M = 0.25
    cost = BASE_FARE + (distance_km * 1000 / 140) * COST_PER_140M
    return round(cost, 2)

if __name__ == "__main__":
    try:
        distance = float(input("Введите расстояние поездки в км: "))
        fare = taxi_fare(distance)
        print(f"Стоимость поездки: ${fare}")
    except ValueError:
        print("Ошибка! Введите числовые значения.")

#3
def calculate_shipping(num_items):
    if num_items >= 1:
        # Первая позиция стоит $10,95, каждая последующая $2,95
        shipping_cost = 10.95 + (num_items - 1) * 2.95
        return shipping_cost
    else:
        return 0

if __name__ == "__main__":
    try:
        num_items = int(input("Введите количество товаров в заказе: "))
        if num_items < 1:
            print("Ошибка: количество товаров должно быть больше 0.")
        else:
            shipping = calculate_shipping(num_items)
            print(f"Сумма доставки для {num_items} товаров составляет: ${shipping:.2f}")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

#4
def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == "__main__":
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        num3 = float(input("Введите третье число: "))
        median = median_of_three(num1, num2, num3)
        print(f"Медиана: {median}")
    except ValueError:
        print("Ошибка! Введите числовые значения.")

#5
def number_to_ordinal(num):
    ordinals = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    return ordinals[num] if 1 <= num <= 12 else ""

if __name__ == "__main__":
    for i in range(1, 13):
        print(f"{i} -> {number_to_ordinal(i)}")

#6
def ordinal_date(day, month, year):
    import datetime
    return (datetime.date(year, month, day) - datetime.date(year, 1, 1)).days + 1

if __name__ == "__main__":
    try:
        day = int(input("Введите день: "))
        month = int(input("Введите месяц: "))
        year = int(input("Введите год: "))
        ordinal = ordinal_date(day, month, year)
        print(f"Порядковый номер дня в году: {ordinal}")
    except ValueError:
        print("Ошибка! Введите корректные числовые значения.")

#7
def center_string(s, w):
    if len(s) >= w:
        return s
    else:
        spaces = (w - len(s)) // 2
        return ' ' * spaces + s

if __name__ == "__main__":
    strings = [
        "Hello, World!",
        "Python",
        "OpenAI",
        "Centered Text"
    ]

    widths = [20, 30, 10, 40]

    for s in strings:
        for w in widths:
            print(f"Window width {w}: '{center_string(s, w)}'")

#8
def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    elif operator == "^":
        return 3
    else:
        return -1

if __name__ == "__main__":
    operator = input("Введите оператор (+, -, *, /, ^): ")

    priority = precedence(operator)

    if priority == -1:
        print("Ошибка: введен неверный оператор.")
    else:
        print(f"Приоритет оператора '{operator}': {priority}")

#9
def is_prime(n):
    # если число меньше или равно 1, оно не простое
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # делится на i, то не простое
    return True  # не делится, значит простое

if __name__ == "__main__":
    try:
        num = int(input("Введите целое число: "))
        if is_prime(num):
            print(f"{num} — простое число.")
        else:
            print(f"{num} — не простое число.")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

#10
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # делится на i, то не простое
    return True  # не делится, значит простое

def nextPrime(n):
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate
if __name__ == "__main__":
    try:
        num = int(input("Введите целое число: "))
        next_prime = nextPrime(num)
        print(f"Первое простое число больше {num}: {next_prime}")
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число.")

#11
import re
def is_strong_password(password):
    if len(password) >= 8 and \
       re.search(r'[a-z]', password) and \
       re.search(r'[A-Z]', password) and \
       re.search(r'[0-9]', password):
        return True
    else:
        return False

if __name__ == "__main__":
    password = input("Введите ваш пароль: ")

    if is_strong_password(password):
        print("Пароль надежный.")
    else:
        print(
            "Пароль ненадежный. Он должен быть как минимум 8 символов, содержать хотя бы одну строчную и одну заглавную букву, а также одну цифру.")

#Списки
#1
def main():
    numbers = []

    while True:
        try:
            num = int(input("Введите целое число (для окончания введите 0): "))

            if num == 0:
                break
            else:
                numbers.append(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    numbers.sort()

    print("\nЧисла в порядке возрастания:")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()

#2
def main():
    numbers = []

    while True:
        try:
            num = int(input("Введите целое число (для окончания введите 0): "))

            if num == 0:
                break
            else:
                numbers.append(num)
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    numbers.sort(reverse=True)

    print("\nЧисла в порядке убывания:")
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()

#3
def main():
    words = []

    while True:
        word = input("Введите слово (или оставьте строку пустой для завершения): ")

        if word == "":
            break
        if word not in words:
            words.append(word)

    print("\nСлова без повторений:")
    for word in words:
        print(word)

if __name__ == "__main__":
    main()

#4
def main():
    numbers = []

    while True:
        try:
            num = input("Введите число (или оставьте строку пустой для завершения): ")

            if num == "":
                break
            else:
                numbers.append(int(num))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    if len(numbers) == 0:
        print("Не было введено ни одного числа.")
        return

    average = sum(numbers) / len(numbers)
    print(f"\nСреднее значение: {average}")

    below_average = [num for num in numbers if num < average]
    equal_to_average = [num for num in numbers if num == average]
    above_average = [num for num in numbers if num > average]

    if below_average:
        print("\nЧисла ниже среднего:")
        for num in below_average:
            print(num)

    if equal_to_average:
        print("\nЧисла, равные среднему:")
        for num in equal_to_average:
            print(num)

    if above_average:
        print("\nЧисла выше среднего:")
        for num in above_average:
            print(num)

if __name__ == "__main__":
    main()

#5
import random

def generate_lottery_ticket():
    ticket = random.sample(range(1, 50), 6)

    ticket.sort()

    print("Ваши номера для лотерейного билета:")
    for num in ticket:
        print(num)

if __name__ == "__main__":
    generate_lottery_ticket()

#6
def countRange(lst, min_val, max_val):
    count = sum(1 for x in lst if min_val <= x < max_val)
    return count


def main():
    list1 = [1, 3, 5, 7, 9, 11, 13, 15]
    list2 = [1.5, 2.3, 3.7, 4.0, 5.8, 6.1, 7.9]
    list3 = [10, 20, 30, 40, 50, 60]

    # целые числа
    print("Пример 1:")
    print(countRange(list1, 5, 15))  # Ожидаем 5 (5, 7, 9, 11, 13)

    # числа с плавающей запятой
    print("Пример 2:")
    print(countRange(list2, 2.0, 6.0))  # Ожидаем 4 (2.3, 3.7, 4.0, 5.8)

    # числа с плавающей запятой
    print("Пример 3:")
    print(countRange(list2, 3.0, 7.0))  # Ожидаем 4 (3.7, 4.0, 5.8, 6.1)

    # целые числа
    print("Пример 4:")
    print(countRange(list3, 20, 50))  # Ожидаем 3 (20, 30, 40)

if __name__ == "__main__":
    main()

#7
import re

def tokenize(expression):
    token_pattern = r'\d+|[+\-*/ˆ()]'
    tokens = re.findall(token_pattern, expression)

    return tokens

def main():
    expression = input("Введите математическое выражение: ")
    tokens = tokenize(expression)
    print("Лексемы выражения:")
    print(tokens)

if __name__ == "__main__":
    main()

#8
def isSublist(larger, smaller):
    if not smaller:
        return True

    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i + len(smaller)] == smaller:
            return True
    return False


def main():
    larger = [1, 2, 3, 4, 5]
    smaller = [2, 3]
    print(f"Является ли {smaller} подсписком {larger}? {isSublist(larger, smaller)}")  # True

    smaller = [3, 5]
    print(f"Является ли {smaller} подсписком {larger}? {isSublist(larger, smaller)}")  # False

    smaller = []
    print(f"Является ли {smaller} подсписком {larger}? {isSublist(larger, smaller)}")  # True

    larger = [1, 2, 3, 4]
    smaller = [1, 2, 3, 4]
    print(f"Является ли {smaller} подсписком {larger}? {isSublist(larger, smaller)}")  # True

if __name__ == "__main__":
    main()

#9
def is_sorted(lst):
    if len(lst) <= 1:
        return True

    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        return True

    if all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        return True

    return False


def main():
    user_input = input("Введите числа через пробел: ")

    try:
        lst = list(map(int, user_input.split()))
    except ValueError:
        print("Ошибка: введены нечисловые значения.")
        return

    if is_sorted(lst):
        print("Список отсортирован.")
    else:
        print("Список не отсортирован.")

if __name__ == "__main__":
    main()

#10
def get_all_sublists(lst):
    sublists = []
    for start in range(len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            sublists.append(lst[start:end])
    sublists.append([])
    return sublists


def main():
    lists = [
        [1, 2, 3],
        ['a', 'b', 'c', 'd'],
        [5],
        []
    ]

    for lst in lists:
        print(f"Все подсписки списка {lst}: {get_all_sublists(lst)}\n")

if __name__ == "__main__":
    main()

#Словари
#1
def reverseLookup(dictionary, value):
    keys = []

    for key, val in dictionary.items():
        if val == value:
            keys.append(key)

    return keys


def main():
    my_dict = {
        'a': 123,
        'b': 78,
        'c': 93,
        'd': 21,
        'e': 13,
    }

    search_value = int(input("Введите значение для поиска: "))

    result = reverseLookup(my_dict, search_value)

    if result:
        print(f"Ключи, соответствующие значению {search_value}: {result}")
    else:
        print(f"Ключи для значения {search_value} не найдены.")

if __name__ == "__main__":
    main()

#2
import random
def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def theoretical_probability(sum_):
    probabilities = {
        2: 1 / 36,
        3: 2 / 36,
        4: 3 / 36,
        5: 4 / 36,
        6: 5 / 36,
        7: 6 / 36,
        8: 5 / 36,
        9: 4 / 36,
        10: 3 / 36,
        11: 2 / 36,
        12: 1 / 36
    }
    return probabilities.get(sum_, 0)

def main():
    frequencies = {i: 0 for i in range(2, 13)}

    total_rolls = 1000
    for _ in range(total_rolls):
        result = roll_dice()
        frequencies[result] += 1

    print("Исход    Процент симуляции    Ожидаемый процент")
    for sum_ in range(2, 13):
        simulation_percentage = (frequencies[sum_] / total_rolls) * 100
        expected_percentage = theoretical_probability(sum_) * 100
        print(f"{sum_:<8}{simulation_percentage:>18.2f}{expected_percentage:>20.2f}")

if __name__ == "__main__":
    main()

#3

#4

#5
def number_to_words(num):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred",
                "six hundred", "seven hundred", "eight hundred", "nine hundred"]

    if num == 0:
        return "zero"

    hundred = num // 100
    ten = (num % 100) // 10
    one = num % 10

    result = []

    if hundred:
        result.append(hundreds[hundred])

    if 10 <= num % 100 < 20:
        result.append(ones[num % 100])
    else:
        if ten:
            result.append(tens[ten])

        if one:
            result.append(ones[one])

    return " ".join(result)


def main():
    num = int(input("Введите число от 0 до 999: "))

    if 0 <= num <= 999:
        print(f"Сумма прописью: {number_to_words(num)}")
    else:
        print("Число должно быть в пределах от 0 до 999.")

if __name__ == "__main__":
    main()

#6
def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

def main():
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    if are_anagrams(word1, word2):
        print("Слова являются анаграммами.")
    else:
        print("Слова не являются анаграммами.")

if __name__ == "__main__":
    main()

#7
def clean_string(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())
    return s


def are_anagrams(str1, str2):
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)

    return sorted(cleaned_str1) == sorted(cleaned_str2)


def main():
    str1 = input("Введите первую фразу: ")
    str2 = input("Введите вторую фразу: ")

    if are_anagrams(str1, str2):
        print("Строки являются анаграммами.")
    else:
        print("Строки не являются анаграммами.")

if __name__ == "__main__":
    main()
