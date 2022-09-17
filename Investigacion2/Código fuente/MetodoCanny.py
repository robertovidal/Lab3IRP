# Uno de los métodos de biblioteca que se escogió es el de
# Canny implementado por OpenCV, la explicación del método
# se encuentra en el siguiente link: https://learnopencv.com/edge-detection-using-opencv/

import cv2
def MetodoCanny(imagen):

    # Se convierte la imagen a escala de grises
    escala_de_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Se hace la imagen blur para una mejor detección de bordes
    imagen_blur = cv2.GaussianBlur(escala_de_grises, (3,3), 0)

    # Se hace una detección de bordes de Canny
    canny = cv2.Canny(image=imagen_blur, threshold1=100, threshold2=200)


    return canny