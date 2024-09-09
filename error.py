class DimensionError(Exception):
    """
    Excepción personalizada para manejar errores relacionados con dimensiones inválidas.

    """

    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None):
        """
        Inicializa una instancia de DimensionError.

        Parámetros:
            mensaje (str): Mensaje de error que describe el problema.
            dimension (int, opcional): Valor de la dimensión que causó el error.
            maximo (int, opcional): Valor máximo permitido para la dimensión.
        """
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self) -> str:
        """
        Retorna una representación en cadena del mensaje de error.

        Si se proporcionaron valores para dimension o maximo, el mensaje será el mensaje de error original.
        Si no se proporcionaron estos valores, se incluirán en el mensaje de error.

        Retorna:
            str: La representación en cadena del error, incluyendo los detalles de la dimensión y el máximo si están disponibles.
        """

        detalles = []
        if self.dimension is not None:
            detalles.append(f"Dimension: {self.dimension}")
        if self.maximo is not None:
            detalles.append(f"Máximo permitido: {self.maximo}")
        
        # Incluir los detalles si están disponibles.
        detalles_str = " - ".join(detalles)
        return f"{self.mensaje} ({detalles_str})" if detalles_str else self.mensaje