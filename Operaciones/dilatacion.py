# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:16:48 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
@author: MI PC
"""
import cv2
from PIL import Image
import time
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.draw import disk
from skimage.morphology import (erosion, dilation, closing, opening,
                                area_closing, area_opening)
from skimage.color import rgb2gray

element = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]])
plt.imshow(element, cmap='gray')
circle_image = np.zeros((25, 40))
circle_image[disk((12, 12), 8)] = 1
circle_image[disk((12, 28), 8)] = 1
for x in range(20):
   circle_image[np.random.randint(25), np.random.randint(40)] = 1
imshow(circle_image);
fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].set_title(‘Eroded Image’)
ax[1].imshow(dilation(circle_image, element), cmap=’gray’)
ax[1].set_title(‘Dilated Image’)

def multi_dil(im, num, element=element):
    for i in range(num):
        im = dilation(im, element)
    return im
def multi_ero(im, num, element=element):
    for i in range(num):
        im = erosion(im, element)
    return im

fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].imshow(multi_ero(circle_image, 2, element), cmap='gray')
ax[0].set_title('Imagen dilatada')
ax[1].imshow(multi_dil(circle_image, 2, element), cmap='gray')
ax[1].set_title('Imagen erosionada')

fig, ax = plt.subplots(1,2, figsize=(15,5))
ax[0].imshow(opening(circle_image, element), cmap=’gray’);
ax[0].set_title(‘Opened Image’)
ax[1].imshow(closing(circle_image, element), cmap=’gray’)
ax[1].set_title(‘Closed Image’)

leaves = imread('leaves.jpg')
fig, ax = plt.subplots(1,2, figsize=(12,6))
ax[0].imshow(leaves);
ax[0].set_title('Original Image')
binary = rgb2gray(leaves)<0.15
ax[1].imshow(binary)
ax[1].set_title('Binarized Image')

multi_eroded = multi_ero(binary, 2, element)
imshow(multi_eroded)
