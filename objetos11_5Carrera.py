class Carrera:

    def __init__(self,lista_materias_plan):
        
        self.materias = {}
        
        self.__agregar__(lista_materias_plan)

    def __agregar__(self,lista_materias_plan):

        for materia in lista_materias_plan:
            self.materias.update({materia.codigo : [materia.nombre, materia.creditos, 0]})
        
    def __str__(self):
        
        suma_creditos = 0
        promedio = 'N/A'
        suma_notas = 0
        materias_aprobadas = []

        for codigo in self.materias.keys():
            if self.materias[codigo][2] != 0:
                
                materias_aprobadas.append(f'{self.materias.keys()} {self.materias[codigo][0]} ({self.materias[codigo][2]})\n')
            
            suma_creditos += self.materias_
            suma_notas += self.materias[codigo][2]

        if suma_notas !=0:
            promedio = suma_notas / len(self.materias)

        return f'Créditos: {suma_creditos} -- Promedio: {promedio} -- Materias Aprobadas: {materias_aprobadas}'
    
    def aprobar(self,codigo,nota):

        self.materias[codigo][2] = nota
    
