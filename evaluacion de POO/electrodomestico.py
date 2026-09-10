class Electrodomestico:
    def __init__(self,referencia,marca,precio):
        self.referencia = referencia
        self.marca = marca
        self.precio = precio

    def mostrar(self):
       print(f"tu electrodomestico tiene referencia: {self.referencia}") 
       print(f"tu electrodomestico tiene marca: {self.marca}")
       print(f"tu electrodomestico tiene precio: {self.precio}")

producto = Electrodomestico('XRY23','Haceb',200.000)
producto.mostrar()