#Creamos una variable de contador
contador = 0

#Creamos la condicion en el bucle While
while contador < 5:
    print(contador)
    contador+=1

print('==========')

#Creamos un buvle con condicion para realizar break
#cuando el contadro llegue a 3
contador = 0
while contador < 5:
    if contador <= 3:
        print(contador)
    else:
        break
    contador+=1

print('==========')

#CREAMOS UN BUCLE IMPLEMENTANDO EL CONTINUE
#AHORA EMPRIMIR DEL 1 A 5 PERO NO EL 3
contador = 0
while contador < 5:
    contador+=1
    if contador == 3:
        continue
    else:
        print(contador)


