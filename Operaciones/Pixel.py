# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:51:21 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar funciones OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import Image
import numpy as np
 
color_nuevo = (0,172,193)
color_actual = (33,150,243)
 
icono = Image.open('C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png')
icono = Image.convert("RGBA")
 
data = np.array(icono)
data[(data == color_actual).all(axis = -1)] = color_nuevo
 
icono_nuevo = Image.fromarray(data, 'RGBA')
icono_nuevo.save('nuevo_icono.png')