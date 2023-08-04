import cv2

imagen = cv2.imread(r".\ProyectoMonedas\imagenes\imagen_01.jpg")
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)


#MOSTRAR IMAGEN
ventana1 = 'Ventana Imagen COLOR [UwU]'
ventana2 = 'Ventana Imagen GRIS [UwU]'


cv2.imshow(ventana1, imagen)
cv2.imshow(ventana2, gris)
cv2.waitKey(0)
cv2.destroyAllWindows()