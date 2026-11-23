# Trabajando con funciones
def calcular_nota(parcial: float, final: float):
    pond_parcial = 0.3
    pond_final = 0.7
    nota = (pond_parcial * parcial) + (pond_final * final)
    return nota