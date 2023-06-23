import numpy as np
import  matplotlib.pyplot as plt
import cv2
def Cortes(imag, alto, ancho):
    cor = imag[0:alto, 0:ancho]
    return cor
def Verificar(medida1, medida2):
    if medida1== medida2:
        medida = medida1
    elif medida1> medida2:
        medida = medida2
    elif medida2 > medida1:
        medida = medida1
    return medida
def Mostrar(imagen, nombre):
    rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.title(nombre)
    plt.axis("apagado")
    plt.show()
def plot(figura, sp, nombre, imagen):
    plt.figure(figura)
    plt.subplot(sp)
    plt.title(nombre)
    plt.imshow(imagen)
a = input("Ingrese la primera imagen con su extension: ")
b = input("Ingrese la segunda imagen con su extension:")
imagen1 = cv2.imread(a)
imagen2 = cv2.imread(b)
print(imagen1.shape)
print(imagen2.shape)
al1, an1, c1 = imagen1.shape
al2, an2, c2 = imagen2.shape
if c1 != c2:
    print("Las imagenes no tienen los mismos canales")
else:
    x = Verificar(an1, an2)
    y = Verificar(al1, al2)
    img1 = Cortes(imagen1, y, x)
    img2 = Cortes(imagen2, y, x)
bw_and = cv2.bitwise_and(img1, img2)
bw_or = cv2.bitwise_or(img1, img2)
bw_xor = cv2.bitwise_xor(img1, img2)
bw_not = cv2.bitwise_not(imagen1)
bw_not2 = cv2.bitwise_not(imagen2)
rgb1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)
rgb2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)
rgb_and = cv2.cvtColor(bw_and, cv2.COLOR_BGR2RGB)
rgb_or = cv2.cvtColor(bw_or, cv2.COLOR_BGR2RGB)
rgb_xor = cv2.cvtColor(bw_xor, cv2.COLOR_BGR2RGB)
rgb_not1 = cv2.cvtColor(bw_not, cv2.COLOR_BGR2RGB)
rgb_not2 = cv2.cvtColor(bw_not2, cv2.COLOR_BGR2RGB)
plot(1, 241, "Imagen 1", rgb1)
plot(1, 242, "Imagen 2", rgb2)
plot(1, 243, "AND", rgb_and)
plot(1, 244, "OR", rgb_or)
plot(1, 245, "XOR", rgb_xor)
plot(1, 246, "NOT1", rgb_not1)
plot(1, 247, "NOT2", rgb_not2)
plt.show()
