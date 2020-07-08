# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

import random
import time

num = 0
print("Загадайте число от 0 до 20!")
time.sleep(1)
print("Загадали?")
time.sleep(1)
inputValueFirst = input("Ваше число меньше 10? Да или Нет? >> ").lower()
while inputValueFirst != "да" and inputValueFirst != "нет" :
    inputValueFirst = input("Я вас не поняла, это число меньше 10? Да или Нет? >> ")

if inputValueFirst == "да":
    inputValueSecond = input("Ваше число {}? Да? >> ".format(num)).lower()
    while inputValueSecond != "да":
        num += 1
        inputValueSecond = input("Ваше число {}? Да? >> ".format(num))
        if num > 20:
            print("Вы загадали число не из диапазона. Досвидание.")
            break
    if inputValueSecond == "да":
        print("Произведение ваших цифр {0} + {0}{0} + {0}{0}{0} = {1}".format(num, (
            num + int("{0}{0}".format(num)) + int("{0}{0}{0}".format(num)))
        ) )
        print("Отлично")

else:
    num = 10
    inputValueSecond = input("Ваше число {}? Да? >> ".format(num)).lower()
    while inputValueSecond != "да":
        num += 1
        inputValueSecond = input("Ваше число {}? Да? >> ".format(num))
        if num > 20:
            print("Вы загадали число не из диапазона. Досвидание.")
            break

    if inputValueSecond == "да":
        print("Произведение ваших цифр {0} + {0}{0} + {0}{0}{0} = {1}".format(num, (
            num + int("{0}{0}".format(num)) + int("{0}{0}{0}".format(num)))
        ) )
        print("Отлично")