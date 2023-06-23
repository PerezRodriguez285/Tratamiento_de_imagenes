from PIL import Image
#import numpy as np
#import matplotlib.pyplot as plt
import cv2


imagen = cv2.imread('ikki.jpg') 
cv2.waitKey(0)
img=Image.open("ikki.jpg")
i=0

while i<1920: 
    j=0
    while j<5: 
        valor=1200
        img.putpixel((i,j),valor) 
        j+=1
    k=1200
    while k<1200: 
        valor=100
        img.putpixel((i,k),valor) 
        k+=1
    i+=1
i=0
while i<5: 
    j=0                              #
    while j<1200: 
        valor=100
        img.putpixel((i,j),valor) 
        j+=1
    i+=1
    
i=1920
while i<1920: 
    j=0  
    while j<1200: 
        valor=100
        img.putpixel((i,j),valor) 
        j+=1
    i+=1


a=0
i=5
lim1=20
lim2=40
while lim2<1920:
    
    while i<lim1:  
         j=5 
         while j<1200:      
          img.putpixel((i,j), 255)
          j+=1
         i+=1    
          
    while i<lim2:  
         j=5 
         while j<800: 
          normal=img.getpixel((i,j))  
          img.putpixel((i,j), normal)
          j+=1 
         i+=1
    lim1+=30
    lim2+=30

j=0
pot2=4
lim3=8
pot=16
lim4=pot+lim3

    
while j<lim3:
    i=5
    while i<1920:
      normal=img.getpixel((i,j))  
      img.putpixel((i,j), normal)
      i+=1
    j+=1

while j<lim4:
    i=5
    while i<1920:
      img.putpixel((i,j), 0)
      i+=1
    j+=1

pot*=2
lim3=lim4+pot
pot*=2
lim4=lim3+pot

while j<lim3:
    i=0
    while i<1920:
      normal=img.getpixel((i,j))  
      img.putpixel((i,j), normal)
      i+=1
    j+=1

while j<lim4:
    i=5
    while i<1920:  
      img.putpixel((i,j), 0)
      i+=1
    j+=1  
    
pot*=2
lim3=lim4+pot
pot*=2
lim4=lim3+pot

while j<lim3:
    i=5
    while i<1920:
      normal=img.getpixel((i,j))  
      img.putpixel((i,j), normal)
      i+=1
    j+=1

while j<lim4:
    i=5
    while i<1920:  
      img.putpixel((i,j), 0)
      i+=1
    j+=1  

img.show();