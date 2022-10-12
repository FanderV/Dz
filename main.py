# задание 3
n = int(input("Введите число n: "))


def sum(n):
    summa = 0
    for i in range(1, n + 1):
        summa = summa + i
    return summa


print("Сумма чисел:", sum(n))
