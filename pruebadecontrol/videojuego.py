class Videojuego:
    def __init__(self, codigo, nombre, genero):
        self.codigo = codigo
        self.nombre = nombre
        self.genero = genero
        self.prestado = False

    def prestar(self):
        if self.prestado:
            print(f"El videojuego '{self.nombre}' ya está prestado.")
            return False
        self.prestado = True
        return True

    def devolver(self):
        if not self.prestado:
            print(f"El videojuego '{self.nombre}' no estaba prestado.")
            return False
        self.prestado = False
        return True

    def mostrar_informacion(self):
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Código: {self.codigo} | Nombre: {self.nombre} | Género: {self.genero} | Estado: {estado}")