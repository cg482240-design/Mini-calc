Mini-calc: Gramática
1. Gramática original
La gramática de Mini-calc admite asignaciones e instrucciones print con expresiones aritméticas. Esta es su forma antes de adaptar las expresiones al análisis descendente:
programa  →  lista_sentencias EOF
lista_sentencias  →  sentencia lista_sentencias | ε
sentencia  →  ID = expresion ;
                 | print expresion ;
expresion  → expresion + termino
                 | expresion - termino
                 | termino
termino  →  termino * factor
                 | termino / factor
                 | factor
factor  →  ( expresion ) | ID | NUM
El símbolo inicial es programa. Los no terminales son programa, lista_sentencias, sentencia, expresion, termino y factor. Los terminales son ID, NUM, print, =, +, -, *, /, (, ) y ;. EOF marca el fin de la entrada.
En el analizador léxico, ID es una sola letra minúscula (a a z) y NUM es uno o más dígitos (0 a 9).
La jerarquía expresion, termino, factor da mayor precedencia a * y / que a + y -. La recursión por la izquierda expresa que los operadores de igual precedencia asocian de izquierda a derecha.
2. Eliminación de la recursividad izquierda
Solo expresion y termino tienen recursividad izquierda, y en ambos casos es directa. Un analizador descendente recursivo no puede usarlas así: expresion() se llamaría a sí misma sin consumir ningún token, y la recursión no terminaría.
Se aplica la siguiente transformación, donde ninguna β comienza con A:
A  → A α1 | A α2 | β

se reemplaza por

A  → β A'
A' → α1 A' | α2 A' | ε
Expresión
Aquí A = expresion, α1 = + termino, α2 = - termino y β = termino.
expresion  →  termino expresion_prima
expresion_prima  →  + termino expresion_prima
                | - termino expresion_prima
                | ε
Término
Aquí A = termino, α1 = * factor, α2 = / factor y β = factor.
termino       → factor termino_prima
termino_prima → * factor termino_prima
              | / factor termino_prima
              | ε
Las demás reglas no cambian. lista_sentencias es recursiva por la derecha, por lo que no necesita transformación. La nueva gramática genera el mismo lenguaje que la original.
3. Gramática adaptada al descenso recursivo
Esta es la gramática que implementa parser.py. Cada no terminal sintáctico corresponde a un método con el mismo nombre. En el árbol, E, E', T, T' y F abrevian los no terminales de las expresiones.
programa  → lista_sentencias EOF
lista_sentencias  →  sentencia lista_sentencias | ε
sentencia  →  ID = expresion ;
                 | print expresion ;
expresion        → termino expresion_prima
expresion_prima  → + termino expresion_prima
                 | - termino expresion_prima
                 | ε
termino  →  factor termino_prima
termino_prima  →  * factor termino_prima
                 | / factor termino_prima
                 | ε
factor  →  ( expresion ) | ID | NUM
Selección de producciones
El analizador elige cada producción mirando un solo token:
• lista_sentencias: elige ε si el token es EOF. En otro caso llama a sentencia, que acepta ID o print y rechaza los demás.
• sentencia: con ID analiza una asignación y con print una impresión.
• expresion_prima: continúa con + o -. Su conjunto SIGUIENTE es { ;, ) }, donde corresponde aplicar ε.
• termino_prima: continúa con * o /. Su conjunto SIGUIENTE es { +, -, ;, ) }, donde corresponde aplicar ε.
• factor: distingue entre (, ID y NUM.
Los conjuntos que inician cada alternativa no se superponen, ni coinciden con el conjunto SIGUIENTE cuando existe una alternativa ε. Por eso la gramática es LL(1) y no requiere retroceso.
En el código, los métodos _prima aplican ε ante cualquier token que no sea uno de sus operadores. Si el token es incorrecto, el error se detecta después, al exigir ) o ;, o al continuar el análisis.
Nota sobre la asociatividad
En el árbol transformado, las repeticiones se extienden hacia la derecha mediante E' y T'. Si luego se evalúan las expresiones, hay que acumular el resultado de izquierda a derecha. Así, 8 - 3 - 2 equivale a (8 - 3) - 2 = 3, no a 8 - (3 - 2) = 7.
