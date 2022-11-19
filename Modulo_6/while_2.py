numero = 1234

contador_digitos = 0

while numero >=1:
    #contador_digitos = contador_digitos + 1

    contador_digitos +=1

    numero = numero / 10
else:
    print("Se acabo el ciclo while")

print(contador_digitos)

"""la forma de abreviar el variable = variable 
+ numero es: variable += numero"""


