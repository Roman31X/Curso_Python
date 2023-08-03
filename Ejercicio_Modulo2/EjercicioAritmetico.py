"""
PARA EL PRESENTE EJERCICIO SE SOLICITA INGRESAR 
3 NUMEROS UN VALOR PARA A UN VALOR PARA B Y POR ULTIMO 
UN VALOR PARA C.
DESPUES SE DEBE DE RESOLVER LA SIGUIENTE ECUACION

    ( C + 5 ) (B^2 - 3AC)A^2
    --------------------------
                4A

"""
a = float(input('Ingrese un numero para A : '))
b = float(input('Ingrese un numero para B : '))
c = float(input('Ingrese un numero para C : '))

respuesta = ((c+5)*((b**2)-(3*a*c)))*a**2/(4*a)
print('La respues de la ecuacion es de : ',respuesta)