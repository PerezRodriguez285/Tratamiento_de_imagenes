# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:36:36 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Proyecto final primera parte
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
Descripción: Tratamiento de imagenes aplicando todo lo aprendido durante el semestre
"""
from PIL import Image
from matplotlib import pyplot as plt
from collections import Counter
from scipy import ndimage as ndi
from skimage import feature
import scipy.misc
import numpy as np
import statistics
import random
import scipy
import time
import cv2


def abrir_imagen(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
    
def escala_de_grises(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i, j), pixel)
            j+=1
        i+=1
    im2.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
    
def negativo_color(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im5 = im
    i = 0
    while i < im5.size[0]:
        j = 0
        while j < im5.size[1]:
            r, g, b = im5.getpixel((i, j))
            rn = 255 - r
            gn = 255 - g
            bn = 255 - b
            pixel = tuple([rn, gn, bn])
            im5.putpixel((i, j), pixel)
            j+=1
        i+=1
    im5.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')

def negativo_grises(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im15 = im
    i = 0
    while i < im15.size[0]:
        j = 0
        while j < im15.size[1]:
            gris = im15.getpixel((i,j))
            valor = 255 - gris
            im15.putpixel((i, j), valor)
            j+=1
        i+=1
    im15.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')

def blanco_negro(im,grisBase):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im6 = im
    i = 0
    while i < im6.size[0]:
        j = 0
        while j < im6.size[1]:
            r, g, b = im6.getpixel((i, j))
            gris = (r + g + b) / 3
            if gris < grisBase:
                im6.putpixel((i, j), (0, 0, 0))
            else:
                im6.putpixel((i, j), (255, 255, 255))   
            j+=1
        i+=1
    im6.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')    

def histograma_grises(im):
    img =cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/cameraman.png",0)
    intensidades = []
    for i in range(255):
        intensidades.append(0)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            intensidades[img.item(i,j)]=intensidades[img.item(i,j)]+1

    intensidades = np.asarray(intensidades)
    plt.plot(intensidades)
    plt.show()
    
def brillo(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im9 = im
    arreglo = np.array(im9.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im9.size[0]:
        j = 0
        while j < im9.size[1]:
            suma = suma + im9.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total    
    print("El brillo de la imagen es", brillo)  
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
    
def contraste(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    im10 = im
    arreglo = np.array(im10.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            suma = suma + im10.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total
    i = 0 
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            aux = im10.getpixel((i,j)) - brillo 
            suma = suma + aux
            j+=1
        i+=1
    cont = suma * suma
    cont = np.sqrt(suma / total)
    contraste = int(cont)
    print("El contraste de la imagen es", contraste) 
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
    
def ecua_uniforme(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    [ren, col] = ima.size 
    ima = np.asarray(ima, dtype = np.float32).reshape(1, ren * col)
    valor = 0 
    maxdata = max(max(ima))
    mindata = min(min(ima))
    niveles = maxdata
    h = np.zeros(niveles)
    ima = ima.reshape(col, ren)
    ac = h
    i = 0
    #cálculo del histograma
    while i < ren:
        j = 0
        while j<col:
            valor = ima[j, i] - 1
            h[valor] = h[valor] + 1
            j+=1
        i+=1
    ac[0] = h[0]
    i = 1
    while i < maxdata:
        ac[i] = ac[i - 1] + h[i]
        i+=1
    ac = ac / (ren * col)
    #funcion de mapeo 
    m1 = maxdata - mindata
    m2 = m1 * ac
    m3 = m2 + mindata
    mapeo = np.floor(m3)
    #si mindata es cero la imagen sera cero
    newim = np.zeros((col, ren))
    i = 0
    while i < ren:
        j = 0
        while j < col:
            newim[j, i] = mapeo[ima[j, i] - 1]
            j+=1
        i+=1
    newim = Image.fromarray(newim)
    newim.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')

def salypimienta_grises(im,prob):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    [ren, col] = im.size
    sal = im
    nMaxRen = round(ren * prob / 100.0)
    nMaxCol = round(col * prob / 100.0)
    i = 1
    for i in range(nMaxRen):
        j = 1
        for j in range(nMaxCol):
            cx = round(np.random.rand() * (col - 1)) + 1
            cy = round(np.random.rand() * (ren - 1)) + 1
            aaa = round(np.random.rand() * 255)
        if aaa > 128:
            val = 255
            sal.putpixel((cy, cx),(val))
        else:
            val= 1
            sal.putpixel((cy, cx),(val))
    sal.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')

def bordes_sobel(im, mask):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    [ren, col] = ima.size
    pix = ima.load()
    out_im = Image.new("L", (ren, col))
#   gx + gy + prewit45° = ([1,3,3],[-3,-2,3],[-3,-3,1])
#   gx = ([-1,0,1], [-2,0,2], [-1,0,1])
#   gy = ([1,2,1], [0,0,0], [-1,-2,-1])   
    out = out_im.load()
    for i in range(ren):
        for j in range(col):
            suma = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and m >= 0 and n < ren and m < col:
                        suma += mask[n - (i - 1)][ m - (j - 1)] * pix[n, m]
            out[i, j] = suma
    out_im.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')
    
def bordes_canny(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    ima = ndi.gaussian_filter(im, 4)
    edges = feature.canny(ima)
    fig, (ax2) = plt.subplots(nrows = 1, ncols = 1, figsize = (8, 3), sharex = True, sharey = True)
    ax2.imshow(edges, cmap = plt.cm.gray)
    ax2.axis('off')
    plt.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')

def umbral_otsu(im):
    tiempoIn = time.time()
    ruta = ("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + im)
    im = Image.open(ruta)
    im.show()
    ima = im
    width, height = ima.size
    img = np.array(ima.getdata())
    histogram = np.array(ima.histogram(),float) / (width * height)
    #Vector de probabilidad acomulada.
    omega = np.zeros(256)
    #Vector de media acomulada
    mean = np.zeros(256)
    #Partiendo del histograma normalizado se calculan la probabilidad
    #acomulada (omega) y la media acomulada (mean)
    omega[0] = histogram[0]
    for i in range(len(histogram)):
        omega[i] = omega[i - 1] + histogram[i]
        mean[i] = mean[i - 1] + (i - 1) * histogram[i]
    sigmaB2 = 0
    mt = mean[len(histogram) - 1] #El Valor de la intensidad media de la imagen
    sigmaB2max = 0
    T = 0
    for i in range(len(histogram)):
        clase1 = omega[i]
        clase2 = 1 - clase1
        if clase1 != 0 and clase2 != 0:
            m1 = mean[i] / clase1
            m2 = (mt - mean[i]) / clase2
            sigmaB2 = (clase1 * (m1 - mt) * (m1 - mt) + clase2 * (m2 - mt) * (m2 - mt))
            if sigmaB2 > sigmaB2max:
                sigmaB2max = sigmaB2
                T = i
    thr = int(T)
    print('El Umbral Optimo De La Imagen Es: ' ,thr)
    #Se Aplica la umbralización al "array" de la imagen
    #limites de procesado en x
    x_min, x_max = 0, width
    #limites de procesado en y
    y_min, y_max = 0, height
    #imagen de salida
    img_out = np.zeros(width * height)
    #procesado de la imagen
    loc = 0 #posicin del "pixel" actual
    for y in range (y_min, y_max):
        for x in range(x_min, x_max):
            loc = y * width + x
            if img[loc] > thr:
                img_out[loc] = 255
            else:
                img_out[loc] = 0
    img_thr = img_out
    im_otsu = img_thr.reshape(height, width)
    im_otsu = Image.fromarray(im_otsu)
    im_otsu.show()
    tiempoFin = time.time()
    print('El Proceso Tardo: ', tiempoFin - tiempoIn, ' Segundos')


