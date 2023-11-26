"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Setup e conexão com o MySQL em Python
=====================================
Executar o seguintes comandos:

$ pip install mysql-connector-python
$ python conexion.py
"""
import mysql.connector
from mysql.connector import Error


try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="senha ao meu DB",
        database='condominio' # ou db="condominio"
    )

    if conexion.is_connected():
        print("Conexão exitosa!")
        infoServer = conexion.get_server_info()
        print("Info do servidor: ", infoServer)

except Error as ex:
    print("Erro durante a conexão: ", ex)

finally:
    if conexion.is_connected():
        conexion.close() # Fechamos a conexão à DB 
        print("A conexão a finalizado.")
