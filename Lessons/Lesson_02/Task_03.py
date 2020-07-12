# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

import random
import time

enum = list(range(1,13))
name = ("Зима", "Весна", "Лето", "Осень")
someDict = {}
for value in enum:
    if  value == 12 or 1 <= value <= 2:
        someDict[value] = name[0]
    if 3 <= value <= 5:
        someDict[value] = name[1]
    if 6 <= value <= 8:
        someDict[value] = name[2]
    if 9 <= value <= 11:
        someDict[value] = name[3]

# input print emulate
for value in range(1,13):
    randomInput = random.randint(1, 12)
    print(f"Вы ввели значение {randomInput} и это соответствует периоду {someDict.get(value)}")
    time.sleep(0.5)

