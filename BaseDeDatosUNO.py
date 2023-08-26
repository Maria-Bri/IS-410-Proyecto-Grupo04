import sqlite3

def crearTabla():
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()

    #Esta funcion verifica si ya existe la tabla y si no la crea
    cur.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' and name= 'juegoUno'")
    table_exists = cur.fetchone()[0]
    if not table_exists:
        #aqui se crea la tabla si no existe
        cur.execute('CREATE TABLE juegoUno (nombre TEXT, juegosjugados int, puntos int, JuegosGanados int)')
        conn.commit()

        conn.close()

#Esta funcion agregar al jugador en la tabla o base de datos
def agregar(nombre):
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()
    #Para comprobar si el jugador ya existe en la BD
    cur.execute('SELECT nombre FROM juegoUno WHERE nombre = ?', (nombre,))
    resultado = cur.fetchall()

    if resultado:
        return
    
    #si el jugador no existe lo agrega en la BD
    cur.execute('INSERT INTO juegoUno (nombre, juegosjugados, puntos, JuegosGanados) VALUES(?,?,?,?)', (nombre, 0, 0, 0))

    conn.commit()
    conn.close()

#Esta funcion es para eliminar un jugador de la base de datos
def eliminarJugador(nombre):
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()

    #se verifica que el jugador existe en la BD
    cur.execute('SELECT nombre FROM juegoUno WHERE nombre = ?', (nombre,))
    resultado = cur.fetchall()

    if not resultado:
        #si el jugador no existe en la BD
        conn.close()
        return    
    
    #si lo encuentra lo elimina
    cur.execute('DELETE FROM juegoUno WHERE nombre = ?', (nombre,))
    conn.commit()
    conn.close()

#Funcion para actualizar las veces que el usuario a jugado
def juegosJugados(nombre, juegosJugados):
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()

    #se verifica si el jugador existe en la BD
    cur.execute('SELECT nombre FROM juegoUno WHERE nombre = ?', (nombre,))
    resultado = cur.fetchall()

    if not resultado:
        return

    #si lo encuentra actualiza los datos en la BD
    cur.execute('UPDATE juegoUno SET juegosjugados = juegosjugados + ? WHERE nombre = ?', (juegosJugados, nombre))
    conn.commit()
    conn.close()

#Esta funcion actualiza los puntos del jugador si gano
def actualizarPuntos(nombre,puntos):
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()

    #verifica si existe el jugador
    cur.execute('SELECT nombre FROM juegoUno WHERE nombre = ?', (nombre,))
    resultado = cur.fetchall()

    if not resultado:
        return
    
    #aqui se actualizan los puntos si encuentra el usuario en la BD
    cur.execute('UPDATE juegoUno SET puntos = puntos + ? WHERE nombre = ?', (puntos, nombre))
    conn.commit()
    conn.close()

def JuegosGanados(nombre, cantidad):
    conn = sqlite3.connect('juegoUno.db')
    cur = conn.cursor()

    cur.execute('SELECT nombre FROM juegoUno WHERE nombre = ?', (nombre,))
    resultado = cur.fetchall()

    if not resultado:
        return
    
    cur.execute('UPDATE juegoUno SET JuegosGanados = JuegosGanados + ? WHERE nombre = ?', (cantidad, nombre))
    conn.commit()
    conn.close()

