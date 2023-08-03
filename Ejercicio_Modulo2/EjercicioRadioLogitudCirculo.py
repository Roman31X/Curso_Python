"""
Para el presente ejercicio nos pide obtener
el radio y longitud de un circulo en python
para ello tenemos la siguiente fomrula
            area = π * r^2 
            logitud = 2 * π * r
"""
#PARA IMPLEMENTAR PI en nuestro desarrollo usaremos la funcion math
import math

radio = float (input('Ingrese el radio del circulo : '))

area = math.pi * radio**2
longitud = 2 * math.pi * radio

#PARA REDONDEAR AL MOMENTO DE MOSTRAR EL RESULTADO [:.1f] esto quiere decir 1 deimal como maximo
print(f"El area del circulo es : {area:.1f}")
print(f"la longitud del circulo es : {longitud:.1f}")

