import cv2

#Con esta funcion reconocera las camras que esten conectadas
#en la pc tendra accesos a monitores conectados o celulares de la red
#0 - CAMARA DE LAPTOP#31 - CAMARA EXTERNA O CONECTADA A LA RED
camara = cv2.VideoCapture(1)

if not camara.isOpened():
    print('No se encontro camaras')
    exit()

while True:
    #Captura una imagen y lo muestra por pantalla
    tipoCamara,video = camara.read()
    gris = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    #Linea para mostrar al ventana con el vido captado por la camara
    cv2.imshow('Vivo Camra',gris)
    #Para poder salir del bucle
    if (cv2.waitKey(1) == ord ('q')):
        break

#DETENER LA CAPTURA DE VIDE
camara.release()
#Cierre o destruir la ventas con presionar una tecla
cv2.destroyAllWindows()
