def promedio(*listado):
    print(listado)
    print(type(listado))

    return sum(listado) / len(listado)

resultado = promedio(10, 5, 10, 5, 10, 5)
print(resultado)