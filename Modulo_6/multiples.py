calificacion = input('Ingrese la nota del alumno: ')

calificacion = int(calificacion)

if calificacion == 10 or calificacion == 9:
    print('A')
elif calificacion <= 8 and calificacion >= 6:
    print('B')
elif calificacion <= 5 and calificacion >= 3:
    print('C')
else:
    print('D')