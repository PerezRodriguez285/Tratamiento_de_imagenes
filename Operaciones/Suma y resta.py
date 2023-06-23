"""
Created on Fri Mar  5 10:13:37 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
           Luis Angel Diaz Navas
           Miguel Angel Flores Urbina
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import numpy as np
import cv2
from random import randint, uniform,random

def Color(Img):
    Img = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    return Img
def Margen(pixel, alto, ancho, a):
    for i in range(alto):
        for t in range(ancho):
            for j in range(30):
                pixel.itemset((i, j, 0), a)
                pixel.itemset((i, j, 1), a)
                pixel.itemset((i, j, 2), a)
                pixel.itemset((j, t, 0), a)
                pixel.itemset((j, t, 1), a)
                pixel.itemset((j, t, 2), a) 
    for i in range(alto):
        for t in range(ancho):
            for j in range(alto-40, alto):
                pixel.itemset((j, t, 0), a)
                pixel.itemset((j, t, 1), a)
                pixel.itemset((j, t, 2), a)
                for k in range(ancho-30, ancho):
                    pixel.itemset((i, k, 0), a)
                    pixel.itemset((i, k, 1), a)
                    pixel.itemset((i, k, 2), a)
    return pixel
def Suma(img1, img2):
    print(img1.shape)
    print(img2.shape)
    sumando = cv2.add(img1, img2)
    return sumando
def Imprimir(Img, titulo):
    cv2.imshow(titulo, Img)
    cv2.waitKey(0)
def Resta(im1, im2):
    print(im1.shape)
    print(im2.shape)
    restando = cv2.subtract(im2,im1)
    return restando
nombre= input("Ingresa el nombre de la imagen: ")
img = cv2.imread(nombre)
alto, ancho = img.shape[0:2]
imgC = Color(img)
color1 = np.zeros((alto, ancho,3))
color1 = Margen(color1, alto, ancho, 255)
color2 = np.ones((alto, ancho, 3))
color2 = Margen(color2, alto, ancho, 0)
Imprimir(color1, "color 1")
Imprimir(color2, "color 2")
cv2.imwrite("color1.jpg",color1)
cv2.imwrite("color2.jpg",color2)
color1 = cv2.imread("color1.jpg")
color2 = cv2.imread("color2.jpg")
color1 = Color(color1)
color2 = Color(color2)
s = Suma(color1, imgC)
s2 = Suma(color2, imgC)
r =  Resta(color1, imgC)
r2 = Resta(color2, imgC)
Imprimir(s, "sumando color 1")
Imprimir(s2, "sumando color 2")
Imprimir(r, "restando color 1")
Imprimir(r2, "restando color 2")
cv2.destroyAllWindows()
