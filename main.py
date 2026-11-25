
import sys

from lexer import Lexer
from parser import Parser
from errores import ErrorLexico, ErrorSintactico


try:
    # Elegir el archivo fuente
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = "ejemplo.calc"

    # Leer el archivo fuente
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        codigo = archivo.read()

    # Analisis lexico
    print("=== INICIO DE ANALISIS LEXICO ===")

    analizador_lexico = Lexer(codigo)
    tokens = analizador_lexico.analizar()

    for tipo, valor, linea, columna in tokens:
        if tipo != "EOF":
            print(f'<{tipo}, "{valor}", {linea}, {columna}>')

    print("\n=== INICIO DE ANALISIS SINTACTICO ===")

    # Analisis sintactico
    analizador_sintactico = Parser(tokens)
    analizador_sintactico.analizar()

except (ErrorLexico, ErrorSintactico) as error:
    print(error)

except FileNotFoundError:
    print(f"Error: no se encontró el archivo {nombre_archivo}.")
