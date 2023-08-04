import cv2

#VARIBALES CON MODIFICACIONES EN LA IMAGEN
imagen = cv2.imread(r".\ProyectoMonedas\imagenes\imagen_01.jpg")
#OBTENER LA IMAGEN EN COLOR GRIS
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
#OBTENER IMAGEN CON HUMBRAL DE 0 A 100 TOMARA LAS IMAGENES MAS CLARAS MENOS DIGITOS
#ESTA NECESITA DOS VARIBALES PERO PODEMOS OMITIRLA INGRESANDO GION BAJO _
_,umbral = cv2.threshold(gris,100,255,cv2.THRESH_BINARY)
#OBTENEDREMOS EL CONTORNO DE LA IMAGEN
contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#CAPTURAR EL CONTORNO 
cv2.drawContours(imagen,contorno,-1,(247,0,0),3)

#NOMBRE DE VENTANA DE IMAGEN
ventana1 = 'Ventana Imagen COLOR [UwU]'
ventana2 = 'Ventana Imagen GRIS [UwU]'
ventana3 = 'Ventana Imagen UMBRAL [UwU]'

#MOSTRAR LA IMAGENES EN LAS VENTANAS
cv2.imshow(ventana1, imagen)
#cv2.imshow(ventana2, gris)
#cv2.imshow(ventana3, umbral)

#DURACION Y DESTRUCION DE VENTANAS
cv2.waitKey(0)
cv2.destroyAllWindows()