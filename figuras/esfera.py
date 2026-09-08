from figura_ import Figura

class Esfera(Figura):
    def calcular_volumen(self):
        return 4/3 * 3.1416 * self.radio * self.radio * self.radio