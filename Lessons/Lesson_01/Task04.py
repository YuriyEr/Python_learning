# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

value: int = 0
maxValue: int = 0
logical = False

while value>1:
    valueCurrent = int(round((value%10),0))
    if valueCurrent > maxValue:
        maxValue = valueCurrent
    value = value / 10
if maxValue > 1:
    print("Максимальное десятичное число в вашей цифре равно {}".format(maxValue))
else: print("Максимальное десятичное число в вашей цифре равно {}".format(value))
