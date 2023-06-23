# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:46:09 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Histograma
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

def hsb2rgb(hsb): 
    H = float(hsb[0]/360.0) 
    S = float(hsb[1]/100.0) 
    B = float(hsb[2]/100.0) 

    if (S == 0): 
        R = int(round(B * 255)) 
        G = int(round(B * 255)) 
        B = int(round(B * 255)) 
    else: 
        var_h = H * 6 
    if (var_h == 6): 
         var_h = 0 # H must be < 1 
         var_i = int(var_h) 
         var_1 = B * (1 - S) 
         var_2 = B * (1 - S * (var_h - var_i)) 
         var_3 = B * (1 - S * (1 - (var_h - var_i))) 
    if  (var_i == 0): 
        var_r = B  ; var_g = var_3 ; var_b = var_1 
    elif (var_i == 1): 
        var_r = var_2 ; var_g = B  ; var_b = var_1 
    elif (var_i == 2): 
        var_r = var_1 ; var_g = B  ; var_b = var_3 
    elif (var_i == 3): 
        var_r = var_1 ; var_g = var_2 ; var_b = B 
    elif (var_i == 4): 
        var_r = var_3 ; var_g = var_1 ; var_b = B 
    else: 
        var_r = B  ; var_g = var_1 ; var_b = var_2 

    R = int(round(var_r * 255)) 
    G = int(round(var_g * 255)) 
    B = int(round(var_b * 255)) 

    return [R, G, B] 

