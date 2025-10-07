from rembg import remove
from PIL import Image


remover_fondo = remove(Image.open("input.png")) #Remover el fondo
remover_fondo.save("output.png") #Guardar la imagen sin fondo

