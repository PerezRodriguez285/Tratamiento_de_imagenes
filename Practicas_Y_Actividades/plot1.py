import numpy as np
import matplotlib.pyplot as plt

#interactivo
#plt.ion()
#plt.plot([1.6, 2.7])
#plt.title("interactive test")
#plt.xlabel("index")
#ax = plt.gca()
#ax.plot([3.1, 2.2])
#plt.draw()

#Nointeractivo
plt.ioff()
plt.plot([1.6, 2.7])
plt.show()

for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()

plt.ylabel("Etiqueta Y")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
