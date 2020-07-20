"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""

import functools


def generator(maxN):
    for x in range(1,maxN+1):
        yield x

def factorial(num):
    result = 1
    print("Значения генератора:")
    for el in generator(num):
        print(el)
        result = result * el
    return result

print(f"Результат расчета факториала равен {factorial(10)}")
