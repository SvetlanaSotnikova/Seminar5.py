# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0 , a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
# def fibonaci(num):
#     if num == 1:
#         return 1
#     elif num <= 0:
#         return 0
#     return fibonaci(num - 1) + fibonaci(num - 2)

# num = int(input("input number: "))
# result = fibonaci(num)

# print(f'result Fibonaci = {result}')


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def find_max(list):
#     new_list = []
#     max_value = max(list)
#     min_value = min(list)

#     for i in range(len(list)):
#         if list[i] == max_value:
#             new_list.append(min_value)
#         else:
#             new_list.append(list[i])
        

#     return new_list

# size = int(input('input size of array: '))
# list = []
# for i in range(size):
#     while True:
#         number = int(input(f'inpunt number {i + 1}: '))
#         if number > 0:
#             break
#         else:
#             print('Error, negativ value :/')
#     list.append(number)
    
# result = find_max(list)
# print(f'result = {result}')

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# without recursy
# def is_prime(number):
#     if number <= 1:
#         return 'no :('
#     if number == 2:
#         return 'yes :D'
#     for i in range(2, number):
#         if number % i == 0:
#             return 'no :('
        
#     return 'yes :D'

# number = int(input('input number: '))
# result = is_prime(number)
# print(result)

# with recursy
# def is_prime(number, div = 2):
#     if number <= 1:
#         return 'no :('
#     if number == 2:
#         return 'yes :D'
#     if div * div > number:
#         return 'yes :D'
#     if number % div == 0:
#         return 'no :('
        
#     return is_prime(number, div + 1)

# number = int(input('input number: '))
# result = is_prime(number)
# print(result)

# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reverse_sequence():
#     num = int(input('input number: '))
#     if num == 0:
#         return
#     reverse_sequence()
#     print(num, end=' ')

# reverse_sequence()
