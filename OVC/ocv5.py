import cv2
import numpy as np
import matplotlib.pyplot as plt

imBGR = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg')
print(imBGR.shape)

color = ('b','g','r')

plt.figure(1)
plt.subplot(121)
plt.title("Histograma")
for i, col in enumerate(color):
    histr = cv2.calcHist([imBGR], [i], None, [256], [0,256])   
    plt.plot(histr, color = col)
    plt.xlim([0,256])

plt.subplot(122)
plt.title("Imagen")
plt.imshow( cv2.cvtColor(imBGR, cv2.COLOR_BGR2RGB) )
plt.show()

pR = imBGR[:,:,2]
pG = imBGR[:,:,1]
pB = imBGR[:,:,0]
cv2.imshow("Plano RGB", np.hstack([pR,pG,pB]))
cv2.waitKey()
cv2.destroyAllWindows()
