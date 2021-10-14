mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)
filtrado2 = filter(lambda x: x % 2 == 0, mi_lista)

print(list(filtrado))
print(list(filtrado2))