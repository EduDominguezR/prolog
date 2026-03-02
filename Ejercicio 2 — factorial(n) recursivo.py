#Caso base: n == 0 o n == 1 retorna 1. Caso recursivo: multiplica n por factorial(n-1)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
