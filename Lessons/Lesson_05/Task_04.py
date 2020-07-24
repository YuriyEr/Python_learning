"""
4. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import os
import random

nameObj = r"Task04-01 Text.txt"

if os.path.exists(nameObj):
    os.remove(nameObj)
try:
    with open(nameObj, "w+") as obj:
        data = [random.randint(0,20) for x in range(100, 150)]
        result: str = ""
        for value in data:
            result = result + " " + str(value)
        obj.write(result)
        print(f"Результат генерации: \n{result}\n")
except:
    print("Ошибка в блоке генерации и записи")

try:
    with open(nameObj) as obj:
        metaData = obj.read().split()
        metaData = list((map(lambda x: int(x), metaData)))
        print(f"Сумма всех сгенерированных чисел из файла:\n{sum(metaData)}")
except:
    print("Ошибка в блоке десериализации и подсчета")