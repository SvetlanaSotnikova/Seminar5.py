# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

def number_in_degree(number, degree):
    if degree == 0:
        return 1
    if degree > 0:
         return number * number_in_degree(number, degree - 1)
    if degree < 0:
        return 1 / (number * number_in_degree(number, -degree - 1))
    
number = float(input('input number: '))
degree = int(input('input degree: '))
result = number_in_degree(number, degree)
print(f'number {number} in degree {degree} = {result}')


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum_numbers(num1, num2):
    if num1 < 0 or num2 < 0:
        return 'Error, invalid values'
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return sum_numbers(num1 - 1, num2 + 1)

num1 = int(input('input the first number: '))
num2 = int(input('input the second number: '))
result = sum_numbers(num1, num2)

print(f'summa {num1} + {num2} = {result}')
    