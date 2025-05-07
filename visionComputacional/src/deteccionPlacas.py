import cv2 as cv
import numpy as np
import easyocr


#Lee la imagen
p1 = cv.imread("../assets/placa_q.jpg")
#Cambia el color de la imagen a una con colores grises
p1 = cv.cvtColor(p1, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 1 gris",p1)
#Aplica un desenfoque con el filtro gaussianox
p1=cv.GaussianBlur(src=p1, ksize=(19,19), sigmaX=43)
cv.imshow("Placa 1 desenfocada",p1)
#aplica un detector de  bordes
edges1 =cv.Canny(p1, 80, 122)
cv.imshow("Bordes placa 1",edges1)


#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results = reader.readtext(p1)
text =""

for detectedText in results:
  text += detectedText[1]+ "\n"
print("\nTexto detectado en la placa 1:",text)

cv.waitKey(0)
cv.destroyAllWindows()

#Lee la imagen
p2 = cv.imread("../assets/placa_2.jpg")
#Cambia el color de la imagen a una con colores grises
p2 = cv.cvtColor(p2, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 2 gris",p2)
#Aplica un desenfoque con el filtro gaussiano
p2=cv.GaussianBlur(src=p2, ksize=(121,121), sigmaX=0) #101
cv.imshow("Placa 2 desenfocada",p2)
#aplica un detector de  bordes
edges2 =cv.Canny(p2, 1,25)
cv.imshow("Bordes placa 2",edges2)

#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results2 = reader.readtext(p2)
text2 =""
for detectedText2 in results2:
  text2 += detectedText2[1]+ "\n"
print("\nTexto detectado en la placa:",text2)

cv.waitKey(0)
cv.destroyAllWindows()


#Lee la imagen
p3 = cv.imread("../assets/placa_3.jpg")
#Cambia el color de la imagen a una con colores grises
p3 = cv.cvtColor(p3, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 3 gris",p3)
#Aplica un desenfoque con el filtro gaussiano
p3=cv.GaussianBlur(src=p3, ksize=(25,25), sigmaX=0)
cv.imshow("Placa 3 desenfocada",p3)
#aplica un detector de  bordes
edges3 =cv.Canny(p3, 100,120)
cv.imshow("Bordes placa 3",edges3)

#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results3 = reader.readtext(p3)
text3 =""
for detectedText3 in results3:
  text3 += detectedText3[1]+ "\n"
print("\nTexto detectado en la placa:",text3)


cv.waitKey(0)
cv.destroyAllWindows()

#Lee la imagen
p4 = cv.imread("../assets/placa_4.jpg")
#Cambia el color de la imagen a una con colores grises
p4 = cv.cvtColor(p4, cv.COLOR_BGR2GRAY)
cv.imshow("Placa 4 gris",p4)
#Aplica un desenfoque con el filtro gaussiano
p4=cv.GaussianBlur(src=p4, ksize=(89,89), sigmaX=0)
cv.imshow("Placa 4 desenfoque",p4)
#aplica un detector de  bordes
edges4 =cv.Canny(p4, 40,45)
cv.imshow("Bordes placa 4",edges4)
#detección de texto del número de placa con easyocr
reader = easyocr.Reader(['es', 'en'])
results4 = reader.readtext(p4)
text4 =""
for detectedText4 in results4:
  text4 += detectedText4[1]+ "\n"
print("\nTexto detectado en la placa:",text4)