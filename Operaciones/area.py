# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 21:42:37 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
from PIL import Image

imgFile = input("Nombre de la imagen: ")
img = Image.open(imgFile);
pixels = img.getdata()
total = len(list(filter(lambda i: i >= (200,200,200), pixels)))
print("Total de pixeles de la imagen", total)
