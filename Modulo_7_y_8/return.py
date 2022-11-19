def saludar():
    def mostrar_mensaje():
        print("Hola")

    return mostrar_mensaje

respuesta = saludar()

respuesta()

#Esto se hace para retornar funciones