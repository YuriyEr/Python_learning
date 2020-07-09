# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

valueA: float = input("Введите значение А >> ")
valueB: float = input("Введите значение B >> ")

try:
    valueA = float(valueA)
    valueB = float(valueB)
    finish = False
    if valueA <= 0:
        valueA = 0.1  # если введен 0 - цикл будет бесконечным
        print("Так как вы ввели начальное значение А <= 0 за точку А отсчета принято {}".format(valueA))
    if valueB <= 0 or valueB < valueA:
        valueB = valueA  # если введен 0 - цикл будет бесконечным
        print("Вы ввели значени В <= 0 или < значиения А = {}".format(valueB))
        finish = not finish
    currentValue = valueA
    day = 1

    print("Результат:")
    print("{}-й день: {} км".format(day, currentValue))
    while not finish:
        currentValue = round((currentValue * 1.1), 2)
        day += 1
        print("{}-й день: {} км".format(day, currentValue))
        if currentValue >= valueB:
            finish = True
        if day > 100:
            print("Достигнут лимит операций 100")
            finish = not finish
except:
    print("Вы ввели не корерректные данные")
