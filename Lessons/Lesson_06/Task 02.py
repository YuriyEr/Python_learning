"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.

Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    _length: int
    _width: int
    _thickness: int

    def __init__(self, lengthMetr, widthMetr, thicknessSantimetr):
        self._length = lengthMetr
        self._width = widthMetr
        self._thickness = thicknessSantimetr

    def weightOfAsphalt(self):
        print(f"Результат на длинну {self._length} ширину {self._width} и высоту{self._thickness} вес в ТН составляет: {self._length*self._width*self._thickness/100*2.5}")

countOne = Road(5000, 20, 5).weightOfAsphalt()