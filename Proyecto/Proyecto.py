# -*- coding: utf-8 -*-
"""
Created on Sun May 16 19:59:03 2021

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Tratamiento de imagenes
TEMA: Proyecto final
Alumno: Antonio Alberto de la Luz Perez Rodriguez
Profesora: Mtra. Edith Cristina Herrena Luna
Descripción: Tratamiento de imagenes aplicando todo lo aprendido durante el semestre
"""

from matplotlib import pyplot as plt
from scipy import ndimage as ndi
from collections import Counter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import DoubleVar
from skimage import feature
from tkinter import Canvas
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import Menu
from tkinter import Tk
from tkinter import NW
from PIL import Image
import numpy as np
import scipy.misc
import statistics
import numpy
import scipy


def abrir():
    ventana.filename = filedialog.askopenfilename(initialdir = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/',title = "Elige Tu Archivo De Imagen:", filetypes = (("Imagenes PNG", "*.png"), ("Imagenes JPG", "*.jpg"),("Imagenes GIF ", "*.gif")))    
    global ruta    
    ruta = ventana.filename
    imagenL = PhotoImage(file = ruta)
    global abrirImagen
    abrirImagen = canvas.create_image(110, 160, anchor=NW, image=imagenL)
    ventana.mainloop()
    
def grises():
    im = Image.open(ruta)
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i, j), pixel)
            j+=1
        i+=1
    g = im2.convert('L')
    g.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Resultados/grises.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/grises.gif')
    global grisesito
    grisesito = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop() 
    
def negativo():    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    im15 = im
    i = 0
    while i < im15.size[0]:
        j = 0
        while j < im15.size[1]:
            gris = im15.getpixel((i,j))
            valor = 255 - gris
            im15.putpixel((i, j), valor)
            j+=1
        i+=1
    im15.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/negativo.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/negativo.gif')
    global neg
    neg = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()
    
def binarizar():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        ima = im
        ren, col = ima.size
        imActual = ima
        pixeles = imActual.load()
        imBinaria = Image.new('RGB', (ren, col))
        binPix = imBinaria.load()
        for x in range(ren):
            for y in range(col):
                if pixeles[x,y] >= alpha:
                    binPix[x,y] = (255,255,255)
                else:
                    binPix[x,y] = (0,0,0)
        imBinaria.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/binarizar.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/binarizar.gif')
        global binaria
        binaria = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()

def rbg():
    im=Image.open(ruta)
    [ren,col]=im.size
    out=im
    i=0
    while i<ren:
        j=0
        while j<col:
            niveles=im.getpixel((i,j))
            nivel_r=niveles[0]
            nivel_g=niveles[1]
            nivel_b=niveles[2]
            out.putpixel((i,j),(nivel_r,nivel_b,nivel_g))
            j+=1
        i+=1
    out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/rbg.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/rbg.gif')
    global rbg
    rbg = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()
    
def maximo():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    arreglo = np.array(im.size)
    mayor=255
    reg1=0
    while reg1<arreglo[0]:
        col1=0
        while col1<arreglo[1]:
            nivel=im.getpixel((reg1,col1))
            if nivel>mayor:
                mayor=nivel
            col1+=1
        reg1+=1
    messagebox.showinfo("MAXIMO:", ("El Nivel Maximo De Gris Es:==>", mayor))
    ventana.mainloop()
    
def minimo():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    arreglo = np.array(im.size)
    menor=255
    reg1=0
    while reg1<arreglo[0]:
        col1=0
        while col1<arreglo[1]:
            nivel=im.getpixel((reg1,col1))
            if nivel<menor:
                menor=nivel
            col1+=1
        reg1+=1
    messagebox.showinfo("MINIMO:", ("El Nivel Minimo De Gris Es:==>", menor))
    ventana.mainloop()

def transpuesta():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    im7 = im
    ar = np.zeros((im7.size[0], im7.size[1]))
    i = 0 
    while i < im7.size[1]:
        j = 0
        while j < im7.size[0]:
            a = im7.getpixel((j, i))
            ar[j, i] = a
            j+=1
        i+=1
    ar = ar.astype(int)    
    im7 = Image.fromarray(ar)
    im7.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/transpuesta.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/transpuesta.gif')
    global trans   
    trans = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()
    
def histograma():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    im16 = im
    [ren, col] = im16.size
    total = ren * col
    a = np.asarray(im16, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    valor = 0
    maxd = max(a)
    grises = maxd
    vec=np.zeros(grises + 1)
    for i in range(total - 1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.plot(vec)
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/histograma.png', dpi=80)
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/histograma.png')
    global hist
    hist = canvas.create_image(520, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def brillo():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    im9 = im
    arreglo = np.array(im9.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im9.size[0]:
        j = 0
        while j < im9.size[1]:
            suma = suma + im9.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total 
    brillo = int(brillo)
    brillo = messagebox.showinfo("BRILLO:", ("El Brillo De La Imagen Es:==> ", brillo))
    ventana.mainloop()
    
def contraste():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    im10 = im
    arreglo = np.array(im10.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            suma = suma + im10.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total
    i = 0 
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            aux = im10.getpixel((i,j)) - brillo 
            suma = suma + aux
            j+=1
        i+=1
    cont = suma * suma
    cont = np.sqrt(suma / total)
    contraste = int(cont)
    contraste = messagebox.showinfo("CONTRASTE:", ("El Contraste De La Imagen Es:==> ", contraste))
    ventana.mainloop()

def suma():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        im11 = im
        i = 0
        while i < im11.size[0]:
            j = 0
            while j < im11.size[1]:
                valor = im11.getpixel((i, j))
                valor = valor + alpha
                if valor >= 255:
                    valor = 255
                else:
                    valor = valor
                im11.putpixel((i, j),(valor))
                j+=1
            i+=1
        im11.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/suma.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/suma.gif')
        global sumita
        sumita = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()
        
def resta():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:    
        im12 = im
        i = 0
        while i < im12.size[0]:
            j = 0
            while j < im12.size[1]:
                valor = im12.getpixel((i, j))
                valor = valor - alpha
                if valor >= 255:
                    valor = 255
                else:
                    valor = valor
                im12.putpixel((i, j),(valor))
                j+=1
            i+=1
        im12.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/resta.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/resta.gif')
        global restita
        restita = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()

def multiplicacion():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        im13 = im
        i = 0
        while i < im13.size[0]:
            j = 0
            while j < im13.size[1]:
                valor = im13.getpixel((i, j))
                valor = valor * alpha
                if valor >= 255:
                    valor = 255
                else:
                    valor = valor
                im13.putpixel((i, j),(valor))
                j+=1
            i+=1
        im13.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/multiplicar.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Resultados/multiplicar.gif')
        global multi
        multi = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()

def division():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:    
        im14 = im
        i = 0
        while i < im14.size[0]:
            j = 0
            while j < im14.size[1]:
                valor = im14.getpixel((i, j)) 
                valor = valor / alpha
                valor = int(valor)
                if valor <= 0:
                    valor = abs(valor)
                else:
                    valor = valor
                im14.putpixel((i, j),(valor))
                j+=1
            i+=1
        im14.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/dividir.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/dividir.gif')
        global div
        div = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()
        
def binaria_And():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    esc = entrada.get()
    if esc==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:  
        [ren, col]=im.size
        m = numpy.asarray(im,dtype = numpy.float32)
        i = 0    
        while i < col:
            j=0
            while j < ren:
                b1 = int(m[i,j])
                np = bin(esc & b1)
                np = int(np,2)
                m[i,j] = np
                j+=1
            i+=1
        out = Image.fromarray(m)
        out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/And.gif')
        imagenL = PhotoImage(file='C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/And.gif')
        global And        
        And = canvas.create_image(600,160,anchor=NW, image=imagenL)
        ventana.mainloop()

def binaria_Or():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    esc = entrada.get()
    if esc==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:  
        [ren, col]=im.size
        m = numpy.asarray(im,dtype = numpy.float32)
        esc=entrada.get()
        i=0    
        while i<col:
            j=0
            while j<ren:
                b1=int(m[i,j])
                np=bin(esc | b1)
                np=int(np,2)
                m[i,j]=np
                j+=1
            i+=1
        out = Image.fromarray(m)
        out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/Or.gif')
        imagenL = PhotoImage(file='C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/Or.gif')
        global Or        
        Or = canvas.create_image(600,160,anchor=NW, image=imagenL)
        ventana.mainloop()

def gamma():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    alpha = entrada2.get()
    if alpha==0.0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0.0"))
    else:
        ima = im
        arreglo = np.array(ima.size)
    #   alpha = cuadrada 2, cubica 3, raiz cuadrada 1/2(0.5), raiz cubica 1/3(0.33)
        L = 255
        reg1=0
        while reg1<arreglo[0]:
            col1=0
            while col1<arreglo[1]:
                nivel = ima.getpixel((reg1, col1))
                new_nivel = L * pow((nivel / L), alpha) 
                new_nivel = int(new_nivel)
                if new_nivel >= 255:
                    new_nivel = 255
                else:
                    new_nivel = new_nivel
                ima.putpixel((reg1, col1), (new_nivel))
                col1+=1
            reg1+=1
        ima.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/gamma.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/gamma.gif')
        global gam
        gam = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()     
        
def convolucion():    
    datos = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    datos=np.asarray(datos)
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    ima = im
    dimension = datos.shape[0]
    datos = np.asarray(datos, dtype = np.float32)
    datos = datos.reshape(dimension, dimension)
    [col,ren] = ima.size
    imagen1 = np.asarray(ima, dtype = np.float32)
    imagen2 = imagen1
    i = 0
    while i < ren-dimension:     
        j = 0
        while j < col-dimension:
            sub = imagen1[i:(dimension + i), j:(dimension + j)]
            suma = 0
            r = 0
            while r < dimension:     
                c=0
                while c < dimension:
                    suma = suma + sub[r,c] * datos[r,c]
                    c+=1
                r+=1
            valor = suma / (dimension * dimension)
            indice1 = ((dimension / 2 + .5) + i)
            indice2 = ((dimension / 2 + .5) + j)
            imagen2[indice1, indice2]=valor
            j+=1
        i+=1
    imagen2=Image.fromarray(imagen2)
    imagen2.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/convolucion.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/convolucion.gif')
    global convol    
    convol = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def gaussiano():
    nombre = 'grises.gif'
    l = scipy.misc.imread("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    noisy = l + 0.4 * l.std() * np.random.random(l.shape)
    plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/gaussiano.png', dpi=90)
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/gaussiano.png')
    global gauss
    gauss = canvas.create_image(450, 130, anchor=NW, image=imagenL)
    ventana.mainloop()
    
def salypimienta():    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    prob = entrada.get()
    if prob==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        [ren, col] = im.size
        sal = im
        nMaxRen = round(ren * prob / 100.0)
        nMaxCol = round(col * prob / 100.0)
        i = 1
        for i in range(nMaxRen):
            j = 1
            for j in range(nMaxCol):
                cx = round(np.random.rand() * (col - 1)) + 1
                cy = round(np.random.rand() * (ren - 1)) + 1
                aaa = round(np.random.rand() * 255)
            if aaa > 128:
                val = 255
                sal.putpixel((cy, cx),(val))
            else:
                val= 1
                sal.putpixel((cy, cx),(val))
        sal.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/sal.gif') 
        imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/sal.gif')
        global sal_y_pimienta
        sal_y_pimienta = canvas.create_image(600, 160, anchor=NW, image=imagenL)
        ventana.mainloop()

def ecualizacion_uniforme():    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    ima = im
    [ren, col] = ima.size 
    ima = np.asarray(ima, dtype = np.float32).reshape(1, ren * col)
    valor = 0 
    maxdata = max(max(ima))
    mindata = min(min(ima))
    niveles = maxdata
    h = np.zeros(niveles)
    ima = ima.reshape(col, ren)
    ac = h
    i = 0
    #cálculo del histograma
    while i < ren:
        j = 0
        while j<col:
            valor = ima[j, i] - 1
            h[valor] = h[valor] + 1
            j+=1
        i+=1
    ac[0] = h[0]
    i = 1
    while i < maxdata:
        ac[i] = ac[i - 1] + h[i]
        i+=1
    ac = ac / (ren * col)
    #funcion de mapeo 
    m1 = maxdata - mindata
    m2 = m1 * ac
    m3 = m2 + mindata
    mapeo = np.floor(m3)
    #si mindata es cero la imagen sera cero
    newim = np.zeros((col, ren))
    i = 0
    while i < ren:
        j = 0
        while j < col:
            newim[j, i] = mapeo[ima[j, i] - 1]
            j+=1
        i+=1
    newim = Image.fromarray(newim)
    newim.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/ecualizacionUniforme.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/ecualizacionUniforme.gif')
    global ecualizacionUniforme    
    ecualizacionUniforme = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def filtro_maximo():    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    out = im
    [ren, col] = out.size
    matriz = np.asarray(out, dtype = np.float32)
    i = 0
    while i < ren - 3:
        j = 0
        while j < col - 3:
            submatriz = matriz[j:j+3,i:i+3]
            submatriz = submatriz.reshape(1, 9)
            nuevo = int(max(max(submatriz)))
            out.putpixel((i + 1, j + 1),(nuevo))
            j+=1
        i+=1
    out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMaximo.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMaximo.gif')
    global filtroMaximo    
    filtroMaximo = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def filtro_minimo():    
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    out = im
    [ren, col] = out.size
    matriz = np.asarray(out, dtype = np.float32)
    i = 0
    while i < ren - 3:
        j = 0
        while j < col - 3:
            submatriz = matriz[j:j+3,i:i+3]
            submatriz = submatriz.reshape(1, 9)
            nuevo = int(min(min(submatriz)))
            out.putpixel((i + 1, j + 1),(nuevo))
            j+=1
        i+=1
    out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMinimo.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMinimo.gif')
    global filtroMinimo    
    filtroMinimo = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def filtro_mediana():   
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    out = im
    [ren, col] = out.size
    matriz = np.asarray(out, dtype = np.float32)
    i = 0
    while i < ren - 3:
        j = 0
        while j < col - 3:
            submatriz = matriz[j:j+3,i:i+3]
            submatriz = submatriz.reshape(1, 9)
            nuevo = (max(submatriz))
            nuevo = statistics.median(nuevo)
            nuevo = int(nuevo)
            out.putpixel((i + 1, j + 1),(nuevo))
            j+=1
        i+=1
    out.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMediana.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/filtroMediana.gif')
    global filtroMediana    
    filtroMediana = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def bordes_sobel():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    ima = im
    [ren, col] = ima.size
    pix = ima.load()
    out_im = Image.new("L", (ren, col))
    mask = ([1,3,3],[-3,-2,3],[-3,-3,1])   
    out = out_im.load()
    for i in range(ren):
        for j in range(col):
            suma = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and m >= 0 and n < ren and m < col:
                        suma += mask[n - (i - 1)][ m - (j - 1)] * pix[n, m]
            out[i, j] = suma
    out_im.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/bordesSobel.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/bordesSobel.gif')
    global bordesSobel    
    bordesSobel = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def bordes_canny():  
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    ima = im
    ima = ndi.gaussian_filter(im, 1)
    edges = feature.canny(ima)
    fig, (ax2) = plt.subplots(nrows = 1, ncols = 1, figsize = (8, 6), sharex = True, sharey = True)
    ax2.imshow(edges, cmap = plt.cm.gray)
    ax2.axis('off')
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/bordesCanny.png')
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/bordesCanny.png')
    global bordesCanny    
    bordesCanny = canvas.create_image(450, 100, anchor=NW, image=imagenL)
    ventana.mainloop()

def erosion():
    datos = np.zeros((16, 16))
    datos[4:-4, 4:-4] = 1
    dist = ndi.distance_transform_bf(datos)
    eroded_dist = ndi.grey_erosion(dist, size=(3, 3), structure=np.ones((2, 2)))
    plt.figure(figsize=(11.14, 8.34))
    plt.subplot(131)
    plt.imshow(dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(eroded_dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/erosion.png')
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/erosion.png')
    global ero    
    ero = canvas.create_image(100, 20, anchor=NW, image=imagenL)
    ventana.mainloop()   

def dilatacion():
    datos = np.zeros((16, 16))
    datos[4:-4, 4:-4] = 1
    dist = ndi.distance_transform_bf(datos)
    dilate_dist = ndi.grey_dilation(dist, size=(3, 3), structure=np.ones((3, 3)))
    plt.figure(figsize=(11.14, 8.34))
    plt.subplot(131)
    plt.imshow(dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(dilate_dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/dilatacion.png')
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/dilatacion.png')
    global dil    
    dil = canvas.create_image(100, 20, anchor=NW, image=imagenL)
    ventana.mainloop() 

def apertura():
    square = np.zeros((32, 32))
    square[10:-10, 10:-10] = 1
    np.random.seed(2)
    x, y = (32*np.random.random((2, 20))).astype(np.int)
    square[x, y] = 1
    eroded_square = ndi.binary_erosion(square)
    reconstruction = ndi.binary_propagation(eroded_square, mask=square)
    plt.figure(figsize=(11.14, 8.34))
    plt.subplot(131)
    plt.imshow(square, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(reconstruction, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.savefig('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/apertura.png')
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/apertura.png')
    global ape
    ape = canvas.create_image(100, 20, anchor=NW, image=imagenL)
    ventana.mainloop()   


def otsu():
    nombre = 'grises.gif'
    im = Image.open("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/" + nombre)
    ima = im
    width, height = ima.size
    img = np.array(ima.getdata())
    histogram = np.array(ima.histogram(),float) / (width * height)
    omega = np.zeros(256)
    mean = np.zeros(256)
    omega[0] = histogram[0]
    for i in range(len(histogram)):
        omega[i] = omega[i - 1] + histogram[i]
        mean[i] = mean[i - 1] + (i - 1) * histogram[i]
    sigmaB2 = 0
    mt = mean[len(histogram) - 1] #El Valor de la intensidad media de la imagen
    sigmaB2max = 0
    T = 0
    for i in range(len(histogram)):
        clase1 = omega[i]
        clase2 = 1 - clase1
        if clase1 != 0 and clase2 != 0:
            m1 = mean[i] / clase1
            m2 = (mt - mean[i]) / clase2
            sigmaB2 = (clase1 * (m1 - mt) * (m1 - mt) + clase2 * (m2 - mt) * (m2 - mt))
            if sigmaB2 > sigmaB2max:
                sigmaB2max = sigmaB2
                T = i
    thr = int(T)
    messagebox.showinfo("UMBRAL OPTIMO:", ("El Umbral Optimo De La Imagen Es::==> ", thr))
    #Se Aplica la umbralización al "array" de la imagen
    #limites de procesado en x
    x_min, x_max = 0, width
    #limites de procesado en y
    y_min, y_max = 0, height
    #imagen de salida
    img_out = np.zeros(width * height)
    loc = 0 #posicin del "pixel" actual
    for y in range (y_min, y_max):
        for x in range(x_min, x_max):
            loc = y * width + x
            if img[loc] > thr:
                img_out[loc] = 255
            else:
                img_out[loc] = 0
    img_thr = img_out
    im_otsu = img_thr.reshape(height, width)
    im_otsu = Image.fromarray(im_otsu)
    im_otsu.save('C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/otsu.gif') 
    imagenL = PhotoImage(file = 'C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/Resultados/otsu.gif')
    global Otsu    
    Otsu = canvas.create_image(600, 160, anchor=NW, image=imagenL)
    ventana.mainloop()

def limpiar():
    canvas.delete("all")

"""Creacion De Ventana Y Lienzo (Canvas)"""
ventana = Tk()
w = 1000
h = 650
extraW=ventana.winfo_screenwidth() - w
extraH=ventana.winfo_screenheight() - h
ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
canvas = Canvas(ventana, width=1000, height=650)
canvas.pack()
ventana.title("PROCESAMIENTO DIGITAL DE IMAGENES")
entrada = IntVar()
entrada2 = DoubleVar()
Entry(ventana, textvariable = entrada, width = 8).place(x=20, y=65)
Label(text = "Ingrese Los Pixeles ", font= ("Times New Roman",9)).place(x=0, y=20)
Label(text = "En Enteros ", font= ("Times New Roman",9)).place(x=17, y=40)
Label(text = "En Decimales ", font= ("Times New Roman",9)).place(x=14, y=87)
Entry(ventana, textvariable = entrada2, width = 8).place(x=20, y=110)
Label(text = "IMAGEN ORIGINAL", font= ("Times New Roman",14)).place(x=175, y=120)
Label(text = "IMAGEN PROCESADA", font= ("Times New Roman",14)).place(x=650, y=120)
#Label(text = "NOTA IMPORTANTE:", fg = 'red', font= ("Times New Roman",13)).place(x=5, y=500)
#Label(text = "PARA LOS METODOS DE BINARIZAR, SUMA DE PIXELES, RESTA DE PIXELES, MULTIPLICACION DE PIXELES, DIVISION DE PIXELES, ECUALIZACION RAYLEIGH", font= ("Times New Roman",10)).place(x=10, y=540)
#Label(text = "AND, OR, RUIDO SAL Y PIMIENTA Y BORDES DE CANNY, SE TIENE QUE AGREGAR UN VALOR ENTERO EN EL CAMPO DE" ,font= ("Times New Roman",10)).place(x=10, y=560)
#Label(text = "(INGRESE LOS PIXELES EN ENTEROS).", fg = 'red', font =("Times New Roman",10)).place(x=690, y=560)
#Label(text = "PARA LOS METODOS DE CORRECION GAMMA Y ECUALIZACION EXPONENCIAL", font= ("Times New Roman",10)).place(x=10, y=600)
#Label(text = "SE TIENE QUE AGREGAR UN VALOR DECIMAL EN EL CAMPO DE" ,font= ("Times New Roman",10)).place(x=10, y=620)
#Label(text = "(INGRESE LOS PIXELES EN DECIMALES).", fg = 'red', font =("Times New Roman",10)).place(x=385, y=620)

"""Creacion De Los Menus"""
barraMenu = Menu(ventana)
mnuOpciones = Menu(barraMenu)
mnuOpcion1 = Menu(barraMenu)
mnuOpcion2 = Menu(barraMenu)
mnuOpcion3 = Menu(barraMenu)
mnuOpcion4 = Menu(barraMenu)
mnuOpcion5 = Menu(barraMenu)

mnuOpcion1.add_command(label = "ABRIR IMAGEN", command = abrir)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "RBG", command = rbg)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "ESCALA DE GRISES", command = grises)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "MAXIMO DE GRISES", command = maximo)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "MINIMO DE GRISES", command = minimo)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "BINARIZACION", command = binarizar)
mnuOpcion1.add_separator()
mnuOpcion1.add_command(label = "NEGATIVO", command = negativo)

mnuOpcion2.add_command(label = "BRILLO", command = brillo)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "CONTRASTE", command = contraste)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "SUMA DE PIXELES", command = suma)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "RESTA DE PIXELES", command = resta)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "MULTIPLICACION DE PIXELES", command = multiplicacion)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "DIVISION DE PIXALES", command = division)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "AND", command = binaria_And)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "OR", command = binaria_Or)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "CORRECION GAMMA", command = gamma)
mnuOpcion2.add_separator()
mnuOpcion2.add_command(label = "HISTOGRAMA", command = histograma)
mnuOpcion2.add_separator()

mnuOpcion3.add_command(label = "CONVOLUCION", command = convolucion)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "RUIDO GAUSSIANO", command = gaussiano)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "RUIDO SAL Y PIMIENTA", command = salypimienta)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "FILTRO MAXIMO", command = filtro_maximo)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "FILTRO MINIMO", command = filtro_minimo)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "FILTRO MEDIANA", command = filtro_mediana)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "BORDES (SOBEL)", command = bordes_sobel)
mnuOpcion3.add_separator()
mnuOpcion3.add_command(label = "BORDES (CANNY)", command = bordes_canny)

mnuOpcion4.add_command(label = "EROSION", command = erosion)
mnuOpcion4.add_separator()
mnuOpcion4.add_command(label = "DILATACION", command = dilatacion)
mnuOpcion4.add_separator()
mnuOpcion4.add_command(label = "APERTURA", command = apertura)

mnuOpcion5.add_command(label = "OTSU", command = otsu)

mnuOpciones.add_command(label = "LIMPIAR", command = limpiar)
mnuOpciones.add_separator()
mnuOpciones.add_command(label = "SALIR", command = ventana.destroy)

barraMenu.add_cascade(label = "Opcion 1", menu = mnuOpcion1)
barraMenu.add_cascade(label = "Opcion 2", menu = mnuOpcion2)
barraMenu.add_cascade(label = "Opcion 3", menu = mnuOpcion3)
barraMenu.add_cascade(label = "Opcion 4", menu = mnuOpcion4)
barraMenu.add_cascade(label = "Opcion 5", menu = mnuOpcion5)
barraMenu.add_cascade(label = "OPCIONES", menu = mnuOpciones)
ventana.config(menu = barraMenu)
ventana.mainloop()