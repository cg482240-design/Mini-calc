
from errores import ErrorLexico


class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.posicion = 0
        self.linea = 1
        self.columna = 1
        self.tokens = []

    def es_letra(self, caracter):
        return "a" <= caracter <= "z"

    def es_digito(self, caracter):
        return "0" <= caracter <= "9"

    def avanzar(self):
        self.posicion += 1
        self.columna += 1

    def agregar_token(self, tipo, valor):
        self.tokens.append(
            (tipo, valor, self.linea, self.columna)
        )

    def analizar(self):
        while self.posicion < len(self.codigo):
            caracter = self.codigo[self.posicion]

            # Ignorar espacios, tabulaciones y retorno de carro
            if caracter in " \t\r":
                self.avanzar()
                continue

            # Reconocer saltos de línea
            if caracter == "\n":
                self.posicion += 1
                self.linea += 1
                self.columna = 1
                continue

            # Reconocer la palabra reservada print
            if self.codigo.startswith("print", self.posicion):
                fin = self.posicion + 5

                if fin == len(self.codigo) or not (
                    self.es_letra(self.codigo[fin])
                    or self.es_digito(self.codigo[fin])
                ):
                    self.agregar_token("KW_PRINT", "print")

                    for _ in range(5):
                        self.avanzar()

                    continue

            # Reconocer números enteros
            if self.es_digito(caracter):
                inicio = self.columna
                numero = ""

                while (
                    self.posicion < len(self.codigo)
                    and self.es_digito(self.codigo[self.posicion])
                ):
                    numero += self.codigo[self.posicion]
                    self.avanzar()

                self.tokens.append(
                    ("NUM", numero, self.linea, inicio)
                )
                continue

            # Reconocer variables de una sola letra
            if self.es_letra(caracter):
                self.agregar_token("ID", caracter)
                self.avanzar()
                continue

            # Reconocer operadores y delimitadores
            simbolos = {
                "=": "OP_ASSIGN",
                "+": "OP_ADD",
                "-": "OP_SUB",
                "*": "OP_MUL",
                "/": "OP_DIV",
                "(": "PUNCT_LPAREN",
                ")": "PUNCT_RPAREN",
                ";": "PUNCT_SEMI"
            }

            if caracter in simbolos:
                self.agregar_token(
                    simbolos[caracter], caracter
                )
                self.avanzar()
                continue

            # Caracter no permitido
            raise ErrorLexico(
                f"carácter no válido '{caracter}'",
                self.linea,
                self.columna
            )

        self.tokens.append(
            ("EOF", "", self.linea, self.columna)
        )

        return self.tokens
