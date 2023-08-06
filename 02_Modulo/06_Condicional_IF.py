#Cuando queremos realizar condiciones en python no es necesario
#implementar las llaves { } en este caso se implementa la identacion 
#y a su vez agregar los dos puntos :

numero = int(input('Ingrese un numero : '))

if numero > 0:
    print(f"El numero {numero} es mayor positivo")
elif numero < 0:
    print(f"El numero {numero} es menor y negativo")
else:
    print("El numero ingresado es igual a cero.")

print('ESTO FUE UNA PRUEBA DE CONDICION IF')