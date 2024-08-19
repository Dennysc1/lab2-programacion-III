class Productos:
    def __init__(self,nombre,tipo,marca,precioC):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.precioC = precioC
        self.precioV = precioC * 1.30

    def __str__(self):
        return (f" Nombre: {self.nombre}\n Tipo: {self.tipo} hojas\n Marca: {self.marca}\n Precio de Compra: ${self.precioC}\n Precio de Venta: ${self.precioV:.2f}\n"
                "------------------------------")
                

class Almacen:
    def __init__(self):
        self.productos = []

    def agregarP(self,nombre,tipo,marca, precioC):
        producto = Productos(nombre,tipo,marca, precioC)
        self.productos.append(producto)

    def mostrarP(self):
        if not self.productos:
            print("No hay productos registrados.")
        for producto in self.productos:
            print(producto)

inventario = Almacen()

while True:
    print("===================================")
    print(" ==== Menu ==== ")
    print("1- agregar producto")
    print("2- mostrar productos")
    print("3- salir")
    opcion = input("Seleccione una opcion (1, 2, 3): ")
    print("---------------------------------")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto (cuaderno/lapiz): ")
        if nombre == "cuaderno":
            tipo = input("De cuantas paginas 50 o 100: ")
            marca = "Hojitas"
        elif nombre == "lapiz":
            tipo = input("De que tipo grafito o color: ")
            marca = "Rayas"
        precioC = float(input("Ingrese el precio de compra del producto: "))
        inventario.agregarP(nombre,tipo,marca,precioC)
        print("Producto registrado con éxito.")
    
    elif opcion == "2":
        print("\nProductos agregados.")
        print("===================================")
        inventario.mostrarP()

    elif opcion == "3":
        print("bye...")
        break

    else:
        print("opcion invalida")

