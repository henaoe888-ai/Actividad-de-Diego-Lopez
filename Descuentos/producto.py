class Producto:
    def __init__(self,id,nombre,cantidad,precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def cantidad_calcular(self):
        if self.cantidad <= 0:
            print("Tu cantidad debe ser positiva")
        elif self.cantidad < 10:
            descuento = self.precio * 0.05
            return descuento
        elif self.cantidad > 10 and self.cantidad < 50:
            descuento = self.precio * 0.10
            return descuento
        elif self.cantidad >= 49:
            descuento = self.precio * 0.125
            return descuento



producto1 = Producto(4245,'Acer',4,76000)
print(producto1.cantidad_calcular())

producto2 = Producto(3845,'HP',25,98000)
print(producto2.cantidad_calcular())
