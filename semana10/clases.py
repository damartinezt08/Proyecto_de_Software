# vamos a crear las clases del sistema de Inscripcion

class Alumnos:
    def __init__(self):
        print("Vamos a registrar al alumno.")
        self.nombre = input("Nombre del alumno: ")
        self.carnet = input("Digite el carnet: ")
        self.edad = int(input("Digite la edad: "))
        
class Materias:
    def __init__(self, codigo: str, nombre: str, cod_maestro: str):
        self.codigo = codigo
        self.nombre = nombre
        self.maestro = cod_maestro
        
class Inscripciones:
    def __init__(self, correlativo_inscripcion: int, alumno: Alumnos):
        self.correlativo = correlativo_inscripcion
        self.alumno = alumno
        self.materias = []
        self.materias_maxima = 5