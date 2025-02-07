from itertools import combinations

def generate_transformed_numbers(n: int, mink: int, maxk: int) -> list:
    result = []
    digits = [int(d) for d in str(n)]

    # Перебираем длины подмножеств цифр
    for k in range(mink, maxk + 1):
        # Перебираем все подмножества длины k
        for i in range(len(digits) - k + 1):
            # Получаем текущее подмножество цифр как число
            digit_slice = digits[i:i + k]
            digit_num = int(''.join(map(str, digit_slice)))

            # Проверяем четность и выполняем операции
            if digit_num % 2 == 0:  # Четное
                half_digit = digit_num // 2
                # Создаем новое число
                new_digits = digits[:i] + [int(d) for d in str(half_digit)] + digits[i + k:]
                new_num = int(''.join(map(str, new_digits)))
                result.append(new_num)

            # Умножаем на 2 для всех случаев
            double_digit = digit_num * 2
            new_digits = digits[:i] + [int(d) for d in str(double_digit)] + digits[i + k:]
            new_num = int(''.join(map(str, new_digits)))
            result.append(new_num)

    # Возвращаем отсортированный список уникальных значений
    return sorted(set(result))

# Примеры вызовов для проверки работы функции
print("n=10, mink=2, maxk=5", generate_transformed_numbers(10, 2, 5))  # Ожидается: [5, 20]
print("n=9, mink=1, maxk=4", generate_transformed_numbers(9, 1, 4))  # Ожидается: [18]
print("n=47, mink=1, maxk=1", generate_transformed_numbers(47, 1, 1))  # Ожидается: [27, 87, 414]
print("n=100, mink=84, maxk=99", generate_transformed_numbers(100, 84, 99))  # Ожидается: []
