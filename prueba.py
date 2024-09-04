from error import DimensionError
from foto import Foto

def main():
    """
    Función principal para consultar al usuario sobre las dimensiones y la ruta de una foto.
    Si el usuario ingresa dimensiones inválidas, se captura la excepción DimensionError y se vuelve a solicitar la entrada.
    Una vez que se ingresan valores válidos, se imprime un mensaje de confirmación.
    """
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

    print("Valores de la foto válidos!")

if __name__ == "__main__":
    main()

