import numpy as np
import matplotlib.pyplot as plt
import cv2


image = cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/DSC_04022.jpg') 
ret1, thresh1 = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
ret5, thresh5 = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh1', thresh1)

cv2.waitKey()