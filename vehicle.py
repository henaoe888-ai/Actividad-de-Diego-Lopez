class Vehicle: #LLamamos a el objeto y se pone dentro de una clase
    def __init__(self,brand,color,plate): #con una funcion cremos los atributos
        self.brand = brand 
        self.color = color
        self.plate = 'ART-675'
        self.speed = 0

    def acelerar(self):
        self.speed += 10

    def decelerate(self):
        self.speed -= 10
        print(f"El {self.brand} con su placa de {self.plate} desacelero a {self.speed} km/h")

my_vehicle = Vehicle('Hiunday','ART-675','Black')
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.decelerate()
my_vehicle.decelerate()
my_vehicle.decelerate()
my_vehicle.decelerate()

