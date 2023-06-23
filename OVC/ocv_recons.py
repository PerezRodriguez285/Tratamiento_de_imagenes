import cv2
import numpy as np
import matplotlib.pyplot as plt


def imreconstruct(marker: np.ndarray, mask: np.ndarray, ee: int = 3):
    kernel = np.ones( (ee,ee), dtype=np.uint8)
    while True:
        expanded = cv2.dilate(src=marker, kernel=kernel)
        cv2.imshow("Dilatacion", expanded)
        cv2.bitwise_and(src1=expanded, src2=mask, dst=expanded)
        cv2.imshow("AND", expanded)
        cv2.waitKey()
        # Termination criterion: Expansion didn't change the image at all
        if (marker == expanded).all():
            return expanded
        marker = expanded

def imreconstructE(marker: np.ndarray, mask: np.ndarray, ee: int = 3):
    kernel = np.ones( (ee,ee), dtype=np.uint8)
    while True:
        expanded = cv2.erode(src=marker, kernel=kernel)
        cv2.imshow("Erosion", expanded)
        cv2.bitwise_or(src1=expanded, src2=mask, dst=expanded)
        cv2.imshow("OR", expanded)
        cv2.waitKey()
        # Termination criterion: Expansion didn't change the image at all
        if (marker == expanded).all():
            return expanded
        marker = expanded


imOrig = cv2.imread('B3.png',0)   #BGR
imMarker = cv2.imread("Marker2.png",0)

cv2.imshow("Orig - Marker", np.hstack((imOrig, imMarker)))
print("Original: \n", imOrig)
print("Marker: \n", imMarker)
cv2.waitKey()

reconst = imreconstructE(imMarker, imOrig, 5)
cv2.imshow("Reconstruccion", reconst)
cv2.waitKey()
cv2.destroyAllWindows()
