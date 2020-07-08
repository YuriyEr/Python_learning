# Задание 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

import time

income: str
expenses: str
dataIsCorrect = False
print("Привет! Для дальнейшей работы вам нужно ввести значения прибыли и издержек.")
time.sleep(1)
income = input("Пожалуйста введите значение выручки >> ")
time.sleep(1)
expenses = input("Пожалуйста введите значение издержек >> ")
try:
    income = float(income)
    expenses = float(expenses)
    dataIsCorrect = True
except:
    print("Вы ввели не коррректное значение.")

if dataIsCorrect and (income > expenses):
    print("Поздравляю - вы сработали в прибыль.")
    time.sleep(1)
    print("Доходность составила {} или {}%".format((income-expenses),(income/expenses*100-100)))
elif dataIsCorrect and (income < expenses):
    print("Период вышел не самый удачный? Мы сработали в убыток.")
    time.sleep(1)
    print("Убытки составили {} или {}%".format((expenses-income),(expenses/income*100-100)))