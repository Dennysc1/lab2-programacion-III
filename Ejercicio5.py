class ropa:
    def __init__(self,tipo,talla,marca,color,precio):
        self.tipo = tipo
        self.talla = talla
        self.marca = marca
        self.color = color
        self.precio = precio

    def __str__(self):
        return (f" Tipo: {self.tipo}\n Talla: {self.talla}\n Marca: {self.marca}\n Color: {self.color}\n Precio: ${self.precio}\n"
                "------------------------------")
                

class Almacen:
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

while True:
    print("*********************************")
    print(" --- opciones --- ")
    print("a- Agregar prenda")
    print("b- Mostrar inventario")
    print("c- Salir")
    opcion = input("Seleccione una opcion (a, b, c): ")
    print("---------------------------------")

    if opcion == "a":
        print("Que tipo de prenda desea agregar: ")
        tipo = input("Camisa, pantalon, vestido, zapatos: ")
        talla = input("Ingrese la talla de la prenda: ").upper()
        marca = input("Ingrese la marca de la prenda: ")
        color = input("Ingrese el color de la prenda: ")
        precio = input("Ingrese el precio del producto: ")
        inventario.agregarP(tipo,talla,marca,color,precio)
        print("Prenda registrada")
    
    elif opcion == "b":
        print("\nProductos agregados.")
        print("*********************************")
        inventario.mostrarP()

    elif opcion == "c":
        print("Cerrando...")
        break

    else:
        print("opcion invalida")