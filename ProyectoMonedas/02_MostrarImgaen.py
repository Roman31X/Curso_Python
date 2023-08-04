#IMPORTAMOS EL PAQUETE DE CV2
import cv2
#DECLARAMOS UNA VARIABLE QUE CONTENGA LA RUTA DE L AIMAGEN
imagen = cv2.imread(r".\ProyectoMonedas\imagenes\imagen_01.jpg")
#DECLARAMOS UN NOMBRE A LA VENTANA QUE CONTENDRA LA IMAGEN
Windows_name = 'imagen'
#CON LA FUNCION .imshow necesita del nombre de la ventana y la imagen a mostrar
cv2.imshow(Windows_name, imagen)
#con la funcion .waitkey contiene el tipo de visualizacion de 0 para imagenes y de 1 en adelante para video y camara
cv2.waitKey(0)
#Con la sigueinete funcion cerrar todas ventanas emergentes similares 
cv2.destroyAllWindows()

