# -*- coding: utf-8 -*-
"""
Created on Sun May 30 11:11:59 2021


Alumno: Antonio Alberto de la Luz Perez Rodriguez
"""

import cv2
from math import *
import numpy as np
import time,math
import os
import re

'' 'Girar la imagen y recortarla' ''
def rotate(img, pt1, pt2, pt3, pt4):
    withRect = math.sqrt((pt4[0] - pt1[0]) ** 2 + (pt4[1] - pt1[1]) ** 2)  # El ancho del rectángulo
    heightRect = math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) **2)
    angle = acos((pt4[0] - pt1[0]) / withRect) * (180 / math.pi)  

    if pt4[1]>pt1[1]:
        print ("rotación en el sentido de las agujas del reloj")
    else:
        print ("Rotación en sentido antihorario")
        angle=-angle

    height = img.shape[0]  # Altura de la imagen original
    width = img.shape[1]   # Ancho de la imagen original
    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)  # Girar la imagen en ángulo
    heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
    widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))

    rotateMat[0, 2] += (widthNew - width) / 2
    rotateMat[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, rotateMat, (widthNew, heightNew), borderValue=(255, 255, 255))
    cv2.imshow('rotateImg2',  imgRotation)
    cv2.waitKey(0)

    # Las coordenadas de cuatro puntos de la imagen rotada
    [[pt1[0]], [pt1[1]]] = np.dot(rotateMat, np.array([[pt1[0]], [pt1[1]], [1]]))
    [[pt3[0]], [pt3[1]]] = np.dot(rotateMat, np.array([[pt3[0]], [pt3[1]], [1]]))
    [[pt2[0]], [pt2[1]]] = np.dot(rotateMat, np.array([[pt2[0]], [pt2[1]], [1]]))
    [[pt4[0]], [pt4[1]]] = np.dot(rotateMat, np.array([[pt4[0]], [pt4[1]], [1]]))

    # Manejo del caso de reversión
    if pt2[1]>pt4[1]:
        pt2[1],pt4[1]=pt4[1],pt2[1]
    if pt1[0]>pt3[0]:
        pt1[0],pt3[0]=pt3[0],pt1[0]

    imgOut = imgRotation[int(pt2[1]):int(pt4[1]), int(pt1[0]):int(pt3[0])]
    cv2.imshow("imgOut", imgOut)  # Recorta el rectángulo girado
    cv2.waitKey(0)
    return imgRotation  # rotated image


 # Dibuja el rectángulo original basado en cuatro puntos
def drawRect(img,pt1,pt2,pt3,pt4,color,lineWidth):
    cv2.line(img, pt1, pt2, color, lineWidth)
    cv2.line(img, pt2, pt3, color, lineWidth)
    cv2.line(img, pt3, pt4, color, lineWidth)
    cv2.line(img, pt1, pt4, color, lineWidth)



if __name__=="__main__":
    directory = "C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/"
    last = 'cneg.txt'
    imageName="paisaje2.jpg"