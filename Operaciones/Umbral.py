# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:38:14 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar funciones OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""


    
import cv2
import numpy as np
import matplotlib.pyplot as plt
    
imBGR = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg') 
def build_sample_image():
    tones = np.arange(start=50, stop=300, step=50)
    result = np.zeros((50, 50, 3), dtype="uint8")
    for tone in tones:
        img = np.ones((50, 50, 3), dtype="uint8") * tone
        result = np.concatenate((result, img), axis=1)
    return result




ret1, thresh1 = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY)