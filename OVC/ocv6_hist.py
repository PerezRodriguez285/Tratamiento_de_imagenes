import cv2
import numpy as np
import matplotlib.pyplot as plt

def histGris( im ):
    h = np.zeros([256]);
    for f in im:
        for c in f:
            h[c] += 1
    return h

def hist2Gris( im ):
    h = np.zeros([256]);
    img = np.reshape(im, -1)
    for p in img:
        h[p] += 1
    return h



imagen = cv2.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg",0)
plt.figure(1)
plt.subplot(311)
histr = cv2.calcHist([imagen], [0], None, [256], [0,256])
plt.plot(histr, color = 'b')
plt.xlim([0,256])


print("Imagen 1: ", imagen.shape)
hist = histGris( imagen )
#print( "Histograma:\n", hist)
plt.subplot(312)
plt.plot(hist, color = 'r')


print("Imagen 2: ", imagen.shape)
hist2 = hist2Gris( imagen )
#print( "Histograma2:\n", hist2)
plt.subplot(313)
plt.plot(hist2, color = 'g')
plt.show()
