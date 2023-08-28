# IS-410-Proyecto-Grupo04

## integrantes del grupo
* Heber Wagner Vasquez Valladares 20151005219
* Carlos Dionisio Fernanadez Betancourt 20171000975
* Alejandra Maria Briceño Dominguez 20181003159
* Kency Pamela Oseguera Valdez 20201004556

## reglas
* Se puede jugar entre un mínimo de dos y un máximo de siete personas.
* Cada jugador iniciara con 7 cartas.
* Cada jugador ira lanzando una carta de acuerdo a su turno, que coincida con el valor, color o caso especial.
* Cuenta con cartas de casos especiales.
   * **Reversa** invierte el orden del juego.
   * **Saltar** salta un turno al siguiente jugador.
   * **Toma 2** aumenta dos cartas al siguiente jugador.
   * **Cambio de color** puede cambiar el color que se lleva en el juego.
   * **Toma 4** aumenta cuatro cartas al siguiente jugador.
* De no contar con una carta que coincida, ira tomando una de la baraja hasta que encuentre una. 
* Ganará el que cuente con una carta, o el mínimo al finalizar la baraja.
  
## funcionalidad

### Utilizando Python
* El proyecto hace una simulacion del juego de meza "Uno", en el cual solicita al usuario el numero de jugadores entre 
  el rango de 2 a 7, luego solicita el nombre de cada uno.
* Toma una carta de forma aleatoria de la baraja para iniciar el juego y asigna a cada jugador 7 cartas de forma aleatoria.
* Las cartas  combinan entre los colores *rojo, azul, verde y amarillo* y los números entre *0 y 9*, Ademas de los colores
  y casos epeciales, a excepcion **Cambio de color** y **Toma cuatro**, ya que el jugador decidira cual color se juega después.
* Al jugador se le mostrará el índice de sus cartas, que valor y color tienen, de escoger una carta que no coincida, se repetira
  la anterior instrucción, hasta que escoja una carta correcta ó tome una de la baraja hasta que coindida.
* El indice para tomar cartas de la baraja es -1. 

### Utilizando SQL
* Crea una tabla que la almacena los datos de juegoUno.
 este permite definir funciones qcomo jeugos jugados que contabiliza cada juego, asì como juegos ganados por cada jugador.

## Video
[Video](https://drive.google.com/file/d/1czLrWHE1J01X8OI7XjoFLbAG2t4mISsY/view?usp=drive_link)

