import cv2 as cv
import numpy as np
import easyocr


#Lee la imagen
plate_1 = cv.imread("../assets/placa_q.jpg")
#Cambia el color de la imagen a una con colores grises
plate_1 = cv.cvtColor(plate_1, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 1 gris",plate_1)
#Aplica un desenfoque con el filtro gaussianox
plate_1=cv.GaussianBlur(src=plate_1, ksize=(19,19), sigmaX=43)
cv.imshow("Placa 1 desenfocada",plate_1)
#aplica un detector de  bordes
edges_1 =cv.Canny(plate_1, 80, 122)
cv.imshow("Bordes placa 1",edges_1)


#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results = reader.readtext(plate_1)
text =""

for detected_text in results:
  text += detected_text[1]+ "\n"
print("\nTexto detectado en la placa 1:",text)

cv.waitKey(0)
cv.destroyAllWindows()

#Lee la imagen
plate_2 = cv.imread("../assets/placa_2.jpg")
#Cambia el color de la imagen a una con colores grises
plate_2 = cv.cvtColor(plate_2, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 2 gris",plate_2)
#Aplica un desenfoque con el filtro gaussiano
plate_2=cv.GaussianBlur(src=plate_2, ksize=(121,121), sigmaX=0) #101
cv.imshow("Placa 2 desenfocada",plate_2)
#aplica un detector de  bordes
edges_2 =cv.Canny(plate_2, 1,25)
cv.imshow("Bordes placa 2",edges_2)

#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results_2 = reader.readtext(plate_2)
text_2 =""
for detected_text_2 in results_2:
  text_2 += detected_text_2[1]+ "\n"
print("\nTexto detectado en la placa:",text_2)

cv.waitKey(0)
cv.destroyAllWindows()


#Lee la imagen
plate_3 = cv.imread("../assets/placa_3.jpg")
#Cambia el color de la imagen a una con colores grises
plate_3 = cv.cvtColor(plate_3, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 3 gris",plate_3)
#Aplica un desenfoque con el filtro gaussiano
plate_3=cv.GaussianBlur(src=plate_3, ksize=(25,25), sigmaX=0)
cv.imshow("Placa 3 desenfocada",plate_3)
#aplica un detector de  bordes
edges_3 =cv.Canny(plate_3, 100,120)
cv.imshow("Bordes placa 3",edges_3)

#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results_3 = reader.readtext(plate_3)
text_3 =""
for detected_text_3 in results_3:
  text_3 += detected_text_3[1]+ "\n"
print("\nTexto detectado en la placa:",text_3)


cv.waitKey(0)
cv.destroyAllWindows()

#Lee la imagen
plate_4 = cv.imread("../assets/placa_4.jpg")
#Cambia el color de la imagen a una con colores grises
plate_4 = cv.cvtColor(plate_4, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 4 gris",plate_4)
#Aplica un desenfoque con el filtro gaussiano
plate_4=cv.GaussianBlur(src=plate_4, ksize=(89,89), sigmaX=0)
cv.imshow("Placa 4 desenfoque",plate_4)
#aplica un detector de  bordes
edges_4 =cv.Canny(plate_4, 40,45)
cv.imshow("Bordes placa 4",edges_4)
#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results_4 = reader.readtext(plate_4)
text_4 =""
for detected_text_4 in results_4:
  text_4 += detected_text_4[1]+ "\n"
print("\nTexto detectado en la placa:",text_4)