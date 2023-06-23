import numpy as np
import matplotlib.pyplot as plt
img = plt.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Dragon_Shiryuu.png")

print( type(img))

plt.imshow( img )
plt.show()

opr = img ** 0.5
opr = np.cos(img)
plt.imshow( opr)
plt.show()

corte = img[0:400, 0:200]   #[y1:y2 , x1:x2]
plt.imshow(corte)
plt.show()

plt.imsave("Corte1.png", corte)
