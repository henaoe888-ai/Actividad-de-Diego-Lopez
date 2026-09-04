class Figura:
    def __init__(self, largo):
        self.largo = largo
    
class Cuadrado(Figura):
    def PerimetroCuadrado(self):
        perimetro = 4 * self.largo
        return perimetro
        
    def AreaCuadrado(self):
        area = (self.largo ** 2)
        return area
    
class Círculo(Figura):
    def PerimetroCírculo(self):
        perimetro = 2 * 3.1416 * self.largo
        return perimetro
        
    def AreaCírculo(self):
        area = 3.1416 * self.largo ** 2
        return area
        
cuadrado = Cuadrado(4)
print(f"perimetro del cuadrado: ", cuadrado.PerimetroCuadrado())
print(f"Area del cuadrado: ", cuadrado.AreaCuadrado())
circulo = Círculo(5)
print(f"Perimetro del circulo: " ,circulo.PerimetroCírculo())
print(f"Area del circulo: " , circulo.AreaCírculo())
