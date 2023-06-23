# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:20:48 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import cv2

image = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/recorte1.png")

total_pixeles = image.size

print("Numero de pixeles: ",total_pixeles)