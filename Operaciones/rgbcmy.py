# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:53:05 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import cv2

def RGBCMY(R,G,B):
    if(R>=0 and G>=0 and B>=0):
        if(R<=255 and G<=255 and B<=255):
            C = 1.0 - (R/255.0)
            M = 1.0 - (G/255.0)
            Y = 1.0 - (B/255.0)
            print("C = " +str(C))
            print("M = " +str(M))
            print("Y = " +str(Y))

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


image = cv2.imread("C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png")
cv2.imshow("Imagen cmy", image)
cv2.waitKey()

if __name__ == "__main__":
    print("Conversion de RGB2CMY")
    RGBCMY(215,125,125) #depende de los valores rgb que se desean colocar
    print("\n===========\n")
    print("Conversion de RGB2HSV")
    Z = RGB2HSV(100,58,45)
    print("H = " +str(Z[0]))
    print("S = " +str(Z[1]))
    print("V = " +str(Z[2]))
    print("\n===========\n")
    
    
    