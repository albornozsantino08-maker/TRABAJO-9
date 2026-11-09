import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar_bd():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

def agregar_jugador():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura en metros (ej: 1.75): "))
    posicion = input("Posición: ")

    conexion = conectar_bd()
    cursor = conexion.cursor()

    sql = "INSERT INTO Jugadores (Nombre, Apellido, Edad, Altura, Posicion) VALUES (%s, %s, %s, %s, %s)"
    datos = (nombre, apellido, edad, altura, posicion)

    cursor.execute(sql, datos)
    conexion.commit()

    print("✅ Jugador agregado correctamente")

    cursor.close()
    conexion.close()

def actualizar_jugador():
    listar_jugadores()
    id_jugador = int(input("ID del jugador a modificar: "))
    nueva_posicion = input("Nueva posición: ")

    conexion = conectar_bd()
    cursor = conexion.cursor()

    sql = "UPDATE Jugadores SET posicion = %s WHERE ID_Jugador = %s"
    datos = (nueva_posicion, id_jugador)

    cursor.execute(sql, datos)
    conexion.commit()

    print("✅ Jugador actualizado correctamente")

    cursor.close()
    conexion.close()

def eliminar_jugador():
    listar_jugadores()
    id_jugador = int(input("ID del jugador a eliminar: "))

    confirmar = input("¿Está seguro? (s/n): ")

    if confirmar.lower() == "s":
        conexion = conectar_bd()
        cursor = conexion.cursor()

        sql = "DELETE FROM Jugadores WHERE ID_jugador = %s"

        cursor.execute(sql, (id_jugador,))
        conexion.commit()

        print("✅ Jugador eliminado correctamente")

        cursor.close()
        conexion.close()
    else:
        print("❌ Eliminación cancelada")

def listar_jugadores():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("SELECT ID_Jugador, Nombre, Apellido, Edad, Altura, Posicion FROM Jugadores")
    filas = cursor.fetchall()

    for fila in filas:
        print(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

    cursor.close()
    conexion.close()


def main():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DEPORTIVA ===")
        print("1. Ver jugadores")
        print("2. Agregar jugador")
        print("3. Modificar jugador")
        print("4. Eliminar jugador")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            listar_jugadores()
        elif opcion == "2":
            agregar_jugador()
        elif opcion == "3":
            actualizar_jugador()
        elif opcion == "4":
            eliminar_jugador()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida")

main()
#agregar_jugador()
#actualizar_jugador()
#eliminar_jugador()
#listar_jugadores()   

