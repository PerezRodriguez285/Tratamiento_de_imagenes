# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:15:28 2021

@author: MI PC
"""

from PIL import Image

img_bd = Image.open("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/IMG03b.png")
hand = Image.open("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/IMG03a.png")

hand_resize = hand.resize((900,600))

img_bd.paste(hand_resize,(0,0),hand_resize)
img_bd.show()
