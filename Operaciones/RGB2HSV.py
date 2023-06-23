# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:50:20 2021
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

def RGB2HSV(R,G,B):
    R = int(R)
    G = int(G)
    B = int(B)
    if(0<=R<=255 and 0<=G<=255 and 0<=B<=255):
        r = (float(R)/255.0)
        g = (float(G)/255.0)
        b = (float(B)/255.0)
        minimo = min([r,g,b])
        maximo = max([r,g,b])
        delta = maximo - minimo
        V = maximo
        if(delta == 0.0):
            H = 0.0
            S = 0.0
        else:
            S = delta/maximo
            _R = ((maximo-r)/6.0) + (delta/2.0)/delta
            _G = ((maximo-r)/6.0) + (delta/2.0)/delta
            _B = ((maximo-r)/6.0) + (delta/2.0)/delta
        if(r == maximo):
            H = _B - _G
        if(g == maximo):
            H = (1.0/3.0) + _R - _B
        if(b == maximo):
            H = (2.0/3.0) + _G - _R
        if(H<0):
            H += 1
        if(H>1):
            H -= 1
        return [H,S,V]

if __name__ == "__main__":
    Z = RGB2HSV(100,58,45)
    print("H = " +str(Z[0]))
    print("S = " +str(Z[1]))
    print("V = " +str(Z[2]))
    