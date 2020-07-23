"""
3. Создать текстовый файл (не программно),
А
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32

Б
Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

С
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

nameObjOne = r"Task03-01 Text.txt"
nameObjTwo = r"Task03-02 Text.txt"
nameObjThree = r"Task03-03 Text.txt"

# А
if os.path.exists("."):
    if os.path.exists(nameObjOne):
        os.remove(nameObjOne)

    dataOne = {"Иванов": 10000, "Сидоров": 19020, "Петрова": 43443, "Леонидова": 34343,
            "Лампочкин": 54544, "Кувалдина": 54545, "Молотков": 32322, "Сочников": 65545,
            "Сочникова": 56343, "Захаров": 54544}

    with open(nameObjOne, "w+") as obj:
        for key, value in dataOne.items():
            obj.write(f"{key} {value}\n")

    print("Сотрудники с ЗП менее 20000")
    for key, value in dataOne.items():
        if value < 20000:
            print(f"{key} - {value}")

# B
if os.path.exists("."):
    if os.path.exists(nameObjTwo):
        os.remove(nameObjTwo)

    dataTwo = {"one": 1, "two": 2, "three": 3, "four": 4}

    with open(nameObjTwo, "w+") as obj:
        for key, value in dataTwo.items():
            obj.write(f"{key} - {value}\n")
# C

if os.path.exists("."):
    if os.path.exists(nameObjTwo):

        dataThree = dict()

        with open(nameObjTwo) as obj:
            dataFour = obj.readlines()
            for value in dataFour:
                if value.split()[0] == "one":
                    dataThree["один"] = value.split()[2]
                elif value.split()[0] == "two":
                    dataThree["два"] = value.split()[2]
                elif value.split()[0] == "three":
                    dataThree["три"] = value.split()[2]
                elif value.split()[0] == "four":
                    dataThree["четыре"] = value.split()[2]
        with open(nameObjThree, "w") as obj:
            for key, value in dataThree.items():
                obj.writelines(f"{key} - {value}\n")
    else:
        print("0")