#EN EL PRESENTE EJERCICIO SE INGRESARA DOS VALORES
#TANTO A COMO B TENDRAN UN VALOR PERO AL MOSTRAR
#POR CONSOLA ESTOS DEBEN DE INTERCAMBIAR SU VALOR
#A DEBE DE SER IGUAL A B Y B DEBE DE SER IGUAL A A

a = input('Ingrese valor para A : ') 
b = input('Ingrese valor para B : ') 

a,b = b,a
print("El valor de A es : ",a)
print("El valor de B es : ",b)