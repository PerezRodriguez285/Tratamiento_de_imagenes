# -*- coding: utf-8 -*-
"""
Created on Sat May 29 17:50:46 2021


Alumno: Antonio Alberto de la Luz Perez Rodriguez
"""
from PIL import Image

img_bd = Image.open("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/paisaje3.jpg")
hand = Image.open("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/yo.jpg")

hand_resize = hand.resize((1200,700))

img_bd.paste(hand_resize,(0,0),hand_resize)
img_bd.show()