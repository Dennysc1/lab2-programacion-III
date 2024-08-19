# Ejercicio 2
class Productos:
    def __init__(self,nombre,tipo,marca,precioC): # se definen las caracteristicas a utilizar
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.precioC = precioC
        self.precioV = precioC * 1.30 # se multiplica el precio de compra para sacar el precio de venta

    def __str__(self): # los datos que seran almacenados
        return (f" Nombre: {self.nombre}\n Tipo: {self.tipo} hojas\n Marca: {self.marca}\n Precio de Compra: ${self.precioC}\n Precio de Venta: ${self.precioV:.2f}\n"
                "------------------------------")
                

class Almacen: # aqui seran almacenados los datos
    def __init__(self):
        self.productos = []

    def agregarP(self,nombre,tipo,marca, precioC):
        producto = Productos(nombre,tipo,marca, precioC)
        self.productos.append(producto)

    def mostrarP(self): # condicional por si se consultan los datos y todavia no se a agregado ninguno
        if not self.productos:
            print("No hay productos registrados.")
        for producto in self.productos:
            print(producto)

inventario = Almacen()

while True: # ciclo para el ingreso de datos de usuario
    print("===================================")
    print(" ==== Menu ==== ") # menu de opciones para decidir si se almacenaran datos o se observaran los datos
    print("1- agregar producto")
    print("2- mostrar productos")
    print("3- salir")
    opcion = input("Seleccione una opcion (1, 2, 3): ")
    print("---------------------------------")

    if opcion == "1": # ingreso de datos de usuario
        nombre = input("Ingrese el nombre del producto (cuaderno/lapiz): ")
        if nombre == "cuaderno": # condicional para pedir dato diferente si es cuaderno y lapiz
            tipo = input("De cuantas paginas 50 o 100: ")
            marca = "Hojitas"
        elif nombre == "lapiz":
            tipo = input("De que tipo grafito o color: ")
            marca = "Rayas"
        precioC = float(input("Ingrese el precio de compra del producto: "))
        inventario.agregarP(nombre,tipo,marca,precioC)
        print("Producto registrado con éxito.")
    
    elif opcion == "2": # impresion de datos almacenados
        print("\nProductos agregados.")
        print("===================================")
        inventario.mostrarP()

    elif opcion == "3": # cerrar el sistema
        print("bye...")
        break

    else:
        print("opcion invalida")

