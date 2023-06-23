# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:04:19 2021

@author: MI PC
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/lc3.tiff')

color = ('b','g','r')

plt.figure(1)
plt.subplot(121)
plt.title("Histograma")
for i, col in enumerate(color):
    histr = cv2.calcHist([img1], [i], None, [256], [0,256])   
    plt.plot(histr, color = col)
    plt.xlim([0,256])

plt.subplot(122)
plt.title("Imagen")
plt.imshow( cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) )
plt.show()

 
hist,bins = np.histogram(img1.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img1.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histograma'), loc = 'upper right')
plt.show()

cdf_m = np.ma.masked_equal(cdf,0) 
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img1]
cv2.imshow('image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
