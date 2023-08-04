#IMPLEMETANDO EL BUCLE WHILE
numero = 0
tabla = 2
print('|| Tabla del 2 ||')
print('||=============||')
while numero < 12:
    print(f"|| {tabla} x {numero} = {tabla * numero}")
    numero +=1
    print('||=============||')

#BUCLE DEL CUAL NO SE PODRA SALIR HASTA QUE INGRESE 0
dato = int(input('Ingrese ucalquier numero y 0 para salir : '))
while dato != 0:
    print('El numero ingresado es : ',dato)
    dato = int(input('Ingrese un numero y 0 para salir : '))

