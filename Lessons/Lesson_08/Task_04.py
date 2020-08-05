"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

from enum import Enum

class TypeEquipments(Enum):
    printer = "принтер"
    scaner = "сканер"
    copier = "ксерокс"

class Equipment():
    def __init__(self, price:int, size: list, id: int, type: TypeEquipments):
        self.price = price
        self.id = id
        if len(size) == 3:
            self.size = size
        else:
            print("Кол-во переменных в list size должно быть 3")
            exit()


    def __str__(self):
        return "оборудование с id " + str(self.id)

class Warehouse():
    maxValueEquipments = 10
    currentValueEquipment = 0
    maxSizePlaceSM = [50,50,50]
    currentItems = []

