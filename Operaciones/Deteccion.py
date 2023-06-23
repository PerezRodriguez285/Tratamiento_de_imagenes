# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:49:07 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Operaciones en las imagenes
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
@author: MI PC
"""
import sys
from PIL import Image, ImageFilter

#apertura de la imagen original
imagen = Image.open('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/lenainvertida.png').convert(Ldetector_bordes(tipo)):

    if tipo == 'Prewitt':
        factor = 6
        coeficientes_h = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        coeficientes_v = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        #coeficientes con signo contrario
        coeficientes_h1 = [1, 0, -1, 2, 0, -2, 1, 0, -1]
        coeficientes_v1 = [1, 2, 1, 0, 0, 0, -1, -2, -1]
    elif tipo == 'Sobel':
        factor = 8
        coeficientes_h = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
        coeficientes_v = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
        #coeficientes con signo contrario
        coeficientes_h1 = [1, 0, -1, 2, 0, -2, 1, 0, -1]
        coeficientes_v1 = [1, 2, 1, 0, 0, 0, -1, -2, -1]

    else:
        #en caso de no introducir el nombre correctamente se cierra el script
        sys.exit(0)

    datos_h = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_h, factor)).getdata()
    datos_v = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_v, factor)).getdata()

    datos= []
  

    for x in range(len(datos_h)):
 
        datos.append(round(((datos_h[x] ** 2) + (datos_v[x] ** 2)) ** 0.5))

    datos_h = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_h1, factor)).getdata()
    datos_v = imagen.filter(ImageFilter.Kernel((3,3), coeficientes_v1, factor)).getdata()
 
    datos_signo_contrario = []
 
 
    for x in range(len(datos_h)):
 
        datos_signo_contrario.append(round(((datos_h[x] ** 2) + (datos_v[x] ** 2)) ** 0.5))

   
    datos_bordes = []
 

    for x in range(len(datos_h)):
 
        datos_bordes.append(datos[x] + datos_signo_contrario[x])

    return datos_bordes 

datos_bordes = detector_bordes('Prewitt') 

#linea para hacer la deteccion con Sobel:
datos_bordes = detector_bordes('Sobel')

nueva_imagen = Image.new('Liimagen.size')
nueva_imagen.putdata(datos_bordes)

#guardar el resultado
nueva_imagen.save('/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/')
#cerrar los objetos de la clase Image
imagen.close()
nueva_imagen.close()
