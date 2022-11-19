usuarios = [ 'Eduardo', 'Fernando', ' Uriel', 'Rafael']

diccionario = {usuario:position + 1
    for position, usuario in enumerate(usuarios) }

print(diccionario)