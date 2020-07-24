"""
5.
A Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
B
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os
import re
import numpy

nameObj = r"Task05-01 Text.txt"
# A
if os.path.exists(nameObj):
    os.remove(nameObj)
try:
    with open(nameObj, "a") as obj:
        data = [["Информатика", {"лекций": 100, "пар": 50, "лабораторных": 20 }],
                ["Физика", {"лекций": 30, "лабораторных": 10 }],
                ["Физкультура", {"пар": 30}],
                ["Выживание", {"лекций": 80, "лабораторных": 30}],
                ]
        for val in data:
            stringValue = ""
            stringValue = f"{val[0]}: "
            for key, value in val[1].items():
                stringValue += f"{value}"
                stringValue += f"({key}) "
            stringValue += "\n"
            obj.write(stringValue)
except:
    print("Ошибка в блоке генерации и записи в файл")

# B
with open(nameObj) as obj:
    unpackData = dict()
    for val in obj.readlines():
        key = val.split()[0].replace(":", "")
        values = []
        for vals in val.split():
            buffer = (re.findall('\d+', vals))
            if buffer != []:
                values.append(int(buffer[0]))
        unpackData[key] = sum(values)
    print(f"результат задания распаковки\n{unpackData}")


