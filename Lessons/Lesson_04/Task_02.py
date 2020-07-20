"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

import random

# part 1 generate list
randomList = [int(x) for x in list((range(0, 300, 23)))]
random.shuffle(randomList)
print(randomList)

# part 2 use expression task
def my_func(list):
    oldValue = list[0]
    newListF = []
    for x in list:
        if x > oldValue:
            newListF.append(x)
    return newListF

newList = my_func(randomList)
print(newList)