import cv2 as cv
import easyocr

images = [
    {"path": "../assets/placa_q.jpg", "ksize": (19, 19), "sigmaX": 43, "canny_lower": 80,  "canny_upper": 122},
    {"path": "../assets/placa_2.jpg", "ksize": (121,121), "sigmaX": 0,  "canny_lower": 1,   "canny_upper": 25},
    {"path": "../assets/placa_3.jpg", "ksize": (25, 25),  "sigmaX": 0,  "canny_lower": 100, "canny_upper": 120},
    {"path": "../assets/placa_4.jpg", "ksize": (89, 89),  "sigmaX": 0,  "canny_lower": 40,  "canny_upper": 45},
]

reader = easyocr.Reader(['es', 'en'])

def get_plate(plate_details,plate_number):
  #Lee la imagen
  plate = cv.imread(plate_details["path"])
  if plate is None:
    print(f"No se pudo cargar la imagen: {plate_details['path']}")
    return


  #Cambia el color de la imagen a una con colores grises
  plate = cv.cvtColor(plate, cv.COLOR_BGR2GRAY)

  #Aplica un desenfoque con el filtro gaussianox
  plate=cv.GaussianBlur(src=plate, ksize=plate_details["ksize"], sigmaX=plate_details["sigmaX"])
  cv.imshow(f"Plate {plate_number} blurred",plate)
  #aplica un detector de  bordes
  edges =cv.Canny(plate, plate_details["canny_lower"], plate_details["canny_upper"],)
  cv.imshow(f"Plate {plate_number} borders",edges)

  #detección de texto del número de placa con easyocr
  results = reader.readtext(plate)
  text =""
  
  for detected_text in results:
    text += detected_text[1]+ "\n"
  print(f"\n Plate {plate_number} detected text: ",text)

  cv.waitKey(0)
  cv.destroyAllWindows()

for plate_number,plate_details in enumerate(images,start=1):
  get_plate(plate_details,plate_number)