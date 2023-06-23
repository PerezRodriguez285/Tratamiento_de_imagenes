import cv2
import numpy as np
#import matplotlib.pyplot as plt


def negativo2( img ):
    neg = 255-img
    return neg


def negativo3( img ):
    neg = np.zeros( img.shape , dtype=np.uint8)
    for f in range( img.shape[0] ):
        for c in range( img.shape[1] ) :
            neg[f,c] = 255 - img[f,c];
    return neg


imagen = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg')     #BGR
neg = cv2.bitwise_not(imagen)#manda el negativo de OPENCV
neg2 = negativo2(imagen)
neg3 = negativo3(imagen)


cv2.imshow("Imagen - Negativo 1", np.hstack((imagen, neg)))
cv2.imshow("Imagen - Negativo 2", np.hstack((neg2, neg3)))
cv2.waitKey();
cv2.destroyAllWindows()


#permite saber si los tipos de datos son los correctos
print("\nImg: ", imagen[0]) #una manera de colocarlo es imagen[0:3, 0:2]
print("\nNeg: ", neg[0])
print("\nNeg2: ", neg2[0])
print("\nNeg3: ", neg3[0])
print(type( imagen ))
print(type( neg ))
print(type( neg2 ))
print(type( neg3 ))
