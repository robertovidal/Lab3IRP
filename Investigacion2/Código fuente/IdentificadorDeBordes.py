import cv2
import time
from MetodoDerivada import MetodoDerivada
from MetodoSobel import MetodoSobel
from MetodoCanny import MetodoCanny

print("1) Método Derivada\n2) Método Sobel\n3) Método Canny\nDigite el número del método que quiere utilizar")
metodo = int(input())

print("Escriba el nombre de la imagen (con extensión)")
nombre_imagen = input()
imagen = cv2.imread(nombre_imagen)

if metodo == 1:
    inicio = time.perf_counter()
    imagen_final = MetodoDerivada(imagen)
    cv2.imwrite("ImagenFinalDerivada.png", imagen_final)
    final = time.perf_counter()
    print(f"Se tardó {final - inicio} segundos")

if metodo == 2:
    inicio = time.perf_counter()
    imagen_final = MetodoSobel(imagen)
    cv2.imwrite("ImagenFinalSobel.png", imagen_final)
    final = time.perf_counter()
    print(f"Se tardó {final - inicio} segundos")

if metodo == 3:
    inicio = time.perf_counter()
    imagen_final = MetodoCanny(imagen)
    cv2.imwrite("ImagenFinalCanny.png", imagen_final)
    final = time.perf_counter()
    print(f"Se tardó {final - inicio} segundos")





