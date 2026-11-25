
from errores import ErrorSintactico


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0

    def token_actual(self):
        return self.tokens[self.posicion]

    def consumir(self, tipo):
        token = self.token_actual()

        if token[0] == tipo:
            self.posicion += 1
            return token

        raise ErrorSintactico(
            f"se esperaba {tipo}, pero se encontró {token[0]}",
            token[2],
            token[3]
        )

    # programa -> lista_sentencias
    def programa(self):
        self.lista_sentencias()
        self.consumir("EOF")

    # lista_sentencias -> sentencia lista_sentencias | epsilon
    def lista_sentencias(self):
        if self.token_actual()[0] == "EOF":
            return

        self.sentencia()
        self.lista_sentencias()

    # sentencia -> ID = expresion ;
    #            | print expresion ;
    def sentencia(self):
        tipo = self.token_actual()[0]

        if tipo == "ID":
            self.consumir("ID")
            self.consumir("OP_ASSIGN")
            self.expresion()
            self.consumir("PUNCT_SEMI")

        elif tipo == "KW_PRINT":
            self.consumir("KW_PRINT")
            self.expresion()
            self.consumir("PUNCT_SEMI")

        else:
            token = self.token_actual()
            raise ErrorSintactico(
                "sentencia no válida",
                token[2],
                token[3]
            )

    # expresion -> termino expresion_prima
    def expresion(self):
        self.termino()
        self.expresion_prima()

    # expresion_prima -> + termino expresion_prima
    #                  | - termino expresion_prima
    #                  | epsilon
    def expresion_prima(self):
        tipo = self.token_actual()[0]

        if tipo in ("OP_ADD", "OP_SUB"):
            self.posicion += 1
            self.termino()
            self.expresion_prima()

    # termino -> factor termino_prima
    def termino(self):
        self.factor()
        self.termino_prima()

    # termino_prima -> * factor termino_prima
    #                | / factor termino_prima
    #                | epsilon
    def termino_prima(self):
        tipo = self.token_actual()[0]

        if tipo in ("OP_MUL", "OP_DIV"):
            self.posicion += 1
            self.factor()
            self.termino_prima()

    # factor -> ( expresion ) | ID | NUM
    def factor(self):
        tipo = self.token_actual()[0]

        if tipo == "PUNCT_LPAREN":
            self.consumir("PUNCT_LPAREN")
            self.expresion()
            self.consumir("PUNCT_RPAREN")

        elif tipo == "ID":
            self.consumir("ID")

        elif tipo == "NUM":
            self.consumir("NUM")

        else:
            token = self.token_actual()
            raise ErrorSintactico(
                "expresión no válida",
                token[2],
                token[3]
            )

    def analizar(self):
        self.programa()
        print("El análisis sintáctico finalizó exitosamente sin errores.")
