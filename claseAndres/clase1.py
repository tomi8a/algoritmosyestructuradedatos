import sqlite3 as sql

conexion = sql.connect('monedas.db')
print('conectado')
conexion.close
print('desconectado')