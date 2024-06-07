# EvideniaCompiladores

## _Indice_ 
- [Integrantes](#integrantes)
- [Evidencia a desarrolar](#evidencia-a-desarrollar)
- [Reglas de gramatica implementadas](#reglas_de_gramatica_implementadas)
- [Anexos](#anexos)

--- 

## _Integrantes_ 
- Alfredo Jeong Hyun Park
- Iwalani Amador Piaga 
- Tonatiuh Reyes Huerta 

## Evidencia a desarrollar: 
Para este entregable se pide el desarrollo y demostración de una herramienta de soporte al proceso de análisis de imágenes

* Objetivo: Implementar una herramienta que ayude a diseñar flujos de trabajo con imágenes a partir de un traductor.

Mas información en: https://experiencia21.tec.mx/courses/482333/assignments/15445488

---

## Reglas de gramatica implementadas: 

### Generales: 
<assignment> ::= <VARIABLE> "=" <expression>
               | <VARIABLE> "=" <flow>
               | <expression>

<flow> ::= <VARIABLE> "->" <flow_functions>

<flow_functions> ::= <flow_function_call> "->" <flow_functions>
                   | <flow_function_call>

<flow_function_call> ::= <VARIABLE> "(" <params> ")"

### Expresiones 
<expression> ::= <expression> "+" <term>
               | <expression> "-" <term>
               | <term>
               | <string_def>

<string_def> ::= <STRING>

### terminos y factores 
<term> ::= <term> "*" <exponent>
         | <term> "/" <exponent>
         | <exponent>

<exponent> ::= <factor>
             | <factor> "^" <factor>

### Factores 
<factor> ::= <NUMBER>
           | <VARIABLE>
           | "(" <expression> ")"
           | <function_call>


### Llamadas a funciones 
<function_call> ::= <VARIABLE> "(" <params> ")"
                  | <VARIABLE> "(" ")"

<params> ::= <params> "," <expression>
           | <expression>


### Tokens 
<VARIABLE> ::= [a-zA-Z_][a-zA-Z0-9_]*
<NUMBER> ::= \d+\.?\d*
<STRING> ::= ".*"


## Descripcion de las funciones implementadas 


## Demostracion de expresiones y el arbol de sintaxis 

## Videos de reflexion 

- Alfredo Jeong Hyun Park: https://drive.google.com/file/d/1ydvvtV24pniyrrjYRHTwQPUqxydJLGxB/view?usp=drive_link
- Iwalani Amador Piaga: 
- Tonatiuh Reyes Huerta: 

## Referencias utilizadas 
