diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

llaves = tuple(diccionario.keys())

valores = tuple(diccionario.values())

objetos = tuple(diccionario.items())

print(llaves)
print(valores)
print(objetos)

print(len(diccionario))

valor = diccionario.pop('c')

del diccionario['a']

print(len(diccionario))