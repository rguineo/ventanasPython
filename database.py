import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import sqlite3

def conexionDB():
# Se crea la variable de conexion a la base de datos
    conexion = mysql.connector.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        port = '3306',
        database = 'usuarios'
    )

    print("Conexion con la base de datos")
    return conexion

def selectDB():
    try:
        connection = conexionDB()
        if connection.is_connected():
            print('Conexión establecida...')

            # Se genera la instancia de la conexion con la base de datos
            cursor = connection.cursor()

            # Aqui se realiza la sentencia SQL para realizar la insercion de los datos a la tabla, con los datos proporcionados por el usuario.
            query = "SELECT nomUser, pasUser, nombre, apellido FROM users"

            # Se ejecuta la sentencia de SQL para la insercion en la tabla de la base de datos.
            cursor.execute(query)
                # Obtener todos los resultados de la consulta
            rows = cursor.fetchall()

            connection.commit()
            # Cerrar la conexión
            connection.close()
            # print(rows)
            return rows

    # La excepcion se utiliza para capturar el mensaje de error que genera el sistema.
    except Error as ex:
        print('Error en la conexion con la BD', ex)


def insertDB(username, password, firstName, lastName):
    try:
        conecction = conexionDB()
        if conecction.is_connected():
            print('Conexión establecida...')

            # Se genera la instancia de la conexion con la base de datos
            cursor = conecction.cursor()

            # Aqui se realiza la sentencia SQL para realizar la insercion de los datos a la tabla, con los datos proporcionados por el usuario.
            query = "INSERT INTO users (nomUser, pasUser, nombre, apellido) VALUES('{0}', '{1}', '{2}', '{3}')".format(username, password, firstName, lastName)

            # Se ejecuta la sentencia de SQL para la insercion en la tabla de la base de datos.
            cursor.execute(query)
            conecction.commit()

            print('Registro Ingresado con Exito !!')

            messagebox.showinfo(message="Registro ingresado con éxito a la Base de Datos: usuarios", title="Mensaje del sistema")

    # La excepcion se utiliza para capturar el mensaje de error que genera el sistema.
    except Error as ex:
        print('Error en la conexion con la BD', ex)