from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, lado=0, radio=0, altura=0): #constructor de la clase
        self.__largo = lado #Atributo
        self.radio = radio
        self.altura = altura

    @abstractmethod
    def calcular_volumen(self):
        pass

    @property #Accediendo a un atributo privado
    def lado(self):
        return self.__largo

    def mostrar_informacion(self): #Método
        print(f"lado de la figura: {self.__largo}")
        print(f"radio de la figura: {self.radio}")
        print(f"altura de la figura: {self.altura}")

    def __str__(self): #Método
        return f"lado de la figura: {self.__largo} radio de la figura: {self.radio}, altura de la figura: {self.altura}"


###Realizar un programa orientado a objetos en python que permita
##Calcular el volumen de un cilindro, esfera y cubo
##Aplicar herencia, polimorfismo, abstracción
##Crear objetos. Crear una clase para cilindro otra para esfera y otra para
#cubo

##Cargar el proyecto a git.
