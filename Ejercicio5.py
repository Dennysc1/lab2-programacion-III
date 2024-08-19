# Ejercicio 5 ejercicio propio
# consiste en un sistema similar al caso del ejercicio 2 con la 
# diferencia que es para el almacenamiento de ropa a un almacen
class ropa:
    def __init__(self,tipo,talla,marca,color,precio): # definicion de datos a solicitar
        self.tipo = tipo
        self.talla = talla
        self.marca = marca
        self.color = color
        self.precio = precio # en este caso el mismo que ingresa los datos decide el precio de venta

    def __str__(self): # datos que sera impresos
        return (f" Tipo: {self.tipo}\n Talla: {self.talla}\n Marca: {self.marca}\n Color: {self.color}\n Precio: ${self.precio}\n"
                "------------------------------")
                

class Almacen: # aqui se guardaran los datos que se ingresen
    def __init__(self):
        self.ropa = []

    def agregarP(self,tipo,talla,marca,color,precio):
        producto = ropa(tipo,talla,marca,color,precio)
        self.ropa.append(producto)

    def mostrarP(self):
        if not self.ropa:
            print("No hay productos registrados.")
        for producto in self.ropa:
            print(producto)

inventario = Almacen()

while True: # ciclo while para la solicitud de datos por medio de menu
    print("*********************************")
    print(" --- opciones --- ")
    print("a- Agregar prenda")
    print("b- Mostrar inventario")
    print("c- Salir")
    opcion = input("Seleccione una opcion (a, b, c): ") # opciones a elegir
    print("---------------------------------")

    if opcion == "a": # ingreso de datos al sistema
        print("Que tipo de prenda desea agregar: ")
        tipo = input("Camisa, pantalon, vestido, zapatos: ")
        talla = input("Ingrese la talla de la prenda: ").upper() # upper para que la talla salga siempre en mayuscula
        marca = input("Ingrese la marca de la prenda: ")
        color = input("Ingrese el color de la prenda: ")
        precio = input("Ingrese el precio del producto: ")
        inventario.agregarP(tipo,talla,marca,color,precio) # envio de datos al sistema
        print("Prenda registrada")
    
    elif opcion == "b": # opcion para ver datos ya guardados
        print("\nProductos agregados.")
        print("*********************************")
        inventario.mostrarP()

    elif opcion == "c": # apagar el sistema
        print("Cerrando...")
        break

    else:
        print("opcion invalida")