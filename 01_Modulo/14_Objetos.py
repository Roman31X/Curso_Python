#Para la creacion de clases en PYTHON primero atepondemos 
#la palabra resevada class NOMBRE:
class Persona:
    nombre = "Diego"
    apellido = "Roman"

#instaciamos un objeto de la clase Persona()
usuario = Persona()
print('El nombre del usuario es [',usuario.nombre,'] y su apellido [',usuario.apellido,']')


#IMPLEMENTAREMOS UNA CLASE CON UNA FUNCION DENTRO PARA 
#RECEPCION DE ARGUMENTOS
class Alumno:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido

print('=============')
#Creamos dos objetos para realizar preuba de envio de argumento
# Alumno1 y ALumno2
Alumno1 = Alumno('Diego','Roman')
Alumno2 = Alumno('Daniel','Cavero')

print('Datos del alumno : ',Alumno1.nombre,Alumno1.apellido)
print('Datos del alumno : ',Alumno2.nombre,Alumno2.apellido)
print('=============')

