# -*- coding: utf-8 -*-
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

from PIL import Image
 
img = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Resultados/grises.gif")
datos = img.getdata()
datos_invertidos = [255 - x for x in datos]
imagen_invertida = Image.new('L', img.size)
imagen_invertida.putdata(datos_invertidos)
imagen_invertida.save("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Resultados/negativo.gif")
imagen_invertida.close()
img.close()

