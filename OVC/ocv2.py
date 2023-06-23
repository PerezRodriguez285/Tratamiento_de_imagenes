import cv2
import numpy as np

bgr = np.zeros((300,500,3),np.uint8)   #(filas, col, planos)crear una matriz
bgr[:,:,:]=(255,0,0)
cv2.imshow("BGR", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()


bgr = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png")
cv2.imshow("Color BGR", bgr)
cv2.waitKey()

cB = bgr[:,:,0]   #B
cG = bgr[:,:,1]   #G
cR = bgr[:,:,2]   #R

cv2.imshow("Color BGR", np.hstack([cB, cG, cR]) )
cv2.waitKey()
#cv2.destroyAllWindows()
print("Azul", cB.shape)

rgb = cv2.cvtColor( bgr, cv2.COLOR_BGR2RGB )
cR = rgb[:,:,0]   #R
cG = rgb[:,:,1]   #G
cB = rgb[:,:,2]   #B
cv2.imshow("Color RGB", np.hstack([cR, cG, cB]) )
cv2.waitKey()
cv2.destroyAllWindows()

gris = cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
cv2.imshow("Color Gris", gris)
cv2.waitKey()
cv2.destroyAllWindows()

rojo = np.zeros(bgr.shape, np.uint8 );
rojo[:,:,2] = bgr[:,:,2]
verde = np.zeros(bgr.shape, np.uint8 );
verde[:,:,1] = bgr[:,:,1]
azul = np.zeros(bgr.shape, np.uint8 );
azul[:,:,0] = bgr[:,:,0]

cv2.imshow("Planos color", np.hstack([rojo, verde, azul]))
cv2.waitKey()
print("ROJO", rojo.shape)

rojo2 = np.zeros(rgb.shape, np.uint8 );
rojo2[:,:,2] = rgb[:,:,0]
verde2 = np.zeros(rgb.shape, np.uint8 );
verde2[:,:,1] = rgb[:,:,1]
azul2 = np.zeros(rgb.shape, np.uint8 );
azul2[:,:,0] = rgb[:,:,2]

cv2.imshow("Planos color2", np.hstack([rojo2,verde2,azul2]))
cv2.waitKey()
print("Azul2", azul2.shape)
cv2.destroyAllWindows()
