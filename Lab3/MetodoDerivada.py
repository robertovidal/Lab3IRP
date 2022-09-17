import cv2
imagen = cv2.imread("ImagenOriginal.png")



# Se convierte la imagen a escala de grises
escala_de_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

imagen_derivada_x = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_derivada_y = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_final = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

(h, w) = escala_de_grises.shape[:2]

for x in range(h):
    for y in range (w):
        if y < (w - 1):
            imagen_derivada_x[x][y] = abs(escala_de_grises[x][y] - escala_de_grises[x][y + 1])
        else:
            imagen_derivada_x[x][y] = abs(escala_de_grises[x][y] - escala_de_grises[x][y - 1])
        if x < (h - 1):
            imagen_derivada_y[x][y] = abs(escala_de_grises[x][y] - escala_de_grises[x + 1][y])
        else:
            imagen_derivada_y[x][y] = abs(escala_de_grises[x][y] - escala_de_grises[x - 1][y])
        imagen_final[x][y] = imagen_derivada_x[x][y] + imagen_derivada_y[x][y]

cv2.imwrite("ImagenDerivadaX.png", imagen_derivada_x)
cv2.imwrite("ImagenDerivadaY.png", imagen_derivada_y)
cv2.imwrite("ImagenSuperposicion.png", imagen_final)