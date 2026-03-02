#Casos base: fibonacci(0) = 0 y fibonacci(1) = 1. El caso recursivo suma los dos anteriores .

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
#Secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...