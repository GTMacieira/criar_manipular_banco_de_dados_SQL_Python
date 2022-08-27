#Projeto baseado em 'https://www.freecodecamp.org/portuguese/news/como-criar-e-manipular-bancos-de-dados-sql-com-python/' de 26/08/2022
#password = Pyth0n&SQLP@ss
#Biblioteca para que o Python e o sql se comuniquem
#pip install mysql-connector-python
#Biblioteca pandas
#pip install pandas

#importar o mysql.connector e o pandas para o projeto, a função Error foi importada separada para fácil acesso
import mysql.connector
from mysql.connector import Error
import pandas as pd

#Função que para conectar no MySQL Server
def create_server_connection(host_name, user_name, user_password):
    #Encerra qualquer conexão
    connection = None
    #Tenta criar a conxão
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Dtabase connection successful")
    #Texto caso não consiga conectar
    except Error as err:
        print(f"Error: {err}")
    return connection


#Função que recebe dois argumentos e executa uma consulta no servidor através da conexão
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Dtabase created succrssfully")
    except Error as err:
        print(f'Error: {err}')


pw= 'Pyth0n&SQLP@ss'
connection = create_server_connection("localhost", "root", pw)
