#Comparacion de conjunto de datos 
#para implementar conjunto usaremos llaves

conjuntoA = {1,3,5,7,9,11}
conjuntoB = {2,4,6,8,10,12}
conjuntoC = {1,2,3,4,5,6,7}

#Compararemos si ambos conjuntos son iguales
print(conjuntoA == conjuntoB)
print('==============')

#Para realisar union de conjuntos 
print(conjuntoA | conjuntoB)
print('==============')

#PARA OBTENER LA INTERCEPCION DE CONJUNTOS A Y C
print((conjuntoA & conjuntoC))
print('==============')

#PARA REALIZAR LA DIFERENCIA DE CONJUNTO
print (conjuntoA - conjuntoC)
print('==============')

#PARA OBTENER LA DIFERENCIA SIMETRICA DE CONJUNTO 
print ((conjuntoA ^ conjuntoC))
print('==============')

