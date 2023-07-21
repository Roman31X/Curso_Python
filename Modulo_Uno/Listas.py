#DECLARA UNA LISTA USAR (CORCHETES = [])
#lista de cadena de letras
listaDias = ['Lunes','Martes','Miercoles','Jueves','Viernes']
print(listaDias)
print("============")

#Agregar mas datos a la lista con metodo .append()
listaDias.append('Sabado')
listaDias.append('Domingo')
print(listaDias)
print("============")

#Lista de numeros
listaDiasSemana = [1,2,3,4,5]
print(listaDiasSemana)
print("============")
listaDiasSemana.append(6)
listaDiasSemana.append(7)
print(listaDiasSemana)
print('============')

#COPIAR UNA LISTA YA RELLENA AOTRA VARIABLE .copy()
listaCopia1 = listaDiasSemana.copy()
print('Copia antes: ',listaCopia1)
listaCopia1.append(8)
listaCopia1.append(9)
listaCopia1.append(10)
listaCopia2 = listaCopia1.copy()
print('Lista Copia Agregando: ',listaCopia2)
print('============')

#ELIMINATR TODOS LOS ELEMNTO DE LA LISTA
listaCopia3 = listaCopia2.copy()
listaCopia3.clear()
print(listaCopia3)
print('============')

"""CONTAR UN ELEMNTO Y VER CUNATAS VECES
SE REPITE DENTRO DE UNA LISTA DENTRO DE UNA LISTA"""
#.count('valor')
print(listaCopia2.count(8))
print('============')

#CONTADOR DE CUANTOS ELEMENTOS EXISTE DENTRO DE LA LISTA
print(len(listaDias),len(listaDiasSemana),len(listaCopia2))
print('============')

#ASIGNAR EL TAMAÑO DE LA LISTA A UNA VARIABLE
tamaño = len(listaDias)
tamaño1 = len(listaCopia2)
print(tamaño,tamaño1)
print('============')

#ACCEDIENDO AL ELEMENTO EN POSICION
print(listaDias[0])
print(listaDias[6])
print('=============')

#ELIMINAR ELEMENTOS DE UNA LISTA
#Eliminar el ultimo elemento de la lista
print(listaDias)
listaDias.pop()
listaDias.pop()
print(listaDias)
print('=============')

#ELIMINAR UN ELEMENTO EN LA LISTA EN ESPECIFICO
listaDias.remove('Miercoles')
listaDias.remove('Viernes')
print(listaDias)
print('=============')

#INVERTIR EL ORDEN DE LA LISTA
print(listaDiasSemana)
listaDiasSemana.reverse()
print(listaDiasSemana)
print('=============')

#LISTA CON DIVERSOS TIPOS DE DATOS
ListaDatos = ['Lunes',1,'Martes',2,'Miercoles',3,'Jueves',4,'Viernes',5]
print(ListaDatos) #este tipo de losta no se puede ordenar
ListaDatos.reverse() #pero si se puede invertir
print(ListaDatos)

#ORDENAR EL CONTENDIO DE UNA LISTA DE MAYOR A MENOR DEL MISMO TIPO
nuevaLista = listaDias.copy()
nuevaLista.sort()
listaDiasSemana.reverse() #INVIERTO LA LISTA
listaDiasSemana.sort() #ORDENA LA LISTA DE MAYOR A MENOR 
print(nuevaLista) 
print(listaDiasSemana)