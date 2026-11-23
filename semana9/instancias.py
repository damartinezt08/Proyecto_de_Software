# Vamos a insustanciar alumnos

from semana10.clases import Alumno

alumno01 = Alumno("0001", "Carlos", 19)
alumno01.saludar()
print(alumno01.edad)
alumno01.presentarse()
alumno01.cambiar_nombre("Alfonso")
alumno01.presentarse()
for i in range(5):
    alumno01.inscribir_materias()
print(alumno01.materias)

        