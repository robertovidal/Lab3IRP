import cv2
import time
from MetodoDerivada import MetodoDerivada

print("1) Método Derivada\n2) Método 2\n3) Método 3\nDigite el número del método que quiere utilizar")
metodo = int(input())

print("Escriba el nombre de la imagen (con extensión)")
nombre_imagen = input()
imagen = cv2.imread(nombre_imagen)

if metodo == 1:
    inicio = time.perf_counter()
    imagen_final = MetodoDerivada(imagen)
    cv2.imwrite("ImagenFinal.png", imagen_final)
    final = time.perf_counter()
    print(f"Se tardó {final - inicio} segundos")





