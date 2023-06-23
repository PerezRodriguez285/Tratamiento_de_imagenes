"""
Created on Fri Mar  5 10:13:37 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Histograma sin usar funciones de OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
		   Luis Angel Diaz Navas
           Miguel Angel Flores Urbina
Profesora: Mtra. Edith Cristina Herrena Luna
           
"""
import numpy as np
import matplotlib.pyplot as plt
#import cv2
import statistics as stats
imagen = input("Ingresa el nombre de la imagen con su extension: ")

img = plt.imread(imagen)

print( img.shape )
print( img.size )
alto, ancho = img.shape[0:2]

print(alto)
print(ancho)

red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

plt.imshow(red)
plt.title("Rojo")
plt.axis("off")
plt.show()

plt.imshow(green)
plt.title("Verde")
plt.axis("off")
plt.show()

plt.imshow(blue)
plt.title("Azul")
plt.axis("off")
plt.show()

hb= np.zeros((256,1))
hg= np.zeros((256,1))
hr= np.zeros((256,1))

for i in range(alto):
    for j in range (ancho):
        b = img.item(i, j, 2)
        g = img.item(i, j, 1)
        r = img.item(i, j, 0)
        hb[b] = hb[b]+1
        hg[g] = hg[g]+1
        hr[r] = hr[r]+1

plt.plot(hb,color = 'b')
plt.title("Azul")
plt.xlim([0,256])
plt.show()

plt.plot(hg,color = 'g')
plt.title("Verde")
plt.xlim([0,256])
plt.show()

plt.plot(hr,color = 'r')
plt.title("Rojo")
plt.xlim([0,256])
plt.show()

plt.hist( blue.ravel(), bins=256 )  
plt.title("Azul")
plt.show()

plt.hist( green.ravel(), bins=256 )  
plt.title("Verde")
plt.show()

plt.hist( red.ravel(), bins=256 )  
plt.title("Rojo ")
plt.show()

print("Promedio")
imagen =[alto,ancho]
print(stats.mean(imagen)) 
print("Desviacion estandar")
imagen =[alto,ancho]
print(stats.pstdev(imagen))
