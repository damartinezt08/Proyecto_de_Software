from usuario import Usuario
from videojuego import Videojuego

if __name__ == "__main__":
    usuario1 = Usuario("2026001", "Diego")
    juego1 = Videojuego("VJ-01", "Elden Ring", "RPG")
    juego2 = Videojuego("VJ-02", "Mario Kart", "Carreras")

    usuario1.tomar_prestado(juego1)
    usuario1.tomar_prestado(juego1)  # Prueba: ya está prestado

    print("\n--- Estado actual ---")
    usuario1.mostrar_informacion()
    juego1.mostrar_informacion()
    juego2.mostrar_informacion()

    print("\n--- Devolución ---")
    usuario1.devolver_videojuego(juego1)
    usuario1.mostrar_informacion()
    juego1.mostrar_informacion()