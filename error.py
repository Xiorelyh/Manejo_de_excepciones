class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo
        super().__init__(mensaje)

    def __str__(self):
        if self.dimension is not None or self.maximo is not None:
            return super().__str__()
        else:
            return f"{self.mensaje} - Dimesion: {self.dimension} - Maximo: {self.maximo}"