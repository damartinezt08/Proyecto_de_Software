# importamos la clase
import clases as cl

# instancias de alumnos
alumno1 = cl.Alumnos()

# instancias de materias
materia1 = cl.Materias("LE1", "Intro a Eco", "01")
materia2 = cl.Materias("LE2", "Bienestar Total", "02")
materia3 = cl.Materias("CJ1", "Intro a Derecho", "03")
materia4 = cl.Materias("IN1", "Intro a Inge", "04")
materia5 = cl.Materias("IN2", "Preca", "05")
materia6 = cl.Materias("SF1", "Intro a Software", "06")

# instancia de inscripcion
inscripcion1 = cl.Inscripciones(108, alumno1)

## obteniendo informacion

# imprima el carnet del alumno
print(f"El alumno de la inscripcion {inscripcion1.correlativo} es ")
print(f"{inscripcion1.alumno.carnet}")
print(f"y tiene {len(inscripcion1.materias)}")