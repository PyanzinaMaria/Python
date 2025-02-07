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
