import cv2

imagen = cv2.imread("C:/Users/MI PC/Documents/Tratamiento de imagenes/Proyecto/Imagenes/ovnis.jpg",0) 
cv2.imshow("Prueba de imagen", imagen)
cv2.waitKey(0)
cv2.imwrite("ovnisgris.png", imagen)
cv2.destroyAllWindows()
