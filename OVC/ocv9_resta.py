import cv2
import numpy as np
import matplotlib.pyplot as plt

def res2( img1, img2 ):
    r = img1 - img2
    return r


def resTruncar( im1, im2):
    r = np.zeros( im1.shape, dtype=np.int16)
    for f in range( im1.shape[0] ):
        for c in range( im1.shape[1] ):
            r[f,c]  = im1[f,c].astype(np.int16) - im2[f,c].astype(np.int16)
            if r[f,c,0] < 0 :
                r[f,c,0] = 0
            if r[f,c,1] < 0 :
                r[f,c,1] = 0
            if r[f,c,2] < 0 :
                r[f,c,2] = 0
    return r


def restaEscalar( im1, im2):
    r = np.zeros( im1.shape, dtype=np.int32)
    for f in range( im1.shape[0] ):
        for c in range( im1.shape[1] ):
            r[f,c]  = im1[f,c].astype(np.int32) - im2[f,c].astype(np.int32)
    may = np.amax(r)
    men = np.amin(r)
    # print("Mayor: " , may, " Menor: ", men)
    # print("Res: ",r[0:3,0:2])
    if men < 0:
        r  = r-men
    may = np.amax(r)
    men = np.amin(r)
    # print("Mayor: " , may, " Menor: ", men)
    # print("Res: ",r[0:3,0:2])

    r = r*255//may
    may = np.amax(r)
    men = np.amin(r)
    # print("Mayor: " , may, " Menor: ", men)
    # print("Esc: ",r[0:3,0:2])
    return r




im1 = cv2.cvtColor( cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/peppers.tiff'), cv2.COLOR_BGR2RGB )
im2 = cv2.cvtColor( cv2.imread('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/mandrill-baboon.tiff'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig1.jpg'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig2.jpg'), cv2.COLOR_BGR2RGB )
#im2 = cv2.cvtColor( cv2.imread('../Imagenes/fig7.jpg'), cv2.COLOR_BGR2RGB )

resta = cv2.subtract( im1, im2 )                  #101 - 164 = -63 < 0     ==>  0
restaAbs = cv2.absdiff( im1, im2)                   #abs(101 - 164) = abs(-63) ==> 63
#
res2 = res2(im1, im2)
res3 = resTruncar(im1, im2)
res4 = restaEscalar(im1, im2)
#
print("Im1: ", im1[0:3, 0:4])
print("Im2: ", im2[0:3, 0:4])
print("\nResta OpenCv: ", resta[0:3, 0:4])
print("\nResta Absoluto OpenCV: ", restaAbs[0:3, 0:4])
print("\nResta D:", res2[0:3, 0:4])
print("\nResta Truncar:", res3[0:3, 0:4])
print("\nResta Escalar:", res4[0:3, 0:4])

plt.figure(1)
plt.subplot(121)
plt.imshow(im1)
plt.subplot(122)
plt.imshow(im2)

plt.figure(2)
plt.subplot(231)
plt.imshow(resta)
plt.subplot(232)
plt.imshow(restaAbs)
plt.subplot(233)
plt.imshow(res2)
plt.subplot(234)
plt.imshow(res3)
plt.subplot(235)
plt.imshow(res4)
plt.show()
