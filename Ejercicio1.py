# Ejercicio 1
class Perro:
    def __init__(self): # aqui se definen las caracteristicas que utilizaremos
        self.nombre = ""
        self.peso = 0
        self.raza = ""
        self.color = ""
        self.edad = 0
        self.estado = "no atendido"
        self.tipo = ""
    
    def registrar(self,nombre,peso,raza,color,edad): # espacio para el registro de las caracteristicas
        self.nombre = nombre
        self.peso = peso
        self.raza = raza
        self.color = color
        self.edad = edad
        self.estado = "atendido"
        if peso > 10: # condicional para el tipo de perro segun su peso
            self.tipo = "Perro grande"
        else:
            self.tipo = "Perro pequeño"

    def info(self):
        return ("############################\n" # impresion de la informacion del perro
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
print("Ingrese los datos de su mascota.") # ingreso de datos del usuario
nombre = input("Nombre: ")
peso = float(input("Peso (kg): "))
raza = input("Raza: ")
color = input("Color: ")
edad = int(input("Edad: "))  

mascota.registrar(nombre, peso, raza, color, edad) # envio de datos al registro

print(mascota.info())  # impresion de datos