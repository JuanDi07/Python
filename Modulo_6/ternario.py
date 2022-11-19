#Esto es un caso normal

'''calificacion = input('Ingrese un numero: ')

calificacion = int(calificacion)

color = None

if calificacion >= 7:
    color = 'Verde'
else:
    color = "Rojo"

print(color)'''

#Esto es un caso mas normal en Python

calificacion = input('Ingrese un numero: ')

calificacion = int(calificacion)

color = 'Verde' if calificacion >= 7 else "Rojo"

print(calificacion, color)