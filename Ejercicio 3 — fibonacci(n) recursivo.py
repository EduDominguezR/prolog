#Caso base: fibonacci(0) = 0 y fibonacci(1) = 1. 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

