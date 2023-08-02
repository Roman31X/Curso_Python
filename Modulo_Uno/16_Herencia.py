#Cuando implementamos herenia en python este debe de implementar 
#en la declaracion de la clase los parentesis ()

##CLASE NORMAL
class Alumno:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Bienvenido Alumno :',self.nombre,self.apellido)

##CLASE CON HERENCIA
class Admin(Alumno):
    def SuperUsario(self):
        print("Usuario administrador : ",self.nombre,self.apellido)


#CREAMOS UN OBJETO DE LA CLASE ALUMNO Y UN OBJETO DE LA CLASE ADMINISTRADOR
alumno1 = Alumno('Diego','Roman') #INICIALIZACION DEL OBJ
alumno1.saludo()

admin1 = Admin('Diego','Guerra')
admin1.SuperUsario()




