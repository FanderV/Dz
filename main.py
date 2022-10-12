# 1 задание

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))


def minimum(a, b, c):
    return min(a, b, c)


print("Наименьшее число:", minimum(a, b, c))