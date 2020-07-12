# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

finish = False
someList = []

while not finish:
    value = input("Введите любое значение, если вы закончили ввод - наберите Да\n")
    if value != "Да":
        someList.append(value)
    else:
        finish = not finish
        print(f"Вы ввели значения \n{someList}")

generateList = []
for value in range(0,(len(someList))):
    if (value%2) == 0 and value != (len(someList)-1):
        generateList.append(someList[value+1])
    elif (value%2) != 0:
        generateList.append(someList[value-1])
    elif value == (len(someList)-1) and value%2 == 0:
        generateList.append(someList[value])

print(f"Результат задания \n{generateList}")