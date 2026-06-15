import sqlite3

# Crear conexión con la base de datos
connection = sqlite3.connect("database.db")

# Leer el archivo SQL
with open("database.sql") as file:
    connection.executescript(file.read())

connection.close()

print("Base de datos creada")