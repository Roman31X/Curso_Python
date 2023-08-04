#En el presente ejercicio se pide realizar la simulacion
#donde se desea que realice los siguienetes funciones 
# ingreso de dinero - retirar dinero - mostrar dinero - salir

saldo = 2000
print(f"Saldo inicial: {saldo}")
print('============')

print('[1] - Ingresar dinero')
print('[2] - Retirar dinero')
print('[3] - Mostrra saldo')
print('[4] - Salir')

opcion = int(input('Ingrese la opcion a realizar : '))

if opcion == 1:
    ingreso = float(input('Ingrese el nuevo monte a registrar : '))
    saldo +=ingreso
    print('El nuevo saldo es :',saldo)
elif opcion == 2:
    retiro = float(input('Ingrese cantidad a retirar : '))
    if (retiro > saldo):
        print("No hay suficiente dinero")
    else:
        saldo -=retiro
elif opcion == 3:
    print ('Su saldo actual es:',saldo)
elif opcion == 4:
    print('Gracias por usar nuestro cajero [UwU]')
else:
    print('La opcion escogida no esta dentro del menu')
