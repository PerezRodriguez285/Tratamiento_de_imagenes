
import matplotlib.pyplot as plt
img = plt.imread("/Users/MI PC/Documents/Tratamiento de imagenes/Imagen/Lenna.png")

print( img.shape )
print( img.size )

red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

plt.imshow(red)
plt.title("Rojo")
plt.axis("off")
plt.show()
#plano numero 1
plt.imshow(green, cmap="gray")
plt.title("Verde")
plt.axis("off")
plt.show()

#Obtener histograma. ravel regresa un arreglo continuo
plt.hist( red.ravel(), bins=256 )  #8by
plt.title("Rojo 256")
plt.show()

plt.hist( red.ravel(), bins=128 ) #6
plt.title("Rojo 128")
plt.show()

plt.hist( red.ravel(), bins=64 ) #6
plt.title("Rojo 64")
plt.show()
