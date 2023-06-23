"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes sin usar funciones OPENCV
Alumnos:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


im = cv2.imread('../Imagenes/fig1b.jpg',0)
#im = cv2.imread('../Imagenes/rice.png',0)
im = cv2.bitwise_not(im)                    #Negativo

ee = cv2.getStructuringElement( cv2.MORPH_RECT, (5,5) );
erosion = cv2.erode( im, ee )
apertura = cv2.dilate(erosion, ee)
TopHat1 = im - apertura
cv2.imshow("Original - Erosion - Apertura - TopHat (Diferencia)", np.hstack((im, erosion, apertura, TopHat1)))
cv2.waitKey()

tophat2 = cv2.morphologyEx( im,cv2.MORPH_TOPHAT, ee )
#blackhat = cv2.morphologyEx(im, cv2.MORPH_BLACKHAT, ee)
cv2.imshow("Original - Top Hat1 - Top Hat  OpenCV", np.hstack((im, TopHat1, tophat2)))
cv2.waitKey()
cv2.destroyAllWindows()
