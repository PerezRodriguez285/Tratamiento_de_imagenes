# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:53:03 2021


Alumno: Antonio Alberto de la Luz Perez Rodriguez
"""

import sys
from PIL import Image, ImageFilter

#apertura de la imagen original
imagen = Image.open('C:/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/paisaje2.jpg').convert(Ldetector_bordes(tipo)
                                                                                                    
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
nueva_imagen = Image.new('Liimagen.size)
nueva_imagen.putdata(datos_bordes)

#guardar el resultado
nueva_imagen.save('ruta_y_nombre_del_archivo
#cerrar los objetos de la clase Image
imagen.close()
nueva_imagen.close()