import cv2
def MetodoDerivada(imagen):

    (h, w) = imagen.shape[:2]

    valor_derivada_x = 0

    valor_derivada_y = 0



    # Se convierte la imagen a escala de grises
    escala_de_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    imagen_final = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    for x in range(h):
        for y in range (w):
            if y < (w - 1):
                valor_derivada_x = abs(escala_de_grises[x][y] - escala_de_grises[x][y + 1])
            else:
                valor_derivada_x = abs(escala_de_grises[x][y] - escala_de_grises[x][y - 1])
            if x < (h - 1):
                valor_derivada_y = abs(escala_de_grises[x][y] - escala_de_grises[x + 1][y])
            else:
                valor_derivada_y = abs(escala_de_grises[x][y] - escala_de_grises[x - 1][y])
            imagen_final[x][y] = valor_derivada_x + valor_derivada_y
    
    return imagen_final