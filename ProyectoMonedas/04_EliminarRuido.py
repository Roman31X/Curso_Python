import cv2

#AL IMPORTAR NUMPY NOS PERMITE UTILIZAR LIBRERIAS QUE CONTINENE FUNCIONES DE CALCULO
#DE MATRICES NECESARIAS PARA LA ELIMINACION Y MANIPULACION DE IMAGENES
import numpy as np

#VARIABLES SOLICITADAS PARA DESAPARACER EL RUIDO
var1 = 3
#VARIABLE PARAMATRICES DE NNUMPY
var2 = 5

original = cv2.imread(r".\ProyectoMonedas\imagenes\Monedas.jpg")
gris = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
#FUNCION PARA REALIZAR EL ANALISIS DE IMAGEN SU SUABIZAR LOS CONTORNO DE UNA 
#IMAGEN BORROZA PAR UNA MEJOR ANALISIS
gaus = cv2.GaussianBlur(gris,(var1,var1),0)

#ELIMINAR RUIDO DE IMAGEN UNA MEJOR ENFOQUE
canny = cv2.Canny(gaus,60,100)

#VARIBALES QUE OBTENER LOS CONTORNOS DE LAS MONEDAS
#SE REALIZA UNA TRANSFORMACION A MATRIS DE 8Bts
kernel = np.ones((var2,var2),np.uint8)

#PARA REALIZAR EL CIERRE DE LOS CONTORNOS DE LAS MONEDAS o tambien conocido
#transformacion morfologica
cierre = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernel)

contorno, jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("MONEDAS ENCONTRADAS : ",format(len(contorno)))

cv2.drawContours(original,contorno,-1,(0,0,255),2)

#Nombre de las ventas
ventana1 = 'Ventana Imagen COLOR GRIS [UwU]'
ventana2 = 'Ventana Imagen COLOR GAUS [UwU]'
ventana3 = 'Ventana Imagen COLOR CANNY [UwU]'
ventana4 = 'Ventana Imafen Color Ciere [UwU]'
ventana5 = 'Ventana Imagen COLOR CONTORNO [UwU]'


cv2.imshow(ventana1, gris)
#cv2.imshow(ventana2, gaus)
#cv2.imshow(ventana3, canny)
#cv2.imshow(ventana4,cierre)
cv2.imshow(ventana4, original)

cv2.waitKey(0)
cv2.destroyAllWindows()



