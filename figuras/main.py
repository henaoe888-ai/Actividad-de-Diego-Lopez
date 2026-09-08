from cubo import Cubo
from cilindro import Cilindro
from esfera import Esfera


def main():
    cubo = Cubo(45)
    cilindro = Cilindro(45,45,12)
    esfera = Esfera(45,45,45)

    print(f"el volumen del cubo es: ",cubo.calcular_volumen())
    print(f"el volumen del cilindro es: ",cilindro.calcular_volumen())
    print(f"el volumen de la esfera es: ",esfera.calcular_volumen())


if __name__ == "__main__":
    main()