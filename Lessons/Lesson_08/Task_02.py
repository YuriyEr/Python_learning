"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class userExeptionZeroDevision(Exception):
    errorName = "Вы пытаетесь осуществить деление на ноль"


class mathOpration:
    def __init__(self, value: int):
        self.value = value

    def __truediv__(self, other):
        if other.value == 0:
            raise userExeptionZeroDevision
        else:
            return self.value / other.value

someValuesA = mathOpration(10)
someValuesB = mathOpration(0)

try:
    newValue = someValuesA / someValuesB
except userExeptionZeroDevision as error:
    print(error.errorName)
