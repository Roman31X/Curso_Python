#DICCIONARIO CON MAS DICCIONARIOS DENTRO
mascotas = {
    "perro": {
        "nombre":"Firulais",
        "edad": 3,
    },
    "gato":{
        "nombre":"Garfield",  
        "edad": 5,
    }
}

print(mascotas)
print('=============')

#CREAR CONSTANTES QUE ALMACENENE INFORMACION
loro = {
    "nombre": "Toribio",
    "edad": 5,
}
Caballo = {
    "nombre" : "Juan",
    "edad": 4,
}
animales = {
    'loros': loro,
    'caballos' : Caballo
}
print(animales)
print('===========')

#CREANDO DICCIONADIO CON CONSTRUCTOR [ dict ]
perritos = dict(nombre = 'Tobi',edad = 2)
print(perritos)



