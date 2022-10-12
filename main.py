n = int(input("Введите число: "))

def factorial(n):
    sum = 1
    for i in range(2,n+1):
        sum=sum*i

    return sum


print("Факториал числа", n , "=" , factorial(n))
