from Carta import Carta
from BaseDeDatosUNO import agregar, juegosJugados


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas_en_mano = []
        #datos que se pasan la base de datos desde la clase Jugador
        agregar(nombre)
        juegosJugados(nombre, 1)
              

    def tomar_cartas_iniciales(self, cartas):
        self.cartas_en_mano.extend(cartas)

    def tomar_carta(self, carta):
        self.cartas_en_mano.append(carta)

    def jugar_carta(self, indice):
        return self.cartas_en_mano.pop(indice)

    def __str__(self):
        cartas_en_mano_str = []
        for i in range(len(self.cartas_en_mano)):
            carta = self.cartas_en_mano[i]
            cartas_en_mano_str.append(f"[{i}] {str(carta)}")
        return f"{self.nombre}, Cartas en mano: {', '.join(cartas_en_mano_str)}"
    
 