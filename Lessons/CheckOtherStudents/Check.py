def my_func1():
    try:
        x, y = float(input('Введите положительное действительное число x: \n')),\
               int(input('Введите целое отрицательное число y: \n'))
    except:
        print("Вы ввели не корректное значение")
        exit()

    if x > 0 and y < 0:
        return x**y
    else:
        print('Вы ввели неправильные числа')

print(my_func1())