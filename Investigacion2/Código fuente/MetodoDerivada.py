import cv2
def MetodoDerivada(imagen):

    (h, w) = imagen.shape[:2]

    valor_derivada_x = 0

    valor_derivada_y = 0



    # Se convierte la imagen a escala de grises
    escala_de_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Se hace la imagen blur para una mejor detección de bordes
    imagen_blur = cv2.GaussianBlur(escala_de_grises, (3,3), 0)

    imagen_final = cv2.GaussianBlur(escala_de_grises, (3,3), 0)
    
    # Se calcula la derivada de la imagen en X y Y y el resultado de la suma de ambas se guarda
    # en la imagen final
    for x in range(h):
        for y in range (w):
            if y < (w - 1):
                valor_derivada_x = abs(imagen_blur[x][y] - imagen_blur[x][y + 1])
            else:
                valor_derivada_x = abs(imagen_blur[x][y] - imagen_blur[x][y - 1])
            if x < (h - 1):
                valor_derivada_y = abs(imagen_blur[x][y] - imagen_blur[x + 1][y])
            else:
                valor_derivada_y = abs(imagen_blur[x][y] - imagen_blur[x - 1][y])
            imagen_final[x][y] = valor_derivada_x + valor_derivada_y
    
    return imagen_final