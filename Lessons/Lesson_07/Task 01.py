"""
1.
A
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

B
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

C
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""

horValues = [[4,1,2,3], [1,4,6,7], [5,6,8,5]]

# A
class Matrix:
    def __init__(self, horizontalValues: [[int]]):
        self.horizontal = horizontalValues

    def __str__(self):
        matrixSTR = ""
        for line in self.horizontal:
            matrixSTR += f"{str(line)}\n"
        return  f"Загружена матрица:\n{matrixSTR}"

    def __add__(self, other):
        newList = list()
        if not isinstance(other, Matrix):
            return None
        if len(self.horizontal) != len(other.horizontal):
            return None

        for num in range(0, len(self.horizontal)):
            line = list()
            for value in range(0, len(self.horizontal[num])):
                line.append(self.horizontal[num][value] + other.horizontal[num][value])
            newList.append(line)
            line = None
        return newList


matrixA = Matrix(horValues)
# B
print(matrixA)

# C
matrixB = Matrix(horValues)
matrixC = matrixA + matrixB
print(matrixC)
