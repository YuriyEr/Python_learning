"""
6. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title: str = "ABBA"

    def draw(self):
        print("This is parent class")

class Pen(Stationery):
    def draw(self):
        print("This is Pen class")

class Pencil(Stationery):
    def draw(self):
        print("This is Pencil class")

class Handle(Stationery):
    def draw(self):
        print("This is Handle class")

exemparOne = Stationery()
exemparOne.draw()

exemparTwo = Pen()
exemparTwo.draw()

exemparThree = Pencil()
exemparThree.draw()

exemparFour = Handle()
exemparFour.draw()
