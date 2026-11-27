## 1. Gramática original

La gramática original del lenguaje es asi:
```text
lista_sentencias → sentencia lista_sentencias
           | ε


sentencia → ID = expresión ;
           | print expresión ;


expresión → término expresión'


expresión' → + término expresión'
           | - término expresión'
           | ε


término → factor término'


término' → * factor término'
         | / factor término'
         | ε


factor → ( expresión )
       | ID
       | NUM
```

## 2. Eliminación de la recursividad izquierda

Para adaptar la gramática eliminamos la recursividad izquierda.

La transformación general:
```text
A → A α | β
```
Que se transformó en:
```text
A  → β A'
A' → α A' | ε
```
Aplicando esta transformación a la gramática:
Para expresión:

Gramática original:
```text
expresión → expresión + término
           | expresión - término
           | término
```
Gramática sin recursividad izquierda:
```text
expresión  → término expresión'
expresión' → + término expresión'
             | - término expresión'
             | ε
```

Para término:

Gramática original:
```text
término → término * factor
         | término / factor
         | factor
```
Gramática sin recursividad izquierda:
```text
término  → factor término'
término' → * factor término'
           | / factor término'
           | ε
```
La producción de factor no necesita modificaciones porque no presenta recursividad izquierda.

## 3. Gramática adaptada al descenso recursivo

Al eliminar la recursividad izquierda, la gramática completa quedó asi:
```text
programa → lista_sentencias

lista_sentencias → sentencia lista_sentencias
                  | ε

sentencia → ID = expresión ;
           | print expresión ;

expresión → término expresión'

expresión' → + término expresión'
           | - término expresión'
           | ε

término → factor término'

término' → * factor término'
```
         | / factor término'
         | ε
