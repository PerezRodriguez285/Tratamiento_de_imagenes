import cv2
import numpy as np
#import matplotlib.pyplot as plt

f1 = np.zeros((512,512,3), dtype=np.uint8)
cv2.rectangle(f1, (100,100), (412,412), (255,255,255), -1)
cv2.imwrite("../Imagenes/fig1.jpg", f1 )

f2 = np.zeros((512,512,3), dtype=np.uint8)
f2.fill(255)
cv2.rectangle(f2, (100,100), (412,412), (0,0,0), -1)
cv2.imwrite("../Imagenes/fig2.jpg", f2 )

f3 = np.zeros((512,512,3), dtype=np.uint8)
f3.fill(255)
cv2.circle(f3, (256,256), 200, (255,0,0), -1)
cv2.imwrite("../Imagenes/fig3.jpg", f3 )

f4 = np.zeros((512,512,3), dtype=np.uint8)
cv2.circle(f4, (256,256), 200, (255,0,0), -1)
cv2.imwrite("../Imagenes/fig4.jpg", f4 )
#
f5 = np.zeros((512,512,3), dtype=np.uint8)
f5.fill(255)
cv2.circle(f5, (256,256), 200, (0,0,255), -1)
cv2.imwrite("../Imagenes/fig5.jpg", f5 )
#
f6 = np.zeros((512,512,3), dtype=np.uint8)
cv2.circle(f6, (256,256), 200, (0,0,255), -1)
cv2.imwrite("../Imagenes/fig6.jpg", f6 )

f7 = np.zeros((512,512,3), dtype=np.uint8)
f7[:,:,:] = (0,255,255)
cv2.imwrite("../Imagenes/fig7.jpg", f7 )
