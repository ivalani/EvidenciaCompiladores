# EvideniaCompiladores

## _Indice_ 
- [Integrantes](#integrantes)
- [Evidencia a desarrolar](#evidencia-a-desarrollar)
- [Instrucciones de ejecución](#instrucciones-de-ejecución)
- [Contenido de la evidencia](#contenido-de-la-evidencia)
    - [Funcinalidades extras](#funcionalidades-extras)
    - [Reglas de gramatica implementadas](#reglas-de-gramatica-implementadas)
    - [Demostración y ejemplos](#demostración-y-ejemplos)
- [Videos de reflexión](#videos-de-reflexion)
- [Referencias](#referencias-utilizadas)
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

## Instrucciones de ejecución
Para ejecutar el programa de forma local, es necesario que clone el repositorio y se situe en la carpeta "project", como se muestra en el siguiente ejemplo: 

```bash
git clone https://github.com/ivalani/EvidenciaCompiladores.git

cd EvidenciaCompiladores/project
```
* Para ejecutar el programa, además de Python 3.11, será necesario contar con los siguientes requerimientos: 
    * ply
    * matplotlib
    * networkx

En caso de no contar con ninguno de ellos, ejecute el siguiente comando en su terminal:
```bash
pip install -r "requirements.txt"
```

* Finalmente, dentro de la carpeta "project" se encuentra el archivo ejecutable "translator.py, este sera el archivo que se va a ejecutar en la terminal: 
    * Nota: Asegurese de encontrarse dentro de EvidenciaCompiladores/project 
```bash
python translator.py
```

## Contenido de la evidencia
El objetivo de la evidencia consiste en implementar una herramienta que ayude a diseñar flujos de trabajo con imágenes a partir de un traductor.

### Metodo
Para esta actividad se genero un codigo con ayuda del profesor, dicho codigo conforma la base del proyecto, sin embargo, se implementan funcionalidades adicionales que tienen una ponderación sobre la calificación. 

### Funcionalidades extras: 
Las opciones de funcionalidades adicionales a implementar cuentan con una ponderación del 5 al 75, el proposito es; implementar funciones determinadas para obtener un puntaje del 100% de implementaciones. Como equipo, seleccionamos las siguientes: 

| Características                    | Valor |
| ---------------------------------- | ------- |
| Implementación de condicionales    | 75      |
| Implementación de condicionales    | 25      |
| TOTAL    |   100  |

### Reglas de gramatica implementadas: 

### Generales: 
```
<assignment> ::= <VARIABLE> "=" <expression>

               | <VARIABLE> "=" <flow>
               | <expression>

<flow> ::= <VARIABLE> "->" <flow_functions>

<flow_functions> ::= <flow_function_call> "->" <flow_functions>
                   | <flow_function_call>

<flow_function_call> ::= <VARIABLE> "(" <params> ")"
```

### Expresiones 
```
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
```
### Factores 
```
<factor> ::= <NUMBER>
           | <VARIABLE>
           | "(" <expression> ")"
           | <function_call>
```

### Llamadas a funciones 
```
<function_call> ::= <VARIABLE> "(" <params> ")"
                  | <VARIABLE> "(" ")"

<params> ::= <params> "," <expression>
           | <expression>
```

### Tokens 
```
<VARIABLE> ::= [a-zA-Z_][a-zA-Z0-9_]*
<NUMBER> ::= \d+\.?\d*
<STRING> ::= ".*"
```

### Demostración y ejemplos

Por comodidad, se dedican los siguientes espacios para mostrar algunos ejemplos:
- [Ejecución de condicionales](Condicionales.md)
- [Ejecución de pruebas](Pruebas.md)

## Videos de reflexion 

- Alfredo Jeong Hyun Park: https://drive.google.com/file/d/1ydvvtV24pniyrrjYRHTwQPUqxydJLGxB/view?usp=drive_link
- Iwalani Amador Piaga: https://drive.google.com/file/d/1qfYbLvuAZRDxYjhRQ01HC-tIcI44rcI3/view?usp=sharing
- Tonatiuh Reyes Huerta: https://drive.google.com/drive/folders/1VSHqdJm72EbLSGn0KDiupzTjq3elb80u?usp=sharing

## Referencias utilizadas 
http://di002.edv.uniovi.es/~ric/sites/apuntes_dlp/chapters/04_sintactico.gramaticas/04_1_10_creacion_de_gramaticas.html#construcciones-basicas 