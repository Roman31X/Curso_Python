#LAS TUPLAS SON SIMILARES A LA LISTA CON LA ECEPCION
#DE QUE UNA VEZ CREADAS ESTAS NO SE PUEDEN MODIFICAR

#CREAR UNA TUPLA USAMOS LOS PARENTESIS [PARENTESIS = ()]
tupla = ('Lunes','Martes','Miercoles','Jueves','Viernes')
print(tupla)
print('==========')

#ESTA CUENTA CON MENOS NUMEROS DE METODOS
#CONTAR LA CANTIDAD DE CONTENIDO
print(tupla.count('Martes'))
print('==========')

#PARA DEVOLVER LA POSICION DEL ELEMENTO
print(tupla.index('Martes'))
print('==========')
print(tupla[tupla.index('Martes')]) #Consigo la ubicacion y la muestro con su numero
posicion = tupla.index('Miercoles') #Consigo primero el numero
print(tupla[posicion]) #Coloco el numero dentro de los corches para mostrara la posicion
print('==========')

#CONVERTIR UNA TUPLA A LISTA
listaDias = list(tupla)
print(listaDias)
listaDias.append('Sabado')
listaDias.append('Domingo')
print(listaDias)



