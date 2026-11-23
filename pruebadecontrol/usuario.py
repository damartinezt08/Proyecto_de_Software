class Usuario:
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.prestamos = []

    def tomar_prestado(self, videojuego):
        if videojuego.prestar():
            self.prestamos.append(videojuego)
            print(f"{self.nombre} prestó '{videojuego.nombre}'.")

    def devolver_videojuego(self, videojuego):
        if videojuego in self.prestamos and videojuego.devolver():
            self.prestamos.remove(videojuego)
            print(f"{self.nombre} devolvió '{videojuego.nombre}'.")
        else:
            print(f"{self.nombre} no tiene prestado '{videojuego.nombre}'.")

    def mostrar_informacion(self):
        titulos = [vj.nombre for vj in self.prestamos] if self.prestamos else ["Ninguno"]
        print(f"Carnet: {self.carnet} | Nombre: {self.nombre} | Préstamos: {', '.join(titulos)}")