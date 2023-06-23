import cv2
import numpy as np
import matplotlib.pyplot as plt


def dilatacionBinaria(img, ee):
    imgS = np.zeros(img.shape, dtype=np.uint8)
    x, y = img.shape
    xEE, yEE = ee.shape[0]//2, ee.shape[1]//2                 #Tamaño del EE
    print("\nX, Y", xEE, " ", yEE)
    for f in range(x):
        for c in range(y):
            if( img[f,c] == 255):
                imgS[f-xEE:f+xEE+1, c-yEE:c+yEE+1] = 255
    return imgS

def dilatacion(imgSinBorde, ee):
    x, y = imgSinBorde.shape
    xEE, yEE = ee.shape[0]//2, ee.shape[1]//2                 #Tamaño del EE 7*/
    imgS = np.zeros((x,y), dtype=np.uint8)                      #imagen de salida
    img = np.zeros((x+(2*xEE), y+(2*yEE)), dtype=np.uint8)             #Imagen de entrada con un borde
    img[xEE:-xEE,yEE:-yEE] = imgSinBorde[:,:]   #coordenada anterior 2x2 con las siguientes coordenadas

    for f in range(xEE,x+1):
        for c in range(yEE,y+1):
            maximo = np.amax( img[f-xEE:f+xEE+1, c-yEE:c+yEE+1] )
            #print("\n", f, " ", c)
            #print("\n",f-xEE, ":", f+xEE+1, " ", c-yEE, ":", c+yEE+1)
            #print("\n", img[f-xEE:f+xEE+1,c-yEE:c+yEE+1])
            #print("\nM: ", maximo )
            imgS[f-xEE,c-yEE] = maximo
            #imgS[f-xEE:f+xEE+1, c-yEE:c+yEE+1] = maximo
            # print("\n", imgS[f-1:f+2,c-1:c+2])
    return imgS

im1 = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/chicago.bmp', 0)
#im1 = cv2.bitwise_not(im1)

ee = np.ones( (5,5), np.uint8 )

#imS = dilatacionBinaria(im1, ee)
imS = dilatacion(im1, ee)
imDilatacion = cv2.dilate(im1, ee)
diferencia = imS - imDilatacion

# print("Or:\n", im1)
# print("S:\n", imS)
cv2.imshow("Original - Salida - diferencia",  np.hstack((im1, imS, imDilatacion, diferencia)))
cv2.waitKey()
cv2.destroyAllWindows()
