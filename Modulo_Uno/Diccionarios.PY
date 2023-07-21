#AGREGAR EL PRIMER DICCIONARIO
#SE UASA:
#[llaves = {} - COMILLAS COBLES = "" - DOS PUNTOS = : - COMA = ,]

diccionario = {
    "nombre" : "Diego",
    "apellido" : "Roman",
    "edad" : 23,
    "sexo" : "masculino"
}

print(diccionario)
print('=====MOSTRAR [DATO]=====')

#COMO OBTENER UN VALOR DE MI DICCIONARO
print(diccionario['nombre'])
print(diccionario["apellido"])
print('=====MOSTRAR GET=====')

#METODO PARA ACEDER ELEMENTO DEL DICCIONARIO sin []
print(diccionario.get('nombre'))
print('=====MODIFICAR DATO=====')

#CAMBIAR VALOR A UN ELEMNTO DLE DICCIONARIO usar []
diccionario ['edad'] +=1 #aumentar edad en uno
print(diccionario.get('edad'))
print('=====AGREGA DATO=====')

#AGREGAR UN VALOR AL DICCIONARIO
diccionario['estado'] = 'Soltero'
print(diccionario)
print('=====ELIMINAR POR VALOR=====')

#ELIMINAR UN ELEMENTO DEL DICCIONARIO EN ESPECIFICO
diccionario.pop('estado')
print(diccionario)
print('=====ELIMINA ULTIMO=====')

#ELIMINAR EL ULTIMO VALOR DEL DICCIONARIO
print(diccionario)
diccionario.popitem()
print(diccionario )
print('=====DEL=====')

#ELIMINAR USANDO [ del ]
del diccionario['apellido']
print(diccionario)
print('=====COPIA I=====')

#COPIA DE DICCIONARIO
copiaDiccionario = diccionario.copy()
print(copiaDiccionario)
print('====COPIA II====')

#METODO DE COPIA dic()
nuevodiccionario = dict (diccionario)
print(nuevodiccionario)
print('=====ELIMINAR TODOS LOS DATOS DICCIONARIO=======')

#ELIMINAR TODOS LOS DATOS DEL DICCIONARIO
copiaDiccionario.clear()
print(copiaDiccionario)


