import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Dragon_Shiryuu.png',0)   #0 porque es en niveles de gris

cv2.imshow("Chicago", imagen)
print( imagen.shape )
cv2.waitKey()

#OPENCV   40x
hist = cv2.calcHist([imagen],[0], None, [256], [0,256])
#cv2.calcHist( imagen, canales, mask, tamHist, rangos[] )
#canales: [0] gris - [0],[1],[2] color
#mask: "None histograma de toda la imagen, o mask para una región
#tamHist: Nivel [256]
#rango: [0,256]

print("Hist: ", hist.shape)
#print(hist)

plt.figure(1)
plt.subplot(221)
plt.plot( hist)
plt.title("Histograma OpenCV (calcHist)")

plt.subplot(222)
plt.hist(imagen.ravel(), 256, [0,256])
plt.title("Histograma Matplotlib (hist)")
#plt.show()

histNP, bins = np.histogram(imagen.ravel(), 256, [0,256])  #1x
plt.subplot(223)
plt.plot(histNP)
plt.title("Histograma Numpy (histogram)")

histNP2 = np.bincount(imagen.ravel(), minlength=256)    #10x
plt.subplot(224)
plt.plot(histNP2)
plt.title("Histograma Numpy (bincount)")
plt.show()


cv2.destroyAllWindows()
