from error import DimensionError
from foto import Foto

consultar = True
while consultar:
    try:
        ancho = int(input("Ingresa el ancho de la foto:\n>"))
        alto = int(input("Ingresa el alto de la foto:\n>"))
        ruta = input("Ingresa la ruta:\n>")
        prueba_foto = Foto(ancho, alto, ruta)
        consultar = False
    except DimensionError as e:
        print(f"ERROR: {e}")

print("Valores de la foto valida!")

#Aun me falta documentar y Readme