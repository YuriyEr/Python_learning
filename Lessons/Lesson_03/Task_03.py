"""Задание 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

someRange = list(range(20))

def my_func(*num):
    num = sorted(num)
    print(num)
    value = num[-1] + num[-2]
    return value

print(my_func(*someRange))
