# python comprende que las clases tienen propiedad y metodos
# las propiedades son caracteristicas del objeto (nombre, edad, correo, etc.)
# se pueden identificar como recetas o instrucciones para trabajar con un objeto
class Perro:
    def __init__(self): # este metodo incia de manera automatica los atributos de un objeto
        self.patas = 4
        self.nombre = ""
        self_estado_alegre = True   #todo esto es un constructor que se ejecuta sin ser llamado 6-8
    def ladrar(self):
        print("Gua")
# creamos una instancia
perrito1 = Perro()
print(perrito1.patas)
otro_perrito = Perro()
print(otro_perrito.patas)
perrito1.ladrar()