# Uno de los métodos de biblioteca que se escogió es el de
# Sobel implementado por OpenCV, la explicación del método
# se encuentra en el siguiente link: https://learnopencv.com/edge-detection-using-opencv/

import cv2
def MetodoSobel(imagen):

    # Se convierte la imagen a escala de grises
    escala_de_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Se hace la imagen blur para una mejor detección de bordes
    imagen_blur = cv2.GaussianBlur(escala_de_grises, (3,3), 0)

    # Se hace una detección de bordes de Sobel del eje X y Y combinadps
    sobelxy = cv2.Sobel(src=imagen_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

    return sobelxy
