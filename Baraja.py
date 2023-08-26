import random
from Carta import Carta

class Baraja:
    def __init__(self):
        colores = ["rojo", "verde", "azul", "amarillo"]
        valores = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        valores_especiales = ["Reversa", "Saltar", "Toma2"]###

        self.cartas = [Carta("0", color) for color in colores]  # 1 carta 0 por cada color
        
        for _ in range(2):  # 2 cartas numeradas del 1 al 9 en cada color
            self.cartas += [Carta(valor, color) for color in colores for valor in valores]
        
        self.cartas += [Carta(valor, color) for valor in valores_especiales for color in colores for _ in range(2)]
        self.cartas += [Carta("CambioColor", "Negro") for _ in range(4)]
        self.cartas += [Carta("Toma4", "Negro") for _ in range(4)]
        

        # Contadores de cartas por color y tipo
        self.contador_por_color = {color: 0 for color in colores}
        self.contador_especiales = 0
        self.contador_comodines = 0

        for carta in self.cartas:
            if carta.color in colores and carta.valor in valores:
                self.contador_por_color[carta.color] += 1
            if carta.valor in valores_especiales:
                self.contador_especiales += 1
            if carta.valor in ["CambioColor", "Toma4"]:
                self.contador_comodines += 1
    
    def mezclar(self):
        random.shuffle(self.cartas)  ##Mezcla las cartas colores y valores

    def repartir_cartas(self, cantidad):
        cartas_repartidas = []
        for _ in range(cantidad):
            cartas_repartidas.append(self.cartas.pop())
        return cartas_repartidas
    
