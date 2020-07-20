"""
Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys
scriptName, laborHours, hourCost, bonus = sys.argv
try:
    result = (int(laborHours) * int(hourCost)) + int(bonus)
    print(result)
except:
    print("Invalid input paramerts")
    exit()


# Для проверки результата выполните команду ниже в консоли
# python Task_01.py 10 2 100
