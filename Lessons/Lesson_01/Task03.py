# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

import random
import time

num = 0
print("Загадайте число от 0 до 20")
time.sleep(3)
print("Загадали?")
time.sleep(1)
print("Ваше число меньше 20? Да или Нет?")
inputValueFirst = input("Ваше число меньше 20? Да или Нет?")
while inputValueFirst != "Да" | inputValueFirst != "Нет":
    inputValueFirst = input("Я вас не поняла, это число меньше 20? Да или Нет?")

inputValueSecond = input("Ваше число меньше 10? Да или Нет?")
while inputValueSecond != "Да" | inputValueSecond != "Нет":
    inputValueSecond = input("Я вас не поняла, это число меньше 10? Да или Нет?")