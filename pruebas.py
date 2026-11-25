
from lexer import Lexer
from parser import Parser
from errores import ErrorLexico, ErrorSintactico


def probar_programa(nombre, codigo):
    print("\nPrueba:", nombre)

    try:
        analizador = Lexer(codigo)
        tokens = analizador.analizar()

        parser = Parser(tokens)
        parser.analizar()

        print("Resultado: CORRECTO")

    except (ErrorLexico, ErrorSintactico) as error:
        print("Resultado: ERROR DETECTADO")
        print(error)


# Prueba 1: programa correcto
probar_programa(
    "Programa correcto",
    "x = 10 + 5 * 2;"
)

# Prueba 2: error lexico
probar_programa(
    "Caracter no permitido",
    "x = 10 + @;"
)

# Prueba 3: error sintactico
probar_programa(
    "Expresion incorrecta",
    "x = + 10;"
)

# Prueba 4: parentesis incorrectos
probar_programa(
    "Parentesis sin cerrar",
    "x = (10 + 5;"
)

# Prueba 5: instruccion print
probar_programa(
    "Instruccion print",
    "print x;"
)


# Prueba 6: falta el punto y coma
probar_programa(
    "Falta punto y coma",
    "x = 10 + 5"
)

# Prueba 7: falta cerrar el parentesis
probar_programa(
    "Parentesis de mas",
    "x = 10 + 5);"
)

# Prueba 8: print sin expresion
probar_programa(
    "Print sin expresion",
    "print ;"
)


# Prueba 9: suma, resta, multiplicación y división
probar_programa(
    "Todas las operaciones",
    "x = 20 + 10 - 5 * 2 / 2;"
)

# Prueba 10: parentesis anidados
probar_programa(
    "Parentesis anidados",
    "x = ((10 + 5) * (8 - 3));"
)

# Prueba 11: expresion para imprimir
probar_programa(
    "Imprimir una expresion",
    "print (10 + 5) * 2;"
)

