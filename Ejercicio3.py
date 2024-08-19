class Vehiculo:
    def __init__(self, tipo, caracteristicas,precioc):
        self.ruedas = 5
        self.capacidad = 5
        self.tipo = tipo
        self.caracteristicas = caracteristicas
        self.precioc = precioc
        self.preciov = precioc * 1.4

    def info(self):
        print("*****************************************")
        print("Información del Vehículo:")
        print(f"Cantidad de ruedas: {self.ruedas}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"El vehiculo es {self.tipo}")
        print("-------------------------------")
        print("Características:")
        for i, caracteristica in enumerate(self.caracteristicas, start=1):
            print(f"  {i}. {caracteristica}")
        print(f"Precio de venta: ${self.preciov:.2f}")
        print("*****************************************")

print("Ingrese los datos del vehículo")

tipo = input("¿Es nacional o importado?: ")

caracteristicas = []
print("Ingrese las 10 características principales del vehículo:")
for i in range(10):
    caracteristica = input(f"Característica {i + 1}: ")
    caracteristicas.append(caracteristica)

precioc = float(input("Precio de compra: "))
    
vehiculo = Vehiculo(tipo, caracteristicas, precioc)
    
vehiculo.info()