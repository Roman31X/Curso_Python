#La funcion for es mayor mente implemetada para iterar o recorrer listas - diccionarios - tuplas
#iniciaremos creando una lista 

dias = ['Lunes','Martes','Miercoles','Jueves','Viernes']

#declaramos dentro del ciclo for una varibale individual de la lista
for dia in dias:
    print(dia)

print('==============')

#Implementando el for para iterrar una cadena de
#carcateres como frases o palabras
dia = 'Miercoles'

for letra in dia:
    print(letra)

print('=============')
#IMPLEMENTAR EL CICLO FOR MAS LAPALABARA RESERVADA 
#BREACK PARA DETENER EL BUCLE EN EL DIA MIERCOLES
for semana in dias:
    print(semana)
    if (semana == "Miercoles"):
        break

print("=============")

#IMPLEMENTAR EL CICLO FOR MAS LAPALABARA RESERVADA 
#CONTINUE PARA OMITIR EN EL BUCLE EN DIA MIERCOLES
for semana in dias:
    if (semana == "Miercoles"):
        continue
    print(semana)

print("=============")

#IMPLEMENTAR EL CICLO FRO HASTA LLEGAR AL LIMITE ESTABLECIDO
#EN LA VARIABLE NUMERO DE ITERACIONES
#[range] : permite inicializar y finalizar el bucle
#esto quiere decir si inicia en 0 o 1 a mas y termina en 6 a mas
#el primer valor indica de que numero inicia y el segundo en cual temrinara
# si agregamos un tercer numero nos indicara en cuanto ira aumentando
for i in range(1,6,2):
    print(i)
else:
    print('Termino la iteracion hasta 6')

print('============')

#IMPLEMENTANDO ELBUCLE FOR ITERAREMOS DOS LISTAS 

lista1 = ['Lunes','Martes','Miercoles','Jueves','Viernes']
lista2 = [1,2,3,4,5]

#IMPLEMENTAMOS UN FOR ANIDADO
for lista in lista1:
    for list in lista2:
        print('El dia ',list,' es ',lista)

#en este caso se repote 5 veces los numeros de dias y los dia de la semana
#esto se debe que el for mas a la derecha de terminara de ejecutar primero
#pra dar paso a la siguiente iteracion dle proimer for






