"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""

import random

someList = [random.randint(0,100) for x in range(50)]

def interseptList(list):
    newList = []
    mySet = set(someList)
    for x in list:
        if mySet.issuperset([x]) and newList.count(x) == 0:
            newList.append(x)
    return newList

print(f"Исходный генерируемый набор\n{someList}")
print(f"Уникальный не упорядоченный результат \n{interseptList(someList)}")