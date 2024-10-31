__author__= "Juan Sebastian Ibarra Salas"
__License__="GPL"
__Version__="1.0.0"
__Email__="juan.ibarrasalas@campusucc.edu.co"

#Metodos
def cambiarNotas(self) -> float:
    for nota in self.notas:
        if nota >= 4.0:
            nota -= 0.5
    
        elif nota <= 2.0:
            nota += 0.5

def darMenorNotaEstudiante (self):
    darMenorNotaEstudiante = self.nota [0]
    for nota in self.notas:
        if nota <= darMenorNotaEstudiante:
            darMenorNotaEstudiante = nota
        return darMenorNotaEstudiante
    
    
def darRangoConMasNotas(self):
    notasRango1 = 0
    notasRango2 = 0
    notasRango3 = 0
    for nota in self.notas:
        if 0.0 <= nota < 1.99:
            notasRango1 += 1
        elif 1.5 <= 3.49:
            notasRango2 += 1
        elif 3.5 <= 5.0:
            notasRango3 +=1
            
            if notasRango1 > notasRango2 and notasRango1 > notasRango3:
                return 1
        elif notasRango2 > notasRango1 and notasRango2 > notasRango3:
            return 2
        else:
            return 3

