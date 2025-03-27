#1
def sum_of_squares(nums):
    n = len(nums)
    return sum(nums[i-1]**2 for i in range(1, n+1) if n % i == 0)

nums = [1, 2, 3, 4]
print(sum_of_squares(nums))

#2
def count_active_devices(batteryPercentages):
    count = 0
    n = len(batteryPercentages)

    for i in range(n):
        if batteryPercentages[i] > 0:
            count += 1
            for j in range(i + 1, n):
                batteryPercentages[j] = max(0, batteryPercentages[j] - 1)

    return count

batteryPercentages = [1, 1, 2, 1, 3]
print(count_active_devices(batteryPercentages))

#3
def pairs(A, B):
    max_length = max(len(A), len(B))
    A.extend([0] * (max_length - len(A)))
    B.extend([0] * (max_length - len(B)))
    return list(zip(A, B))

A = [1, 2, 3]
B = ['aa', 'vv']
print(pairs(A, B))

#4
def FindMedian(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid - 1] + arr[mid]) / 2

print(FindMedian([1, 5, 2, 3, 6]))
print(FindMedian([100, 5, 2, 4, 3, 6]))

#5
def PureIntersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

print(PureIntersection([1, 2, 3], [1, 1, 5]))
print(PureIntersection([1, 2, 3], [6, 7, 5]))
print(PureIntersection([1, 2, 3], [1, 2, 15, 3, 3]))

#6
def reverse_linked_list(head):
    return head[::-1]
print(reverse_linked_list([1, 2, 3, 4, 5]))

#7
def is_palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]

print(is_palindrome("abba"))
print(is_palindrome("а роза упала на лапу азора"))
print(is_palindrome("hello"))

#8
def max_charging_ports(n, m_str):
    if n == 0:
        return "Тройников не нашлось"
    m = list(map(int, m_str.split()))
    return sum(m) - (n - 1)

print(max_charging_ports(1, "1"))
print(max_charging_ports(3, "2 5 4"))

#9
def jumping_on_clouds(clouds):
    jumps, i = 0, 0
    while i < len(clouds) - 1:
        i += 2 if i + 2 < len(clouds) and clouds[i + 2] == 0 else 1
        jumps += 1
    return jumps

print(jumping_on_clouds([0, 1, 0, 0, 1, 0]))
print(jumping_on_clouds([0, 1, 0, 0, 0, 1, 0]))
print(jumping_on_clouds([0, 1, 0, 1, 0, 1, 0, 0, 0]))

#10
def CountSpecialProblems(n, k, arr):
    special_count = 0
    page = 1
    for problems in arr:
        for i in range(1, problems + 1):
            if i == page:
                special_count += 1
            if i % k == 0 or i == problems:
                page += 1
    return special_count

print(CountSpecialProblems(2, 3, [4, 2]))

#11
def flat(arr):
    return [elem for tpl in arr for elem in tpl]

print(flat([(1, 2, 'a'), ('bb', ), ('cc', 'dd', 1)]))

#12
def find_middle_node(lst):
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 == 1 else lst[mid]

print(find_middle_node([1, 2, 3, 4, 5]))
print(find_middle_node([1, 2, 3, 4, 5, 6]))

#13
def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

print(gcd(54, 24))

#14
def l_p(my_dict):
    print("Введите логин и пароль")
    attempts = 3
    for attempt in my_dict.values():
        print(attempt)
        login, password = attempt
        if login.isalpha() and password.isdigit():
            print("Успех!")
            return
        else:
            print("Попробуйте еще раз")
            attempts -= 1
            if attempts == 0:
                print("У вас не осталось попыток, приходите завтра")
                return

my_dict = {'try1': ['33', 'Nikita'], 'try2': ['333', 'Nikita^-^'], 'try3': ['Nikita', '33']}
l_p(my_dict)

#15
def max_volume(allmatches):
    if len(allmatches) < 3:
        return 0
    allmatches.sort(reverse=True)
    return allmatches[0] * allmatches[1] * allmatches[2]

print(max_volume([1, 2, 3]))
print(max_volume([7, 1, 17, 25, 50]))

#16
from collections import Counter

def most_frequent_char(s):
    counter = Counter(s)  # Подсчет количества каждого символа
    return counter.most_common(1)[0]  # Берем самый частый символ

print(most_frequent_char("hello world"))  # Вывод: ('l', 3)
print(most_frequent_char("aaa bbb cc"))  # Вывод: ('a', 3)

#17
from itertools import permutations

def perms(arr):
    return list(permutations(arr))  # Генерируем все перестановки

print(perms([1, 2, 3]))
# Вывод: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#18
def combine(A, B, C):
    return list(A) + list(B) + list(C)  # Объединяем три структуры в один список

print(combine([1, 2, 3], (4, 5, 6), {4, 5, 6}))
# Вывод: [1, 2, 3, 4, 5, 6, 4, 5, 6]

#19
def anagram(word1, word2):
    return sorted(word1) == sorted(word2)  # Проверяем, совпадают ли буквы в словах

print(anagram("насос", "сосна"))
print(anagram("Hello", "Helo"))

#20
from collections import Counter

def good_pairs(nums):
    count = Counter(nums)
    return sum(v * (v - 1) // 2 for v in count.values())
print(good_pairs([1, 2, 3, 1, 1, 3]))
print(good_pairs([1, 1, 1, 1]))
print(good_pairs([1, 2, 3]))

#21
def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        if '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num)):
            result.append(num)
    return result
print(self_dividing_numbers(20, 30))

#22
def diff_product_sum(n):
    digits = [int(d) for d in str(n)]
    return eval('*'.join(map(str, digits))) - sum(digits)
print(diff_product_sum(128))

#23
def tuple_creator(arr, n):
    return list(enumerate(arr, start=n))

print(tuple_creator(['aaa', 125, 'bbb'], 3))

#24
def set_comp(st1, st2):
    return not bool(st1 & st2)
print(set_comp({1, 2, 3}, {4, 5, 6}))
print(set_comp({1, 2, 3}, {3, 4, 5}))

#25
from math import prod
def multiplier(arr):
    return prod(arr)
print(multiplier([1, 2, 3, 4, 5]))

#26
def even(arr):
    return [arr[i] for i in range(1, len(arr), 2)]

print(even([1, 2, 3, 4, 4, 4]))

#27
def even_pos(s):
    return s[::2]

print(even_pos("abcdef"))

#28
def min_steps_to_strictly_increasing(nums):
    steps = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            diff = nums[i - 1] - nums[i] + 1
            nums[i] += diff
            steps += diff
    return steps

print(min_steps_to_strictly_increasing([1, 1, 1]))

#29
def remove_adjacent_duplicates(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
print(remove_adjacent_duplicates("abbaca"))