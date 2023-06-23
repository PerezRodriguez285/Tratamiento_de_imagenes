# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:48:03 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Histograma en una imagem a color
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

#import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Dragon_Shiryuu.png")
cv2.imshow('Imagen Original',img)
imagen1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
color = ('b','g','r')

def histograma(img):
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    
def DibujarRangoColor(img,por,inf,sup):
    for i in range(0,len(img)):
        for j in range (0,len(img)[0]):
            if(img[i][j][pos]<inf or img[i][j][pos]>sup):
                img[i][j][0]=255
                img[i][j][1]=255
                img[i][j][2]=255

histograma(imagen1)
DibujarRangoColor(img,0,200,255)
cv2.imshow('histograma',img)
cv2.waitkey(0)

