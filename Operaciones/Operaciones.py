# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:33:17 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import cv2
#import numpy as np
#import matplotlib.pyplot as plt
  
"""Suma de imagenes"""
def suma():
    img1 = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/peppers.tiff")
    img2 = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/mandrill-baboon.tiff")
    suma = cv2.add(img1,img2)
    cv2.imshow('suma',suma)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""Resta de imagenes"""
def resta():
    img3 = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/peppers.tiff")
    img4 = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/mandrill-baboon.tiff")
    resta = cv2.subtract(img3,img4)
    cv2.imshow('resta',resta)
    cv2.waitKey(0)
    cv2.destroyAllWindows()