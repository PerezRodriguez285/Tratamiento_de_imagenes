import cv2
import numpy as np
import matplotlib.pyplot as plt


def erosionBinaria(img, ee):
    imgS = np.full(img.shape, 255, dtype=np.uint8)
    x, y = img.shape
    xEE, yEE = ee.shape[0]//2, ee.shape[1]//2                 #Tamaño del EE
    for f in range(x):
        for c in range(y):
            if( img[f,c] == 0):
                imgS[f-xEE:f+xEE+1, c-yEE:c+yEE+1] = 0
    return imgS

def erosion(imgSinBorde, ee):
    x, y = imgSinBorde.shape
    xEE, yEE = ee.shape[0]//2, ee.shape[1]//2                 #Tamaño del EE
    imgS = np.zeros((x,y), dtype=np.uint8)                      #imagen de salida
    img = np.full((x+(2*xEE), y+(2*yEE)), 255, dtype=np.uint8)             #Imagen de entrada con un borde
    img[xEE:-xEE,yEE:-yEE] = imgSinBorde[:,:]

    for f in range(xEE,x+1):
        for c in range(yEE,y+1):
            minimo = np.amin( img[f-xEE:f+xEE+1, c-yEE:c+yEE+1] )
            imgS[f-xEE,c-yEE] = minimo
    return imgS


im1 = cv2.imread('../Imagenes/onerice.bmp', 0)
ee = np.ones( (3,3), np.uint8 )

imB = erosionBinaria(im1, ee)
imS = erosion(im1, ee)
imErosion = cv2.erode(im1, ee)
diferencia = imS - imErosion

# print("Or:\n", im1)
# print("S:\n", imS)
cv2.imshow("Original - Diferencia",  np.hstack((im1, diferencia)))
cv2.imshow("erosionBinaria - Erosion - Erosion OpenCV",  np.hstack((imB, imS, imErosion)))
cv2.waitKey()
cv2.destroyAllWindows()
