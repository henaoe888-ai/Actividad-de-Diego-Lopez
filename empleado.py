from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self,nombre,documento,salario): #Constructor de la clase
        self.nombre = nombre #Atributo
        self.documento = documento #Atributo
        self.salario = salario #Atributo

        @abstractmethod  #Metodo abstracto
        def calcular_bonificacion(self):
            pass
        
        def mostrar_informacion(self): #Metodo
            print(f"Nombre: {self.nombre}")
            print(f"Documento: {self.documento}")
            print(f"Salario: {self.salario:,.0f}")

        def __str__(self): #Metodo
            return f"Nombre: {self.nombre} - Documento: {self.documento}"