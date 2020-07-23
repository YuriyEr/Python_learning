"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

import os

nameObj = r"Task01 Text.txt"

if os.path.exists("."):
    if os.path.exists(nameObj):
        os.remove(nameObj)
    key = False
    newValue = ""
    try:
        with open(nameObj, "a") as obj:
            while not key:
                newValue = input("Введите новое значение. Если вы хотите закончить ввод нажмите Ввод в пустой строке\n")
                if obj.writable():
                    obj.write(f"{newValue}\n")
                    if newValue == "":
                        break
                else:
                    print("Файл не может быть создан")
                    break
    except:
        print("Что-то пошло не так")
