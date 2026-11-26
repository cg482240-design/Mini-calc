from arbol import Nodo
from errores import ErrorSintactico


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.arboles = []

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

            arbol = self.expresion()

            self.consumir("PUNCT_SEMI")
            self.arboles.append(arbol)

        elif tipo == "KW_PRINT":
            self.consumir("KW_PRINT")

            arbol = self.expresion()

            self.consumir("PUNCT_SEMI")
            self.arboles.append(arbol)

        else:
            token = self.token_actual()

            raise ErrorSintactico(
                "sentencia no válida",
                token[2],
                token[3]
            )

    # expresion -> termino expresion_prima
    def expresion(self):
        return Nodo("E", [
            self.termino(),
            self.expresion_prima()
        ])

    # expresion_prima -> + T E' | - T E' | epsilon
    def expresion_prima(self):
        tipo = self.token_actual()[0]

        if tipo in ("OP_ADD", "OP_SUB"):
            operador = self.consumir(tipo)[1]

            return Nodo("E'", [
                Nodo(operador),
                self.termino(),
                self.expresion_prima()
            ])

        return Nodo("E'", [Nodo("ε")])

    # termino -> factor termino_prima
    def termino(self):
        return Nodo("T", [
            self.factor(),
            self.termino_prima()
        ])

    # termino_prima -> * F T' | / F T' | epsilon
    def termino_prima(self):
        tipo = self.token_actual()[0]

        if tipo in ("OP_MUL", "OP_DIV"):
            operador = self.consumir(tipo)[1]

            return Nodo("T'", [
                Nodo(operador),
                self.factor(),
                self.termino_prima()
            ])

        return Nodo("T'", [Nodo("ε")])

    # factor -> ( expresion ) | ID | NUM
    def factor(self):
        tipo = self.token_actual()[0]

        if tipo == "PUNCT_LPAREN":
            self.consumir("PUNCT_LPAREN")
            expresion = self.expresion()
            self.consumir("PUNCT_RPAREN")

            return Nodo("F", [
                Nodo("("),
                expresion,
                Nodo(")")
            ])

        elif tipo == "ID":
            token = self.consumir("ID")
            return Nodo("F", [Nodo(token[1])])

        elif tipo == "NUM":
            token = self.consumir("NUM")
            return Nodo("F", [Nodo(token[1])])

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