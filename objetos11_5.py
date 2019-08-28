class Materia:

    def __init__(self,codigo,nombre,creditos):
        """constructor de una materia con sus datos"""

        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

class Carrera:

    def __init__(self,lista_materias_plan):
        
        self.materias = {}
        self.__agregar__(lista_materias_plan)

    def __agregar__(self,lista_materias_plan):

        for materia in lista_materias_plan:
            self.materias.update({materia.codigo : [materia.nombre, materia.creditos, 0]})
    
    def aprobar(self,codigo, nota):

        if codigo not in self.materias:
            raise ValueError(f'La materia {codigo} no es parte del plan de estudios')
        self.materias[codigo][2] = nota
    
    def __lista_materias_aprobadas(self):
        
        materias_aprobadas = []
        for codigo in self.materias:
            if self.materias[codigo][2] != 0:
                materias_aprobadas.append(codigo)
        
        return materias_aprobadas
    
    def __str__(self):
        
        materias_aprobadas = self.__lista_materias_aprobadas()
        suma_creditos = 0
        suma_notas = 0
        promedio = 'N/A'

        for codigo in materias_aprobadas:
            suma_creditos += self.materias[codigo][1]
            suma_notas += self.materias[codigo][2]
        
        if suma_notas:
            promedio = round(suma_notas / len(materias_aprobadas),2)

        return f'Créditos: {suma_creditos} -- Promedio: {promedio} -- Materias Aprobadas: {self._lista_aprobadas_con_datos()}'

    def _lista_aprobadas_con_datos(self):

        datos_imprimibles = []
        for codigo in self.__lista_materias_aprobadas():
            datos_imprimibles.append(f'\n{codigo}  {self.materias[codigo][0]}  ({self.materias[codigo][2]})')
            
        
        return "".join(datos_imprimibles)


    
    
