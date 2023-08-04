#En el presente ejercicio se solicita dos datos por teclado para ser evaluados
#si son numeros pares

numero1 = int(input('Ingrese un numero para A: '))
numero2 = int(input('Ingrese un numero para B: '))

#SACAMOS EL MODULO O RESIDUO DEL NUMERO

resultadoA = numero1 % 2
resultadoB = numero2 % 2

#Condicion
if resultadoA == 0 and resultadoB == 0:
    print("Los números ingresados son pares")
elif resultadoA == 0:
    print(f"El numero {numero1} es par y el numero {numero2} es impar")
elif resultadoB == 0:
    print(f"el numero {numero2} es par y el numero {numero1} es impar")
else:
    print(f"Los dos numeros {numero1,numero2} ingresado son impares")