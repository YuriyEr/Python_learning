"""
7.
A Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

B Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

C Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

import os
import statistics
import json

nameObjOne = r"Task07-01 Text.txt"

# A
if os.path.exists(nameObjOne):
    os.remove(nameObjOne)
try:
    with open(nameObjOne, "a") as obj:
        data = ["firm_1 ООО 10000 5000", "firm_2 ОАО 9000 11000", "firm_3 ЗАО 12000 9000"]
        for value in data:
            obj.write(f"{value}\n")
except:
    print("Ошибка в блоке записи в файл")

# B
with open(nameObjOne) as obj:
        data = []
        profit = []
        averageProfit = int()
        for value in obj.readlines():
            lineData = []
            for val in value.split():
                lineData.append(val)
            data.append(lineData)

            print(f"прибыль для компании {lineData[0]} = {(int(lineData[2]) - int(lineData[3]))}")

            if (int(lineData[2]) - int(lineData[3])) > 0:
                profit.append((int(lineData[2]) - int(lineData[3])))

            averageProfit = statistics.mean(profit)
        print(f"средняя выручка для компаний с положительной рентабельностью: {averageProfit}")

# C
        if os.path.exists("nameObjJSON.json"):
            os.remove("nameObjJSON.json")

        dataJSON = [data, {"Средняя прибыль": averageProfit}]
        # serialization
        with open("nameObjJSON.json", "w") as obj:
            json.dump(dataJSON, obj)
        # check deserialization
        with open("nameObjJSON.json") as obj:
            dataFromJSON = None
            dataFromJSON = json.load(obj)
            print(f"Десериализация из файла прошла успешно\n{dataFromJSON}")