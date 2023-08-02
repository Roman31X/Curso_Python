#Cuando queremos declara funciones en python tenemos que utiliar la palbra 
#reservada def 

#Por si solo una funcion no mostrara ni realizara nada
#primero deb de ser llamado con el cnombre declarado y sus parentesis
def miFuncion():
    print("Mi primera funcion en python [UwU]")

#IMPLEMETAREMOS UN FOR CON RNAGO DE 5 VECES PARA MOSTRARA
#EL MENSAJE DENTRO DE LA FUNCION PARA ELLO SE HACE EL LLAMADO
#DENTRO DEL BUCLE
for i in range(3):
    miFuncion()

print('=============')
#CREARMEOS UNA FUNCION QUE RECIBA UN PARAMETRO
def ImprimirDato(dato):
    print('El dato ingresado fue: ',dato)

#EMVIAMOS UNA PARABLETRO POR MEDIO DE LA FUNCION
ImprimirDato('Diego')
print('============')

#Creaos una funcion que reciva dos parametros distintos
def persona(nombre,edad):
    print('El nombre es ',nombre,' y su edad es ',edad)

persona('Diego Roman',23)
print('=============')

#CREAMOS UNA FUNCION CON RETORNO
def sumaDosNumeros(numero1, numero2):
    resultado = int (numero1 + numero2)
    return resultado

total = sumaDosNumeros(5,5)
print('La suma de los dos numeros es de : ',total)
print('=============')

#Funsion con recusividad, esta funcion realizara la accion de autollamarce
#siempre y cuando se cumpla un determinado valor
def recursivo(valor):
    if(valor < 1):
        return i
    print(valor)
    recursivo(valor - 1)


#Llamamos a la funcion
recursivo(5)
print('=============')