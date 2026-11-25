
class ErrorLexico(Exception):
    def __init__(self, mensaje, linea, columna):
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna

    def __str__(self):
        return (
            f"Error léxico: {self.mensaje}. "
            f"Línea {self.linea}, columna {self.columna}"
        )


class ErrorSintactico(Exception):
    def __init__(self, mensaje, linea, columna):
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna

    def __str__(self):
        return (
            f"Error sintáctico: {self.mensaje}. "
            f"Línea {self.linea}, columna {self.columna}"
        )
