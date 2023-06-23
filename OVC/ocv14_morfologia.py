import cv2
import numpy as np
import matplotlib.pyplot as plt


im = cv2.imread('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg',0)
#im = cv2.imread('../Imagenes/rice.png',0)
im = cv2.bitwise_not(im)                    #Negativo


ee = cv2.getStructuringElement( cv2.MORPH_RECT, (5,5) );

apertura = cv2.morphologyEx( im, cv2.MORPH_OPEN, ee )
clausura = cv2.morphologyEx(im, cv2.MORPH_CLOSE, ee)
cv2.imshow("Original - Apertura - Clausura", np.hstack((im, apertura, clausura)))
cv2.waitKey()


erosion = cv2.erode( im, ee )
dilatacion = cv2.dilate(im, ee)
gradiente = dilatacion - erosion
gradiente2 = cv2.morphologyEx(im, cv2.MORPH_GRADIENT, ee)
cv2.imshow("Erosion - Dilatacion - Gradiente", np.hstack((erosion, dilatacion, gradiente, gradiente2)))
cv2.waitKey()


tophat = cv2.morphologyEx( im,cv2.MORPH_TOPHAT, ee )
blackhat = cv2.morphologyEx(im, cv2.MORPH_BLACKHAT, ee)
cv2.imshow("Original - Top Hat - Black Hat - 7x7 Elipse", np.hstack((im, tophat, blackhat)))
cv2.waitKey()

hitmiss = cv2.morphologyEx( im, cv2.MORPH_HITMISS, ee )
cv2.imshow("Original - HIT & MISS", np.hstack((im, hitmiss)))
cv2.waitKey()
cv2.destroyAllWindows()
