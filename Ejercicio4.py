class dispositivo:
    def __init__(self,disp,caracteristicas,precioc):
        self.producto = "importado"
        self.disp = disp
        self.marca = "PHR"
        self.caracteristicas = caracteristicas
        self.precioc = precioc
        self.preciov = precioc * 1.7

    def info(self):
        print("*********************************")
        print("---informacion del producto---")
        print(f"Producto {self.producto}")
        print(f"{self.disp}")
        print(f"Marca: {self.marca}")
        print("Características:")
        for i, caracteristica in enumerate(self.caracteristicas, start=1):
            print(f"  {i}. {caracteristica}")
        print(f"preceio de compra: ${self.precioc}")
        print(f"Precio de venta: ${self.preciov:.2f}")
        print("*********************************")

print("Ingrese los datos solicitados.")
print("-------------------------------")
print("Ingrese el tipo de dispositivo")
disp = input("Celular, Tablet, Portatil: ")
caracteristicas = []
print("Ingrese 6 principales caracteristicas del dispositivo")
for i in range(6):
    caracteristica = input(f"Característica {i + 1}: ")
    caracteristicas.append(caracteristica)
precioc = float(input("Ingrese el precio de compra: "))

almacen = dispositivo(disp,caracteristicas,precioc)

almacen.info()