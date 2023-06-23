# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:21:25 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""

def RGB2CMYK (R,G,B):
    if(float(int(R)) == float(R) and float(int(G)) == float(G) and float(int(B)) == float(B)):
        if(0<=int(R) <=255 and 0<=int(G)<=255 and 0<=int(B)<=255):
            r = float(R)/255
            g = float(G)/255
            b = float(B)/255
            white = max(r,g,b)
            C=(white-r)/white
            M=(white-g)/white
            Y=(white-b)/white
            K=(1-white)
            print("\n==========\n")
            print("C = " +str(C))
            print("M = " +str(M))
            print("Y = " +str(Y))
            print("K = " +str(K))
            print("\n===========\n")

if __name__ == "__main__":
    RGB2CMYK(100,98,254) #depende de los valores rgb que se desean colocar