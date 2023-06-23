import numpy as np
import matplotlib.pyplot as plt

#Config para imagenes en gris
plt.rcParams['image.cmap'] = 'gray'

img1 = np.zeros((20,30))    #Para escala de grisesq
plt.imshow(img1, vmin=0, vmax=1)
plt.show()
