# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:17:08 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

import numpy as np

def umbral_adaptativo(input_img):

    h, w = input_img.shape

    S = w/8
    s2 = S/2
    T = 15.0

    #integral img
    int_img = np.zeros_like(input_img, dtype=np.uint32)
    for col in range(w):
        for row in range(h):
            int_img[row,col] = input_img[0:row,0:col].sum()

    #output img
    out_img = np.zeros_like(input_img)    

    for col in range(w):
        for row in range(h):
            #SxS region
            y0 = max(row-s2, 0)
            y1 = min(row+s2, h-1)
            x0 = max(col-s2, 0)
            x1 = min(col+s2, w-1)

            count = (y1-y0)*(x1-x0)

            sum_ = int_img[y1, x1]-int_img[y0, x1]-int_img[y1, x0]+int_img[y0, x0]

            if input_img[row, col]*count < sum_*(100.-T)/100.:
                out_img[row,col] = 0
            else:
                out_img[row,col] = 255

    return out_img
