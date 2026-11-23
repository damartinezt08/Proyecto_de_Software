# Vamos a defenir clases como alumnos
class Alumno:
    """Clase para instancia alumnos"""
    def __init__(self, carnet:str,nombre:str,edad:int):
        self.carnet = carnet
        self.nombre = nombre
        self.edad = edad
        self.materias = []
    def saludar(self):
        print(f"Buenos dias su nimbre es {self.nombre}")
    def presentarse(self):
        print(f"Hola, mi carnet es {self.carnet}, mi nimbre es {self.nombre} y tengo {self.edad} años")
    def cambiar_nombre(self,nuevo_nombre:str):
        self.nombre = nuevo_nombre
        print(F"Mi nombre actual ahora es: {self.nombre}")
    def inscribir_materias(self,cantidad:int):
        """Metodo para inscribir una materia"""
        for i in range(cantidad):
            nueva_materia = input("Digite la nueba materia: ")
        self.materias.append(nueva_materia)
    def mostrar_materias(self):
        for i in range(len(self.materias)):
            print(f"{i + 1}. {self.materias[i]}") 