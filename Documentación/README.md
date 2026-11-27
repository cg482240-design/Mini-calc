# Mini-Calc

Analizador léxico y sintáctico para **Mini-Calc**, un lenguaje pequeño de cálculos con variables.

El programa lee un archivo `.calc`, lo divide en tokens mediante el análisis léxico y verifica que las sentencias cumplan con la gramática mediante un análisis sintáctico por descenso recursivo.

Si el código es correcto, informa que el análisis finalizó exitosamente. Si encuentra un error, indica el tipo de error, la línea y la columna donde ocurrió.

> Trabajo Práctico Final de Teoría de Autómatas — Ingeniería en Informática — UNIDA — 2026.

## Integrantes

| Integrante | Nombre | Responsabilidad |
|---|---|---|
| 1 | Cesar Gomez | Analizador léxico y código |
| 2 | Enreique Maldonado | Autómata finito (AFD y diagrama de estados) |
| 3 | Carlos Ortiz | Tabla de transiciones |
| 4 | Nauricio Florentin | Gramática y eliminación de recursividad izquierda |
| 5 | Guillermo Zorilla | Árboles de derivación |
| 6 | Santiago Samudio | README, documentación y video demostrativo |

## Requisitos

- Python 3.10 o superior.
- No necesita instalar librerías externas, ya que utiliza solamente la biblioteca estándar de Python.

Para comprobar la versión instalada:

```bash
python --version
```

En Linux o macOS se puede utilizar:

```bash
python3 --version
```

## Instalación

1. Descargar o clonar el repositorio de GitHub.
2. Abrir la carpeta `Mini-calc` en Visual Studio Code.
3. Abrir una terminal dentro de esa carpeta.

No es necesario instalar otras dependencias.

## Ejecución

Para ejecutar el archivo de ejemplo, que utiliza `ejemplo.calc` por defecto:

```bash
python main.py
```

Para ejecutar otro archivo:

```bash
python main.py prueba2.calc
```

Para ejecutar las pruebas automáticas, que incluyen casos correctos e incorrectos:

```bash
python pruebas.py
```

En Linux o macOS se puede utilizar `python3` en lugar de `python`.

## Estructura del proyecto

```text
Mini-calc/
├── Documentación/
│   ├── README.md
│   ├── video-demostrativo.mp4
│   └── documentos-teoricos/
├── main.py
├── lexer.py
├── parser.py
├── errores.py
├── pruebas.py
├── ejemplo.calc
└── prueba2.calc
```

## El lenguaje Mini-Calc

Un programa está formado por una lista de sentencias. Cada sentencia debe terminar con punto y coma (`;`).

Existen dos tipos de sentencias:

**Asignación:**

```text
x = 10 + 5 * 2;
```

**Impresión:**

```text
print x;
```

Las expresiones admiten:

- Números enteros.
- Variables de una sola letra minúscula (`a`–`z`).
- Operadores aritméticos: `+`, `-`, `*` y `/`.
- Paréntesis: `(` y `)`.

La multiplicación y la división tienen mayor prioridad que la suma y la resta.

Ejemplo del archivo `ejemplo.calc`:

```text
x = 10 + 5 * 2;
y = (x - 4) / 2;
print y;
```

## Tokens reconocidos

| Token | Descripción | Ejemplo |
|---|---|---|
| `ID` | Variable de una letra minúscula | `x` |
| `NUM` | Número entero | `10` |
| `KW_PRINT` | Palabra reservada | `print` |
| `OP_ASSIGN` | Asignación | `=` |
| `OP_ADD` | Suma | `+` |
| `OP_SUB` | Resta | `-` |
| `OP_MUL` | Multiplicación | `*` |
| `OP_DIV` | División | `/` |
| `PUNCT_LPAREN` | Paréntesis izquierdo | `(` |
| `PUNCT_RPAREN` | Paréntesis derecho | `)` |
| `PUNCT_SEMI` | Fin de sentencia | `;` |
| `EOF` | Fin del archivo | — |

Los espacios, tabulaciones y saltos de línea son ignorados durante el análisis léxico.

## Gramática utilizada por el parser

La siguiente gramática se utiliza en el analizador sintáctico y está adaptada para el método de descenso recursivo, eliminando la recursividad izquierda.

```text
programa         -> lista_sentencias EOF

lista_sentencias -> sentencia lista_sentencias
                  | ε

sentencia        -> ID = expresion ;
                  | print expresion ;

expresion        -> termino expresion_prima

expresion_prima  -> + termino expresion_prima
                  | - termino expresion_prima
                  | ε

termino          -> factor termino_prima

termino_prima    -> * factor termino_prima
                  | / factor termino_prima
                  | ε

factor           -> ( expresion )
                  | ID
                  | NUM
```

## Salida esperada

Al ejecutar:

```bash
python main.py
```

Se muestran los tokens reconocidos y el resultado del análisis sintáctico.

Ejemplo:

```text
=== INICIO DE ANALISIS LEXICO ===
<ID, "x", 1, 1>
<OP_ASSIGN, "=", 1, 3>
<NUM, "10", 1, 5>
...
<PUNCT_SEMI, ";", 3, 8>

=== INICIO DE ANALISIS SINTACTICO ===
El análisis sintáctico finalizó exitosamente sin errores.
```

## Manejo de errores

El programa detecta errores léxicos y sintácticos, indicando la línea y la columna donde se producen.

| Situación | Ejemplo | Mensaje |
|---|---|---|
| Carácter no permitido | `x = 10 + @;` | `Error léxico: carácter no válido '@'. Línea 1, columna 10` |
| Expresión incorrecta | `x = + 10;` | `Error sintáctico: expresión no válida. Línea 1, columna 5` |
| Falta punto y coma | `x = 10 + 5` | `Error sintáctico: se esperaba PUNCT_SEMI, pero se encontró EOF. Línea 1, columna 11` |
| Paréntesis sin cerrar | `x = (10 + 5;` | `Error sintáctico: se esperaba PUNCT_RPAREN, pero se encontró PUNCT_SEMI. Línea 1, columna 12` |

Si el archivo indicado no existe, el programa muestra un mensaje informando que no se encontró el archivo.

## Limitaciones

- Las variables deben tener una sola letra minúscula.
- Solo se admiten números enteros, sin decimales.
- El programa realiza análisis léxico y sintáctico, pero no calcula ni muestra el resultado numérico de las expresiones.

## Documentación del proyecto

La carpeta `Documentación/` contiene los materiales complementarios del trabajo:

- Diagrama del autómata finito determinista (AFD).
- Tabla de transiciones.
- Gramática y eliminación de recursividad izquierda.
- Árboles de derivación.
- Video demostrativo del funcionamiento del programa.

## Video demostrativo

Archivo: `Documentación/video-demostrativo.mp4`

El video muestra la ejecución del programa, el reconocimiento de tokens y la detección de errores léxicos y sintácticos.
