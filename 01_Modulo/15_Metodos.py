#Para lla implementacion de un metodo dentro de una clase
#primero tenemos que identificar bien la identacion
#de las lineas de codigo 
#PARA LOS METODOS LA INSTANCIA self no es necesaria pero 
#cuando este codigo es revisado por alguien mas y se hace el llmado de la varibales
#esta palabra resevada ayuda en la identificacion de donde se esta llamando
#Self puede ser remplasado por otra plabra prefija 

class Alumno:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido= apellido

    def binevenida(self):
        print('Bienvenido alumno : ',self.nombre,self.apellido)


Alumno1 = Alumno('Diego','Roman')
Alumno2 = Alumno('Daniel','Cavero')

Alumno1.binevenida()
Alumno2.binevenida()
print('===============')

#Si implemetamos el prefijo Del antes del objeto este eliminara
#el valor asignado en el objeto
del Alumno2.nombre
Alumno2.binevenida #Ahora al ejecutar  esta linea no arrojara nada ya que el metodo
# de la clase Alumno requiere el argumento de nombre que a sido eliminado

