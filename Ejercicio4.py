# Ejercicio 4
class dispositivo:
    def __init__(self,disp,caracteristicas,precioc): # se definen los datos a solicitar
        self.producto = "importado"
        self.disp = disp
        self.marca = "PHR"
        self.caracteristicas = caracteristicas
        self.precioc = precioc
        self.preciov = precioc * 1.7

    def info(self): # se define los datos que seran impresos
        print("*********************************")
        print("---informacion del producto---")
        print(f"Producto {self.producto}")
        print(f"{self.disp}")
        print(f"Marca: {self.marca}")
        print("Características:")
        for i, caracteristica in enumerate(self.caracteristicas, start=1): # enumeracion de las caracteristicas que se solicitan
            print(f"  {i}. {caracteristica}")
        print(f"preceio de compra: ${self.precioc}") # en este caso decidi si poner el precio de compra
        print(f"Precio de venta: ${self.preciov:.2f}") 
        print("*********************************")

print("Ingrese los datos solicitados.") # solicitud de datos del usuario
print("-------------------------------")
print("Ingrese el tipo de dispositivo")
disp = input("Celular, Tablet, Portatil: ") # solicitud del tipo de dispositivo a ingresar
caracteristicas = []
print("Ingrese 6 principales caracteristicas del dispositivo") 
for i in range(6): # bucle para el ingreso de 6 caracteristicas del dispositivo a ingresar
    caracteristica = input(f"Característica {i + 1}: ")
    caracteristicas.append(caracteristica)
precioc = float(input("Ingrese el precio de compra: "))

almacen = dispositivo(disp,caracteristicas,precioc) # envio de ingreso de datos

almacen.info() # impresion de los datos ingresados