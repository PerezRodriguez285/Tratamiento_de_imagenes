import cv2
import numpy as np
import matplotlib.pyplot as plt


im = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/fig1b.jpg',0)
#im = cv2.imread('../Imagenes/rice.png',0)
im = cv2.bitwise_not(im)                    #Negativo

ee = np.ones( (3,3), np.uint8 )         # Elemento de estructura 7x7 cuadrado
#print(ee)
erosion = cv2.erode( im, ee )
dilatacion = cv2.dilate(im, ee)

cv2.imshow("Original - Erosion - Dilatacion - 3x3 Cuadrado", np.hstack((im, erosion, dilatacion)))
cv2.waitKey()

#Elementos específicos
ee = cv2.getStructuringElement( cv2.MORPH_RECT, (7,7) );
erosion = cv2.erode( im, ee )
dilatacion = cv2.dilate(im, ee)
cv2.imshow("Original - Erosion - Dilatacion - 5x5 Cuadrado", np.hstack((im, erosion, dilatacion)))
cv2.waitKey()

ee = cv2.getStructuringElement( cv2.MORPH_CROSS, (7,7) );
print("Cruz\n", ee)
erosion = cv2.erode( im, ee )
dilatacion = cv2.dilate(im, ee)
cv2.imshow("Original - Erosion - Dilatacion - 7x7 Cruz", np.hstack((im, erosion, dilatacion)))
cv2.waitKey()

ee = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (7,7) );
print("Circulo\n", ee)
erosion = cv2.erode( im, ee )
dilatacion = cv2.dilate(im, ee)
cv2.imshow("Original - Erosion - Dilatacion - 7x7 Elipse", np.hstack((im, erosion, dilatacion)))
cv2.waitKey()
cv2.destroyAllWindows()
