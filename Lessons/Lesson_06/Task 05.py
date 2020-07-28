"""
5. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

# Не очень понял к чему данное задание - поэтому сделал на основе произвоьных данных
class SomeClassOne:
    atributOne: int
    atributTwo: bool
    atributThree = 10
    counter = 0

    def __init__(self, atributOne, atributTwo):
        self.atributOne = atributOne
        self.atributTwo = atributTwo
        SomeClassOne.counter += 1

    def printCounter(self):
        print(SomeClassOne.counter)

exemplarOne = SomeClassOne(200, True)
exemplarOne.atributOne = 10
exemplarOne.printCounter()

exemplarTwo = SomeClassOne(100, False)
print(exemplarTwo.atributOne)

# демонстрация типа ссылки (рефернса)
exemplarTrhee = exemplarOne
print(exemplarTrhee.atributOne)
exemplarOne.atributOne = 999
print(exemplarTrhee.atributOne)
# таким образом экземпляр 3 == экземпляру 1 (ссылочное значение) и не имеет собственного значения, тип 3 не экземпляр а ссылка
exemplarTrhee.printCounter() # счетчик также не поменялся - значение 2 что говорит что 3 экземпляр ссылка
