#La incorporacion de una lista o Array list nos permite contener
#distintos tipos de datos 

array = ['Lunes','Martes','Miercoles','Jueves',1,2,3,4,['a','b','c','d'],True,False]

#MOSTRRA TODO EL ARRAY
print(f'El contenedio del array es {array}')
print('=============')
#PARA MOSTRAR LA POSICION 8 DONDE SE ENCUENTRA EL SEGUNDO ARRAY
print(array[8])
print('=============')
#PARA MOSTRARA EL ULTIMA POSICION DEL ARRAY
print(array[-1])
print('=============')
#PARA MOSTRARA CIERTA CANTIDAD DE CONTENEIDO DEL ARRAY
# el primero indica la posicion
# el segundo indica la cantidad 
# el tercero indica de cuanto incrementa el recorrido
print(array[0:6:2])
print('=============')
#FUNCION PARA CONTAR LA CANTIDAD DE DATOS DENTRO DE UNA LISTA
print(len(array))
print('=============')
#AGREGAR NUEVO DATO A LA LISTA
array.append("Sabado")
print(array,' ultimo dato es ',array[-1])
print('=============')
#Agregar un dato nuevo en la posicion asignada
array.insert(0,"Domingo") 
print(array)
print('===============')
#Concaterar dos listas
array1 = [1,2,3,4,5]
array2 = ['Lunes','Martes','Mieroles','Jueves','Viernes']
array3 = array1+array2
print(array3)
print('=============')
#Encontrra unvalor dentro de nuestro array list
print("Martes" in array3)
print('===========')
#Averiguar el numero de index o ubicacion de un dato en el array
print(array.index('Martes'))
print('===========')
#Contar cuantas veces se repite un elemento dentro de un array list
print (array.count('Martes'))
print('==============')
#Para remover un dato del arraylit
print(array.remove("Martes"))
print(array)

