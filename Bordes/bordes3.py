# -*- coding: utf-8 -*-
"""
Created on Fri May 28 18:56:44 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Bordes con OpenCV
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
Descripción: 
"""
import numpy as np
import cv2


def sobel(img, threshold):
  
    G_x = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    G_y = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])
    rows = np.size(img, 0)
    columns = np.size(img, 1)
    mag = np.zeros(img.shape)
    for i in range(0, rows - 2):
        for j in range(0, columns - 2):
            v = sum(sum(G_x * img[i:i+3, j:j+3]))  # vertical
            h = sum(sum(G_y * img[i:i+3, j:j+3]))  # horizon
            mag[i+1, j+1] = np.sqrt((v ** 2) + (h ** 2))
            
    for p in range(0, rows):
        for q in range(0, columns):
            if mag[p, q] < threshold:
                mag[p, q] = 0
    return mag

img = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/imagen2.jpg', 0)  # read an image
mag = sobel(img, 70)

def img_show(img):  
    cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def sub_plot(img_1, img_2):
    l = np.size(img, 1)/4  # a quarter of the columns
    rows = np.size(img, 0) 
    interval = np.ones((rows, int(l)))
    interval = interval * 255
    
    img_o = np.concatenate((img_1, interval, img_2), axis=1)
    return img_o
