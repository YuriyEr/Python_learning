"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

import os

nameObj = r"Task02 Text.txt"

# Создать текстовый файл (не программно), сохранить в нем несколько строк
if os.path.exists("."):
    if os.path.exists(nameObj):
        os.remove(nameObj)
    try:
        data = ["Пойду на речку купаться\n",
                "Венок из цветов соберу\n",
                "Как хочется мне улыбаться\n",
                "Лето я очень люблю.\n"]

        with open(nameObj, "w+") as obj:
            obj.writelines(data)
        #     выполнить подсчет количества строк, количества слов в каждой строке.
        if os.path.exists(nameObj):
            newData = open(nameObj)
            array = newData.readlines()
            print(f"колличество строк в объекте: {len(array)}")
            for line in array:
                data = line.split()
                print(f"для строки: {line} {len(data)} слов")
            newData.close()

    except:
        print("Что-то пошло не так")


