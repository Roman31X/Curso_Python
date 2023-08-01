#SOLICITAR DOS NUMEROS POR TECLADO Y REALIZAR EVALUACION
#POR EL TIPO DE DATO CADENA O EMTERO

numero1 = input('Ingrese valor para A : ')

try:
    numero1 = int(numero1)
except:
    numero1 = 'Es una CADENA'

numero2 = input('Ingrese valor para B : ')

try:
    numero2 = int(numero2)
except:
    numero2 = 'Es una CADENA'

if numero1 == 'Es una CADENA' or numero2 == 'Es una CADENA':
    print('Para realizar la suma debe de ingresar numeros enteros')
else:
    print('La suma de los numeros es : ',(numero1+numero2))

print('==================================')

#PRIMERO EVALUAR ANTES DE SOLICITAR EL SIGUIENTE VALOR 
#DE NO SER UN NUMERO ENTERO TERMINARA EL PROCESO
numero3 = input('Ingrese valor para C : ')

try:
    numero3 = int(numero3)
except:
    numero3 = 'Es una CADENA'

if numero3 == 'Es una CADENA':
    print('Solo esta permitido ingresar numeros enteros')
    exit()

numero4 = input('Ingrese valor para D : ')

try:
    numero4 = int(numero4)
except:
    numero4 = 'Es una CADENA'

if numero4 == 'Es una CADENA':
    print('Solo esta permitido ingresar numeros enteros')
    exit()

print('La suma de los numeros es : ',(numero1+numero2))



