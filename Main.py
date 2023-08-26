from Jugador import Jugador
from JuegoUno import JuegoUno
import sqlite3
from BaseDeDatosUNO import crearTabla,eliminarJugador,juegosJugados

class Main:
    def __init__(self):
        self.jugadores = []
        self.crear_jugadores()
        self.juego = JuegoUno(self.jugadores)   

    def crear_jugadores(self):
        while True:
            #Se crea la tabla en la base de datos
            crearTabla()
            try:
                num_jugadores = int(input("Escriba el numero de jugadores: "))  # Puedes cambiar este número según la cantidad de jugadores que desees
                if num_jugadores > 1 and num_jugadores < 8:
                    num_jugadores1 = int(num_jugadores)
                    break
                elif num_jugadores == 1:
                    print("el numero de jugadores debe ser mayor a uno")
                else:
                    print("el numero de jugadores debe ser entre 2 y 7")
            except: print("ERROR!!")
        for i in range(num_jugadores1):
            nombre = input(f"Ingresa el nombre del jugador {i + 1}: ")
            self.jugadores.append(Jugador(nombre))
            #eliminarJugador(nombre) #solo para borrar datos de manera remota

            
            
            

    def iniciar_juego(self):
        self.juego.baraja.mezclar()
        
        # Imprimir la cantidad de cartas por color
        for color, cantidad in self.juego.baraja.contador_por_color.items():
            print(f"Cartas de color {color}: {cantidad + 1}")  # Sumar 1 para contar las cartas 0
        
        # Imprimir la cantidad de cartas especiales y comodines
        print(f"Cartas especiales: {self.juego.baraja.contador_especiales}")
        print(f"Comodines: {self.juego.baraja.contador_comodines}")
        
        self.juego.jugar()
        
        #jugar_otra_partida = input("¿Deseas jugar otra partida? (s/n): ")
        #if jugar_otra_partida.lower() != "s":
            #print("¡Hasta luego!")
            #break

if __name__ == "__main__":
    main = Main()
    main.iniciar_juego()

