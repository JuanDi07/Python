lista_1 = ['Manzana','Pera','Naranja','Uva','Sandia']

print(lista_1[2])

#Las listas comienzan en 0, pero se puede leer en negativo tambien

lista_1[2] = 'Melon'

print(lista_1[2])

print(lista_1[0:3])

#Para las sub listas es (variable[inicio:final]) 

lista_1.append('Guayaba')
print(len(lista_1))
print(lista_1)

#append sirve para agregar un elemento al final de la lista

lista_1.insert(0, 'Durazno')
lista_1.insert(5, 'Limon')
print(lista_1)

#insert nos permite agregar un elemento a una lista
#para esto es: variable.insert(N_posicion, elemento a agregar)

lista_2 = ['Coco', 'Mandarina', 'Aguacate']
lista_1.extend(lista_2)
print(lista_1)

#extend sirve para agregar una lista a otra

del lista_2[2]
print(lista_2)

#del es una palabra reservada para eliminar elementos

lista_2.clear()
lista_2.append('Maracuya')
print(lista_2)
print(len(lista_2))