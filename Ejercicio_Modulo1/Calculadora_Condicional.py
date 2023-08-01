#DEBE SOLITAR EL TIPO DE OPERACION A REALIZAR 
#TAMBIEN SOLICITAR VALOR PARA LAS AOPERACIONES
a = int(input('Ingrese valor para A : '))
b = int(input('Ingres evalor para B : '))
operacion = input('Ingrese signo de operacion [ + - * /] : ')

if operacion == '+':
    resultado1 = a+b
    print('La suma de A + B es : ',resultado1)
elif operacion == '-':
    resultado2 = a-b
    print('La suma de A - B es : ',resultado2)
elif operacion == '*':
    resultado3 = a*b
    print('La suma de A * B es : ',resultado3)
elif operacion == '/':
    resultado4 = a/b
    print('La suma de A / B es : ',resultado4)
else:
    print("Operación no valida")