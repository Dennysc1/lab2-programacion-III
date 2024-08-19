class Perro:
    def __init__(self):
        self.nombre = ""
        self.peso = 0
        self.raza = ""
        self.color = ""
        self.edad = 0
        self.estado = "no atendido"
        self.tipo = ""
    
    def registrar(self,nombre,peso,raza,color,edad):
        self.nombre = nombre
        self.peso = peso
        self.raza = raza
        self.color = color
        self.edad = edad
        self.estado = "atendido"
        if peso > 10:
            self.tipo = "Perro grande"
        else:
            self.tipo = "Perro pequeño"

    def info(self):
        return ("############################\n"
                "Informacion de la mascota\n"
                f"Nombre: {self.nombre}\n"
                f"Peso: {self.peso} kg\n"
                f"Raza: {self.raza}\n"
                f"Color de pelo: {self.color}\n"
                f"Edad: {self.edad} años\n"
                f"Tipo: {self.tipo} \n"
                f"Estado: {self.estado}\n"
                "############################")

mascota = Perro()
print("Ingrese los datos de su mascota.")
nombre = input("Nombre: ")
peso = float(input("Peso (kg): "))
raza = input("Raza: ")
color = input("Color: ")
edad = int(input("Edad: "))  

mascota.registrar(nombre, peso, raza, color, edad)

print(mascota.info())  