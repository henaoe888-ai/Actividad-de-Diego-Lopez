class Cuenta:
    def __init__(self,numero,saldo): #Constructor: Construye las clases
        self.numero = numero
        self.__saldo = saldo

    def ImprimirSaldo(self):
        print(f"El saldo de la cuenta {self.numero} es: {self.__saldo}")

    def depositar(self,cantidad): #Métodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad invalida")

    def retirar(self,cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

#Creación de el objeto
cuenta1 = Cuenta(1111,1000)
cuenta1.depositar(9999)
cuenta1.retirar(3000)
print(cuenta1.ImprimirSaldo())
