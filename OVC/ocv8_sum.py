import cv2
import numpy as np
import matplotlib.pyplot as plt

def sum2( img1, img2 ):
    s = img1 + img2         # 101 + 164 = 265%256 ==> 9
    return s


def sumTruncar( im1, im2):
    s = np.zeros( im1.shape, dtype=np.int16)
    for f in range( im1.shape[0] ):
        for c in range( im1.shape[1] ):
            s[f,c]  = im1[f,c].astype(np.int16) + im2[f,c].astype(np.int16)
            if s[f,c,0] > 255 :
                s[f,c,0] = 255
            if s[f,c,1] > 255 :
                s[f,c,1] = 255
            if s[f,c,2] > 255 :
                s[f,c,2] = 255
            #print(s[f,c])
    return s

def sumEscalar( im1, im2):
    s = np.zeros( im1.shape, dtype=np.uint32)
    for f in range( im1.shape[0] ):
        for c in range( im1.shape[1] ):
            s[f,c]  = im1[f,c].astype(np.uint32) + im2[f,c].astype(np.uint32)
    may = np.amax(s)
    men = np.amin(s)
    print("Mayor: " , may, " Menor: ", men)
    #print("sum: ",s[0:3,0:2])
    if men != 0:
        s  = s-men
    may = np.amax(s)
    men = np.amin(s)
    print("Mayor: " , may, " Menor: ", men)
    #print("Res: ",s[0:3,0:2])

    s = s*255//may
    #print("Esc: ",s[0:3,0:2])
    return s


im1 = cv2.cvtColor( cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/peppers.tiff'), cv2.COLOR_BGR2RGB )
im2 = cv2.cvtColor( cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/mandrill-baboon.tiff'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig1.jpg'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig2.jpg'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig7.jpg'), cv2.COLOR_BGR2RGB )

suma = cv2.add( im1, im2 )                  #101 + 164 = 264 > 255    ==>  255
sumaP = cv2.addWeighted( im1, 0.5, im2, 0.8, 0 )        #(im1*0.8) + (im2*0.2) + alpha = imgR

suma2 = sum2(im1, im2)
suma3 = sumTruncar(im1, im2)
suma4 = sumEscalar(im1, im2)

# print("Im1: ", im1[0:3, 0:4])
# print("Im2: ", im2[0:3, 0:4])
# print("\nSuma OpenCv: ", suma[0:3, 0:4])
# print("\nSuma Ponderada OpenCV: ", sumaP[0:3, 0:4])
# print("\nSuma D:", suma2[0:3, 0:4])
# print("\nSuma Truncar:", suma3[0:3, 0:4])
#print("\nSuma Escalar:", suma4[0:3, 0:4])

plt.figure(1)
plt.subplot(121)
plt.imshow(im1)
plt.subplot(122)
plt.imshow(im2)

plt.figure(2)
plt.subplot(231)
plt.imshow(suma)
plt.subplot(232)
plt.imshow(sumaP)
plt.subplot(233)
plt.imshow(suma2)
plt.subplot(234)
plt.imshow(suma3)
plt.subplot(235)
plt.imshow(suma4)
plt.show()
