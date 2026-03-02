#Se importa reduce desde functools ya que en Python 3 no es una función built-in

from functools import reduce
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#4a — Cuadrados con map

cuadrados = list(map(lambda x: x ** 2, lista))
# → [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#4b — Pares con filter

pares = list(filter(lambda x: x % 2 == 0, lista))
# → [2, 4, 6, 8, 10]
#4c — Suma con reduce

suma_total = reduce(lambda a, b: a + b, lista)
# → 55
#4d — Producto con reduce

producto = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
# → 120  (equivalente a 5!)