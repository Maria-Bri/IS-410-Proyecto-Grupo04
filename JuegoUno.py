from Baraja import Baraja
from Carta import Carta
from Jugador import Jugador
from BaseDeDatosUNO import actualizarPuntos, JuegosGanados

class JuegoUno:
    def __init__(self, jugadores):
        self.baraja = Baraja()
        self.baraja.mezclar()
        self.jugadores = jugadores
        self.cartas_jugadas = []

    def repartir_cartas_iniciales(self, cantidad):
        for jugador in self.jugadores:
            cartas_iniciales = self.baraja.repartir_cartas(cantidad)
            jugador.tomar_cartas_iniciales(cartas_iniciales)

    def jugar(self):
        self.repartir_cartas_iniciales(7)

        carta_actual = self.baraja.cartas.pop()
        self.cartas_jugadas.append(carta_actual)

        turno = 0
        sentido_del_juego = 1  # 1 para adelante, -1 para atrás

        while True:
            jugador_actual = self.jugadores[turno]
            print("\n" + "=" * 40)
            print(f"La Carta actual es: {carta_actual}")
            print(jugador_actual)

            # Buscamos una carta válida para jugar
            carta_valida = False
            while not carta_valida:
                indice = int(input("Elige el índice de la carta que deseas jugar (primer indice 0) o -1 para tomar otra carta: "))
                if indice == -1:  ##Para tomar una carta de la baraja debe de colocar el indice -1
                    # El jugador toma una carta del mazo o baraja
                    nueva_carta = self.baraja.cartas.pop()
                    print(f"Has tomado una nueva carta: {nueva_carta}")
                    
                    #Si la carta nueva coincide por color o valor o es color negra se juega inmediatamente
                    if nueva_carta.color == carta_actual.color or nueva_carta.valor == carta_actual.valor \
                            or nueva_carta.color == "Negro":
                        carta_actual = nueva_carta  # Actualizar la carta actual
                        self.cartas_jugadas.append(carta_actual)
                        carta_valida = True
                        print("¡Se juega la carta de inmediato porque coincide por color o valor!")
                        continue
                    else:
                        jugador_actual.tomar_carta(nueva_carta)##
                        pass

                    # Si la carta tomada es válida, el jugador la juega automáticamente
                    if nueva_carta.color == carta_actual.color or nueva_carta.valor == carta_actual.valor \
                            or nueva_carta.color == "Negro" or "rojo" or "verde" or "amarillo" or "azul":
                        carta_actual = carta_jugada #Muestra la carta actual sobre la meza#
                        self.cartas_jugadas.append(carta_actual)
                        carta_valida = True
                    else:
                        print("La carta tomada no es válida. Continúa tu turno.")
                else:
                
                    if indice >= 0 and indice < len(jugador_actual.cartas_en_mano):
                        carta_jugada = jugador_actual.jugar_carta(indice)
                        if carta_jugada.color == carta_actual.color or carta_jugada.valor == carta_actual.valor \
                                or carta_jugada.color == "Negro" :
                            carta_actual = carta_jugada
                            self.cartas_jugadas.append(carta_actual)
                            carta_valida = True
                        else:
                            print("Carta no válida. Intente de nuevo.")
                            jugador_actual.tomar_carta(carta_jugada)##
                    else:
                        print("Índice inválido. Intente de nuevo.")

            # Verificamos si el jugador ganó
            if len(jugador_actual.cartas_en_mano) == 1: #Si solo le queda una carta gana
                print(f"¡Felicidades {jugador_actual.nombre} ya has ganado!")
                puntos_ganados = 10  # Por ejemplo, 10 puntos ganados por el jugador
                #desde aqui se actualizan los puntos que gana el jugador por partida
                actualizarPuntos(jugador_actual.nombre , puntos_ganados)
                JuegosGanados(jugador_actual.nombre, puntos_ganados/10)
                break

            # Aplicamos efectos especiales de las cartas
            if carta_actual.valor == "Saltar":#Salta un jugador y hace que pierda el turno ese jugador#
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
            elif carta_actual.valor == "Reversa": #Cambia el sentido del juego#
                sentido_del_juego *= -1
            elif carta_actual.valor == "Toma2":
                siguiente_jugador = self.jugadores[(turno + sentido_del_juego) % len(self.jugadores)]
                cartas_tomar = self.baraja.repartir_cartas(2)
                siguiente_jugador.tomar_cartas_iniciales(cartas_tomar)
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
            elif carta_actual.valor == "Toma4":
                siguiente_jugador = self.jugadores[(turno + sentido_del_juego) % len(self.jugadores)]
                cartas_tomar = self.baraja.repartir_cartas(4)
                siguiente_jugador.tomar_cartas_iniciales(cartas_tomar)
                turno = (turno + 1 * sentido_del_juego) % len(self.jugadores)
                nuevo_color = input("Elige un color para continuar (Rojo, Verde, Azul o Amarillo): ")
                carta_actual.color = nuevo_color
            elif carta_actual.valor == "CambioColor":
                nuevo_color = input("Elige un nuevo color (Rojo, Verde, Azul o Amarillo): ")
                carta_actual.color = nuevo_color

            turno = (turno + sentido_del_juego) % len(self.jugadores)

