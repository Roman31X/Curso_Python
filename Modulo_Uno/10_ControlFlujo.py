#Control de flujo de condicionales
if 5 > 3:
    print("5 es mayor que 3") #Este bloque se ejecuta si la expresión es verdadera

print('================')
#EVALUACIONES EN CONDICIONES

"""
a == b : a y b es igual
a < b : a es menor a b
a > b : a es mayor a b
a != b : a es diferente de b
a <= b : a es menor igual a b
a >= b : a es mayor igual a b
"""

#Verificar si dos variable son igules cadenas
nombre1 = "Diego"
nombre2 = "Diego"
if nombre1 == nombre2:
    print("Las dos variables continen la misma cadena")
else:
    print("Las dos variables no contienen las mismas cadena")

print('================')
#Evaluar con elif
if 5 > 10:
    print('5 es menor que 10')
elif 50 > 4:
    print('50 es mayor que 4')
else:
    print('Ninguna expresión anterior fue True.') #solo es verdad si la condiciones anteriores son false

print('================')
#CONDICION EN UNA SOLA LINEA [TERNARIO]
print('Verdad en una sola linea') if 4 < 5 else print('Valor falso en una sola linea')

print('================')

#EVALUACION DE AND O OR
#AND 
if 2 < 5 and 3 < 5:
    print('Ambas evaluaciones dio true')
else:
    print('Una de las condiciones no se cumplio')

print('================')

#OR
if 4 < 5 or 5 < 4:
    print('Una de las condiciones dio TRUE')
else:
    print('Ninguna de las condiciones dio TRUE')


