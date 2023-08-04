#En el presente ejercicio solicita ingresar dos nombres 
#o cadena de caracteres para ser evaluadas si inicia
#con la misma letra y termine con la ultima letra

nombre1 = input('Ingrese un nombre : ')
nombre2 = input('Ingrese un segundo nombre : ')

if nombre1[0] == nombre2[0] and nombre1[-1] == nombre2[-1]: 
    print('Si exite coincidencia cuando inicie y temrine el nombre')
else:
    print('No coinciden el inicio con el final')


