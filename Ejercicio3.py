# Ejercicio 3
class Vehiculo:
    def __init__(self, tipo, caracteristicas,precioc): # se definen los datos a solicitar
        self.ruedas = 4
        self.capacidad = 5
        self.tipo = tipo
        self.caracteristicas = caracteristicas
        self.precioc = precioc
        self.preciov = precioc * 1.4

    def info(self): # los datos qu se van a imprimir
        print("*****************************************")
        print("Información del Vehículo:")
        print(f"Cantidad de ruedas: {self.ruedas}")
        print(f"Capacidad: {self.capacidad} personas")
        print(f"El vehiculo es {self.tipo}")
        print("-------------------------------")
        print("Características:")
        for i, caracteristica in enumerate(self.caracteristicas, start=1): # enumeracion de las caracteristicas solicitadas
            print(f"  {i}. {caracteristica}")
        print(f"Precio de venta: ${self.preciov:.2f}") # decidi omitir el precio de compra en la impresion final
        print("*****************************************")

print("Ingrese los datos del vehículo") # solicitud de datos al usuario

tipo = input("¿Es nacional o importado?: ")

caracteristicas = []
print("Ingrese las 10 características principales del vehículo:")
for i in range(10): # ciclo para la solicitud de 10 caracteristicas
    caracteristica = input(f"Característica {i + 1}: ")
    caracteristicas.append(caracteristica)

precioc = float(input("Precio de compra: "))
    
vehiculo = Vehiculo(tipo, caracteristicas, precioc) # envio de datos para la impresion
    
vehiculo.info() # impresion de datos