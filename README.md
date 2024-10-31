Tarea 

Objetivo: Generar habilidad en el uso del patrón de algoritmo de recorrido total.

Escriba los métodos de la clase Curso que resuelven los siguientes problemas, los cuales corresponden a las dos variantes del patrón de algoritmo de recorrido total.

1. Escriba un método para modificar las notas de los estudiantes de la siguiente manera: a todos los que obtuvieron más de 4,0, les quita 0,5. A todos los que obtuvieron menos de 2,0, les aumenta 0,5. A todos los demás, les deja la nota sin modificar:




Def cambiarNotas(self):

\_\_author\_\_= "Juan Sebastian Ibarra Salas"

\_\_License\_\_="GPL"

\_\_Version\_\_="1.0.0"

\_\_Email\_\_="juan.ibarrasalas@campusucc.edu.co"

#Metodos

def cambiarNotas(self) -> float:

`    `for nota in self.notas:

`        `if nota >= 4.0:

`            `nota -= 0.5



`        `elif nota <= 2.0:

`            `nota += 0.5



1. Escriba un método que retorne la menor nota del curso:

Def darMenorNota(self):

def darMenorNotaEstudiante (self):

`    `darMenorNotaEstudiante = self.nota [0]

`    `for nota in self.notas:

`        `if nota <= darMenorNotaEstudiante:

`            `darMenorNotaEstudiante = nota

`        `return darMenorNotaEstudiante




1. Escriba un método que indique en cuál rango se encuentra la mayoría de las notas del curso. Los rangos están definidos de la siguiente manera: rango 1 de 0,0 a 1,99, rango 2 de 2,0 a 3,49, rango 3 de 3,5 a 5,0. El método debe retornar el número del rango.

Def darRangoConMasNotas(self):

def darRangoConMasNotas(self):

`    `notasRango1 = 0

`    `notasRango2 = 0

`    `notasRango3 = 0

`    `for nota in self.notas:

`        `if 0.0 <= nota < 1.99:

`            `notasRango1 += 1

`        `elif 1.5 <= 3.49:

`            `notasRango2 += 1

`        `elif 3.5 <= 5.0:

`            `notasRango3 +=1



`            `if notasRango1 > notasRango2 and notasRango1 > notasRango3:

`                `return 1

`        `elif notasRango2 > notasRango1 and notasRango2 > notasRango3:

`            `return 2

`        `else:

`            `return 3




