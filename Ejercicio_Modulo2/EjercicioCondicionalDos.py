#EL PRESENTE EJERCICO NOS PIDE SOLICITAR TRES NUMEROS POR TECLADOS Y DETERMINAR CUAL ES 
#EL MAYOR DE LOS NUMEROS INGRESADOS

a = int(input('Ingrese valor para A : '))
b = int(input('Ingrese valor para B : '))
c = int(input('Ingrese valor para C : '))

if a > b and a > c:
    print(f"El numero {a} es mayor que {b} y {c}")
elif b > a and b > c:
    print(f"El numero {b} es mayor que {a} y {c}")
else:
    print(f"El numero {c} es mayor que {a} y {b}")

