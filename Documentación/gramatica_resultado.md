## 1. Introducción

Mini-calc es un pequeño lenguaje de programación que permite realizar asignaciones de variables, operaciones aritméticas e instrucciones de impresión mediante `print`.

El objetivo del proyecto es implementar un analizador sintáctico utilizando la técnica de descenso recursivo.

## 2. Gramática original

La gramática original de Mini-calc es:

```text
programa → lista_sentencias EOF

lista_sentencias → sentencia lista_sentencias | ε

sentencia → ID = expresion ;
          | print expresion ;

expresion → expresion + termino
          | expresion - termino
          | termino

termino → termino * factor
        | termino / factor
        | factor

factor → ( expresion )
       | ID
       | NUM
