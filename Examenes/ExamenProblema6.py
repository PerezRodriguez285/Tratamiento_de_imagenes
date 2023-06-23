# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:29:32 2021

Alumno: Antonio Alberto de la Luz Perez Rodriguez
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors 
plt.rcParams['image.cmap'] = 'gray'
from skimage import io

image = io.imread('C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/paisaje2.jpg')
image=image/255.
print("Dimensiones de la imagen: %s" % str(image.shape))
h,w,c=image.shape

print("Tipo de los elementos de la imagen: %s" % str(image.dtype))

#visualizamos la imagen
plt.imshow(image)

green=np.copy(image)
green[:,:,0]=0
green[:,:,2]=0
plt.figure()
plt.imshow(green)

#Anulo los canales azul y verde para ver solo el rojo
red=np.copy(image)
red[:,:,1:3]=0
plt.figure()
plt.imshow(red)

#Anulo los canales rojo y verde para ver solo el azul
blue=np.copy(image)
blue[:,:,0:2]=0
plt.figure()
plt.imshow(blue)

image_hsv=matplotlib.colors.rgb_to_hsv(image)

print("El pixel de la posición (100,100) se codifica en RGB como %s " % str(image[100,100,:]))
print("El pixel de la posición (100,100) se codifica en HSV como %s " % str(image_hsv[100,100,:]))

plt.figure()
plt.imshow(image_hsv[:,:,0])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:,:,1])
plt.colorbar()

plt.figure()
plt.imshow(image_hsv[:,:,2])
plt.colorbar()

h_min,h_max=(230/255,250/255)
s_min,s_max=(100/255,230/255)
v_min,v_max=(50/255,170/255)

h,w,c=image_hsv.shape
segmentation_mask=np.zeros((h,w))

for i in range(h):#evitamos los bordes
    for j in range(w): #evitamos los bordes
        h_val,s_val,v_val=image_hsv[i,j,:]

plt.imshow(segmentation_mask,vmin=0,vmax=1) 
eroded_mask=np.zeros(segmentation_mask.shape) # creamos otra imagen con la misma forma que la mascara de seg.

# erosionar la mascara 
for i in range(1,h-1):#evitamos los bordes
    for j in range(1,w-1): #evitamos los bordes
        pass

plt.imshow(eroded_mask,vmin=0,vmax=1)  

oordinate_sum=np.array([0,0])
count=0
for i in range(h):
    for j in range(w):
        # IMPLEMENTAR
        # Si el pixel (i,j) pertenece al guante, sumar dicha coordenada a la suma total
        pass

green_glove_position=np.array([0,0]) # IMPLEMENTAR
print("Las coordenadas del centro son:")
print(green_glove_position)

def erode(segmentation_mask):
    #IMPLEMENTAR
    return 0 # retornar mascara de segmentacion erosionada

def segment_by_color(image_hsv,h_min,h_max,s_min,s_max,v_min,v_max):
    #IMPLEMENTAR
    return 0 # retornar mascara de segmentacion

def calculate_mass_center(segmentation_mask):
    #IMPLEMENTAR
    return np.array([0,0]) #retornar posicion

def locate_object(image_rgb,h_min,h_max,s_min,s_max,v_min,v_max):

    return np.array([0,0]) # retornar posición

h_min,h_max=(0/255, 0/255)
s_min,s_max=(0/255, 0/255)
v_min,v_max=(0/255, 0/255)


blue_glove_position=locate_object(image,h_min,h_max,s_min,s_max,v_min,v_max)
print(blue_glove_position) # debería imprimir algo similar a [1150,580]
plt.imshow(image)
