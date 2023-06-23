"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno:   Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image



im = Image.open('patos.png')

plt.imshow(im)

ax = plt.gca()

rect = patches.Rectangle((500,200),
                 170,
                 100,
                 linewidth=2,
                 edgecolor='cyan',
                 fill = False)

ax.add_patch(rect)

rect = patches.Rectangle((690,280),
                 180,
                 100,
                 linewidth=2,
                 edgecolor='cyan',
                 fill = False)

ax.add_patch(rect)
plt.show()